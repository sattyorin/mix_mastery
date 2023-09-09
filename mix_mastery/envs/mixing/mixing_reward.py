from typing import Any
import numpy as np


class MixingReward:
    def __init__(self, mode: str):
        if mode == "hoge":
            self.get_reword = self.get_reword_hoge()
        elif mode == "piyo":
            self.get_reword = self.get_reword_piyo()

    def __call__(self, *args: Any, **kwds: Any) -> np.ndarray:
        return self.get_reword

    def get_reword_hoge(self, observation: np.ndarray) -> np.ndarray:
        # servo_position = observation[:7]
        # servo_velocity = observation[7:14]
        ingredient_position = observation[14:]
        return

    def get_reword_piyo(self, observation: np.ndarray) -> np.ndarray:
        # servo_position = observation[:7]
        # servo_velocity = observation[7:14]
        ingredient_position = observation[14:]
        return
