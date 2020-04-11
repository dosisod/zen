from zen.board import Board

class TestBoard:
    def test_creating_board(self) -> None:
        board1=Board(length=1)
        assert board1._length != 0

        board2=Board()
        assert board2._length != 0

    def test_board_setup(self) -> None:
        board=Board(length=4)

        assert board._board == [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def test_board_filtering_full_columns(self) -> None:
        board=Board(length=4)

        board._board=[
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1]
        ]

        board.filter()

        assert board._board == [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]

    def test_first_dot(self) -> None:
        board=Board()

        assert board._first_dot([1]) == 0
        assert board._first_dot([0, 0, 1]) == 2
        assert board._first_dot([0, 0, 0]) == 3

    def test_oob(self) -> None:
        board=Board()

        assert board._oob([0], 100) == 0
        assert board._oob([1], 0) == 1

    def test_adding_data_to_board(self) -> None:
        board=Board(length=6)

        board._board=[
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0]
        ]

        board.add((
            (0, 0, 1),
            (0, 1, 1),
            (1, 1, 1)
        ))

        assert board._board == [
            [1, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0]
        ]

    def test_adding_data_to_board2(self) -> None:
        board=Board(length=6)

        board._board=[
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        board.add((
            (0, 0, 1),
            (0, 1, 1),
            (1, 1, 1)
        ))

        assert board._board == [
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0]
        ]
