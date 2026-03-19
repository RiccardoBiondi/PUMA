from typing import Any, Self
from dataclasses import dataclass

__author__ = ["Riccardo Biondi"]


class HU(int):
    """
    """
    def __new__(cls, value: Any) -> Self:
        
        _value = int(value)

        if (_value < -4096) | (_value > 4096):
            raise ValueError("Hounsifield Units cannot be higher than 4096 and lower than -4096")

        return super().__new__(cls, _value)
    


class Fraction(float):
    """
    """
    def __new__(cls, value: Any) -> Self:

        _value = float(value)

        if (_value < 0.0) | (_value > 1.0):
            raise ValueError(f"Invalid fraction value: {_value}.- Fraction must be in [0., 1.] range")
        
        return super().__new__(cls, _value)
    

class Percentage(float):
    """
    """
    def __new__(cls, value: Any):

        _value = float(value)

        if (_value < 0.0) | (_value > 100.0):
            raise ValueError(f"Invalid percentage value: {_value}.- PErcentage must be in [0., 100.] range")
        
        return super().__new__(cls, _value)


@dataclass(frozen=True)
class Const:

    value: Any
    name = ""
