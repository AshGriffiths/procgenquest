from typing import Any

import numpy as np
import scipy.signal
from numpy.typing import NDArray


class DungeonGenerator:
    def __init__(self):
        pass

    def show(self) -> str:
        return ""


class CaveGenerator:
    def __init__(
        self,
        height: int = 30,
        width: int = 70,
        initial_chance: float = 0.45,
        convolve_steps: int = 4,
        wall_rule: int = 5,
    ) -> None:
        tiles: NDArray[np.bool_] = np.random.random((height, width)) > initial_chance
        for _ in range(convolve_steps):
            tiles = self._convolve(tiles, wall_rule)
            tiles[[0, -1], :] = 0
            tiles[:, [0, -1]] = 0
        self.tiles = tiles

    def _convolve(self, tiles: NDArray[Any], wall_rule: int) -> NDArray[np.bool_]:
        neighbours: NDArray[Any] = scipy.signal.convolve2d(
            tiles == 0, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "same"
        )
        next_tiles: NDArray[np.bool_] = neighbours < wall_rule
        return next_tiles

    def show(self) -> str:
        output = ""
        for line in self.tiles:
            output += "".join("# "[int(cell)] for cell in line) + "\n"
        return output
