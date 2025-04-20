from typing import List

import numpy as np

from ..environment.actions import MbagAction, MbagActionTuple
from ..environment.blocks import MinecraftBlocks
from ..environment.types import MbagObs
from .mbag_agent import MbagAgent

class SimpleGoalGeneratorAgent(MbagAgent):
    """
    Gets resources, then tries to build the simple goal generator
    """

    current_command: int

    def reset(self, **kwargs):
        super().reset(**kwargs)
        self.current_command = 0

    def get_action(self, obs: MbagObs) -> MbagActionTuple:
        command_list: List[MbagActionTuple] = [
            # Move to starting position
            (MbagAction.MOVE_NEG_Y, 0, 0),
            (MbagAction.MOVE_POS_Y, 0, 0),
            (MbagAction.MOVE_NEG_X, 0, 0),
            (MbagAction.MOVE_NEG_Z, 0, 0),
            # Place first row of blocks
            (
                MbagAction.PLACE_BLOCK,
                int(
                    np.ravel_multi_index(
                        (1, 2, 1),
                        self.env_config["world_size"],
                    )
                ),
                MinecraftBlocks.NAME2ID["cobblestone"],
            ), ]
        #     (MbagAction.MOVE_POS_X, 0, 0),
        #     (MbagAction.MOVE_POS_X, 0, 0),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (2, 2, 1),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (3, 2, 1),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     # Place second row of blocks
        #     (MbagAction.MOVE_POS_Y, 0, 0),
        #     (MbagAction.MOVE_POS_Z, 0, 0),
        #     (MbagAction.MOVE_POS_Z, 0, 0),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (1, 2, 2),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (2, 2, 2),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (3, 2, 2),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     # Place third row of blocks
        #     (MbagAction.MOVE_POS_Z, 0, 0),
        #     (MbagAction.MOVE_NEG_Z, 0, 0),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (1, 2, 3),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (2, 2, 3),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        #     (
        #         MbagAction.PLACE_BLOCK,
        #         int(
        #             np.ravel_multi_index(
        #                 (3, 2, 3),
        #                 self.env_config["world_size"],
        #             )
        #         ),
        #         MinecraftBlocks.NAME2ID["cobblestone"],
        #     ),
        # ]
        if self.current_command >= len(command_list):
            return (MbagAction.NOOP, 0, 0)

        action = command_list[self.current_command]
        self.current_command += 1
        return action

    def get_state(self) -> List[np.ndarray]:
        return [np.array([self.current_command])]

    def set_state(self, state: List[np.ndarray]) -> None:
        self.current_command = int(state[0][0])
