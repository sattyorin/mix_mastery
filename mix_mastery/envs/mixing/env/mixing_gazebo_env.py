import random
from typing import Dict, Tuple

import gym
from gym.spaces import Box
import numpy as np

import rt_manipulators_python_ros
import mixing_image_processor
from mixing_reward import MixingReward

_FRAME_SKIP = 1
_TIME_STEP = 0.1
REWARD_MODE = "hoge"


class MixingGazeboEnv(gym.Env):
    metadata = {
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
        "render_fps": np.round(1.0 / (_TIME_STEP * _FRAME_SKIP)),
    }

    def __init__(self, **kwargs) -> None:
        np.random.seed(0)
        random.seed(0)
        self.crane_manipulators = rt_manipulators_python_ros.CraneManipulators()
        self.ingredient_detector = mixing_image_processor.ingredient_detector
        self.mixing_reword = MixingReward(REWARD_MODE)

        self.action_space = Box(
            low=np.zeros(7),
            high=np.ones() * 0.3,
            shape=7,
            dtype=np.float32,
        )

        self.observation_space: Box = Box(
            low=-np.inf,
            high=np.inf,
            shape=(
                # servo_num(position) +
                # servo_num(velocity) +
                # ingredient_pose * num_ingredients,
            ),
            dtype=np.float64,
        )

        self.reward_range  # ?

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, bool, dict]:
        # action: 各関節の電流値 [0.1, 0.3, 0.5, 0.4 .....]

        self.crane_manipulators.write_current(current)
        observation = self._get_observation()
        reward, terminated = self._stir_env.get_reward(observation)
        self._stir_env.step_variables(observation)
        info: Dict[str, str] = {}

        return observation, reward, terminated, False, info

    def reset(self) -> np.ndarray:
        self.crane_manipulators.torque_off()
        self.crane_manipulators.change_operation_mode("position")
        self.crane_manipulators.move_init_position()  # 寝かせる
        self.crane_manipulators.change_operation_mode("current")
        self.crane_manipulators.init_motion()

        return self._get_observation()

    def render(self) -> None:
        return

    def _get_observation(self) -> np.ndarray:
        # observation[ロボットの各関節角度, 食材の位置, ...]

        servo_position = self.crane_manipulators.read_position()
        servo_velocity = self.crane_manipulators.read_velocity()
        ingredient_position = self.ingredient_detector.get_position()
        return np.concatenate([servo_position, servo_velocity, ingredient_position])

    def _get_reward(self) -> np.ndarray:
        return self.mixing_reword(), self._get_terminated()

    def _get_terminated(self) -> bool:
        # 終了条件判定
        return False
