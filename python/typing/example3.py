from dataclasses import dataclass
from typing import Union


@dataclass
class Cica:
    """cica"""

    name: str
    legs: Union[int, float]

    def legs_missing(self) -> Union[int, float]:
        return 4 - self.legs


cirmos = Cica("cirmos", 4)
nem_cirmos = Cica(12, "egy")
labatlan_cirmos = Cica("labatlan cirmos", cirmos.legs_missing())
