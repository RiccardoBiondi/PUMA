from typing import Callable, Any, Optional, List


class Registry:
    """Generic implementation of the Registry pattern using a hash map.
    """

    def __init__(self):
        """Initialize the registry with an empty internal store."""
        self._store: dict[str, Callable[[Any], Any]] = {}

    
    def __getitem__(self, key: str) -> Callable[[Any], Any]:
        return self.get(key)
    

    def register(self, keys: str | List[str], value: Optional[Callable[[Any], Any]] = None) -> None:
        """Register a key-value pair to the registry.

        This method checks for key collisions to ensure uniqueness.

        Args:
            key (Key): The unique identifier for the stored value.
            value (Value): The item (object, class, or callable) to store.

        Raises:
            ValueError: If the key is already registered.
        """
        if isinstance(keys, str):
            keys = [keys]
    
        if value is not None:
            _ = [self._do_register(key, value) for key in keys]
            return value

        # Case 2 & 3: decorator usage
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            for key in keys:
                register_key = key or func.__name__
                self._do_register(register_key, func)
            return func

        return decorator

    def _do_register(self, key: str, value: Callable[..., Any]) -> None:
        if key in self._store:
            raise ValueError(f"Key '{key}' is already registered.")

        self._store[key] = value

    def get(self, key: str) -> Callable[[Any], Any]:
        """Retrieve a value by its key.

        Args:
            key (Key): The unique identifier to look up.

        Returns:
            Value: The stored value associated with the key.

        Raises: 
            KeyError: If the key is not found in the registry.
        """
        if value := self._store.get(key):
            return value
        else:
            raise KeyError(f"Key '{key}' not found in registry.")

    def unregister(self, key: str) -> None:
        """Remove a key-value pair from the registry.

        Args:
            key (Key): The unique identifier of the item to remove.

        Raises:
            KeyError: If the key is not found in the registry.
        """
        if key not in self._store:
            raise KeyError(f"Key '{key}' not found in registry.")
        del self._store[key]

    def __contains__(self, key: str) -> bool:
        """Checks if a key exists in the registry.

        This method enables the use of the 'in' operator (e.g., `if key in registry:`).

        Args:
            key (Key): The unique identifier to check.

        Returns:
            bool: True if the key is registered, False otherwise.
        """
        return key in self._store

    def list_keys(self) -> list[str]:
        """Return a list of all keys currently registered.

        Returns:
            list[Key]: A list containing all registered keys.
        """
        return list(self._store.keys())
