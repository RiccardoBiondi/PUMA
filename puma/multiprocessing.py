import shutil
from multiprocessing.pool import ThreadPool

from typing import Union, Iterable, Callable, Tuple

__author__ = ["Riccardo Biondi"]
__email__ = ["riccardo.biondi7@unibo.it"]

class MultithreadedCopier:
    """
    A context manager for performing multithreaded file or path copying operations.

    This class enables efficient parallel copying of multiple files or directories
    using a user-specified copy function (e.g., `shutil.copy`, `shutil.copy2`, or a
    custom implementation). The copy function must accept two positional arguments:
    the source path and the destination path.

    The copier manages a thread pool and ensures that all threads are properly
    closed and joined when exiting the context.

    Parameters
    ----------
    max_threads : int, optional
        The maximum number of worker threads to use for concurrent copying.
        Defaults to 2.
    copy_function : Callable[[str, str], None], optional
        A function that takes a source path and a destination path and performs
        the copy operation. Defaults to `shutil.copy`.

    Examples
    --------
    Copy multiple files to specific destinations in parallel:

    >>> import shutil
    >>> with MultithreadedCopier(max_threads=4, copy_function=shutil.copy2) as copier:
    ...     copier.copy(
    ...         ["a.txt", "b.txt", "c.txt"],
    ...         ["backup/a.txt", "backup/b.txt", "backup/c.txt"]
    ...     )

    Copy several files into a single destination directory:

    >>> with MultithreadedCopier() as copier:
    ...     copier.copy(["file1.txt", "file2.txt"], "backup_dir/")
    """
    def __init__(self, max_threads: int = 2, copy_function: Callable[[str, str], None] = shutil.copy):
        """
        Initialize the multithreaded copier with a thread pool and copy function.

        Parameters
        ----------
        max_threads : int, optional
            The maximum number of concurrent threads to use. Defaults to 2.
        copy_function : Callable[[str, str], None], optional
            A callable responsible for performing the copy operation.
            Must accept `(source, destination)` arguments.
        """

        self.pool = ThreadPool(max_threads)
        self.copier = copy_function

    def _copy_wrapper(self, x: Tuple[str, str]):
        """
        Internal helper that wraps the copy function for use with the thread pool.

        Parameters
        ----------
        x : Tuple[str, str]
            A tuple containing the source path and destination path to copy.
        """

        _ = self.copier(x[0], x[1])


    def copy(self, source_list: Iterable[str], dest: Union[Iterable[str], str]):
        """
        Perform parallel copying of multiple files or paths.

        Parameters
        ----------
        source_list : Iterable[str]
            An iterable of source paths to copy.
        dest : Union[Iterable[str], str]
            Either a single destination path (applied to all sources) or an iterable
            of destination paths matching the length of `source_list`.

        Raises
        ------
        ValueError
            If `dest` is an iterable and its length does not match that of `source_list`.
        """
        
        dest_list = dest
        if isinstance(dest_list, str): 
            dest_list = len(source_list)*[dest_list]

        self.pool.map(self._copy_wrapper, zip(source_list, dest_list))


    def __enter__(self):
        """
        Enter the context manager.

        Returns
        -------
        MultithreadedCopier
            The instance itself, allowing use within a `with` statement.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager, ensuring all threads are properly closed.

        Parameters
        ----------
        exc_type : Optional[Type[BaseException]]
            The exception type, if an exception was raised within the context.
        exc_val : Optional[BaseException]
            The exception instance, if any.
        exc_tb : Optional[TracebackType]
            The traceback object associated with the exception, if any.

        Notes
        -----
        All threads in the pool are closed and joined upon exiting the context,
        ensuring that no background operations are left running.
        """
        self.pool.close()
        self.pool.join()