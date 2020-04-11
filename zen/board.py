from typing import Sequence

from zen.render import BrailleArrayN

class Board:
    def __init__(self, length: int=16) -> None:
        self._length=length

        self._board=[ [0] * length ] * 3

    """
    Filter each column in the board

    If there are 3 1s in a column, remove them, and shift the board over
    """
    def filter(self) -> None:
        for i in range(len(self._board[0])):
            if all([row[i] for row in self._board]):
                for row in range(3):
                    self._board[row].pop(i)
                    self._board[row].append(0)

    def _first_dot(self, data: Sequence[int]) -> int:
        try:
            return data.index(1)
        except ValueError:
            return len(data)

    """
    Return the value at the given index, or zero if it is out of bounds
    """
    def _oob(self, data: Sequence[int], index: int) -> int:
        try:
            return data[index]
        except IndexError:
            return 0

    """
    Add braille data by shifting it down the board until it hits a dot
    """
    def add(self, data: BrailleArrayN) -> None:
        first_dots=[self._first_dot(row) for row in data]

        insert_at=0
        for i in reversed(range(self._length + len(data))):
            if any([self._oob(self._board[j], i + first_dots[j] - 1) for j in range(3)]):
                insert_at=i
                break

        for i in range(3):
            for j in range(len(data[i])):
                if data[i][j]:
                    self._board[i][j + insert_at]=data[i][j]