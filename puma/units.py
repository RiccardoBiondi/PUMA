from typing import Any, Self, Dict
from dataclasses import dataclass
from collections.abc import Mapping

import yaml
from pathlib import Path

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


class ConfusionMatrixMetric(float): 
    def __new__(cls, value: Any) -> Self:

        _value = float(value)

        if (_value < 0.0) | (_value > 1.0):
            raise ValueError(f"Invalid fraction value: {_value}.- ConfusionMatrixMetric must be in [0., 1.] range")
        
        return super().__new__(cls, _value)


class NonNegativeInt(int):
    def __new__(cls, value: Any) -> Self:

        _value = int(value)

        if _value < 0:
            raise ValueError(f"NonNegativeINt must be non-negative")

        return super().__new__(cls, _value)


@dataclass(frozen=True)
class Const:

    value: Any
    name = ""


class Config(Mapping):

    def __new__(cls, config: Dict[str, Any]) -> Self:
        
        return cls(config)

    def __init__(self, config: Dict[str, Any]) -> None:

        _ = [setattr(k, v) for k, v in config.item()]

    def __len__(self) -> int:
        ...

    def __getitem__(self, name: str) -> Any:
        return getattr(name)

    def __iter__(self):
        ...

    @classmethod
    def from_yaml(cls, filename: Path | str) -> Self:
        ...
