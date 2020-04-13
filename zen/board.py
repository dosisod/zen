from typing import Sequence

from zen.render import BrailleArrayN

class Board:
    """
    Store, filter, and add braille data in a board
    """

    def __init__(self, length: int=16) -> None:
        """
        Construct a board that is 3 dots tall by `length` dots wide
        """
        self._length=length
        self._board=[ [0] * length ] * 3

    def filter(self) -> None:
        """
        Filter each column in the board

        If a column is not filled with ones, ignore it
        Else, remove that column, then shift everything to the left
        """
        for i in range(len(self._board[0])):
            if all([row[i] for row in self._board]):
                for row in range(3):
                    self._board[row].pop(i)
                    self._board[row].append(0)

    def _first_dot(self, data: Sequence[int]) -> int:
        """
        Find the index of the first dot in data

        If it cannot be found, return the length of data instead
        """
        try:
            return data.index(1)
        except ValueError:
            return len(data)

    def _oob(self, data: Sequence[int], index: int) -> int:
        """
        Return the value at the given index

        If it is out of bounds, return zero instead
        """
        try:
            return data[index]
        except IndexError:
            return 0

    def add(self, data: BrailleArrayN) -> None:
        """
        Add braille data to the board

        Data is inserted from the right, stopping when it hits a dot

        Example:

        >>> b=Board(length=4)
        >>> b._board=
        ...    [0, 0, 0, 0],
        ...    [0, 1, 0, 0],
        ...    [0, 0, 0, 0]
        ... ]

        >>> b.add((
        ...    (0, 1, 0),
        ...    (0, 1, 0),
        ...    (0, 1, 0)
        ... ))

        >>> b._board
        [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
        ]
        """

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