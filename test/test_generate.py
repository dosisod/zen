from zen.generate import _make_braille, _is_valid, make_valid_braille

class TestGenerate:
    def test_make_braille__is_valid(self) -> None:
        braille=_make_braille()

        assert len(braille) == 3
        assert len(braille[0]) == len(braille[1]) == len(braille[2]) == 2

    def test__is_valid_with_invalid_braille_returns_false(self) -> None:
        assert not _is_valid((
            (1, 0),
            (1, 0),
            (1, 0)
        ))

        assert not _is_valid((
            (0, 1),
            (0, 1),
            (0, 1)
        ))

        assert not _is_valid((
            (1, 1),
            (1, 1),
            (1, 1)
        ))

    def test__is_valid_with_valid_braille_returns_true(self) -> None:
        assert _is_valid((
            (0, 0),
            (0, 0),
            (0, 0)
        ))

        assert _is_valid((
            (1, 0),
            (1, 0),
            (0, 0)
        ))

    def test_make_valid_braille_returns_valid_braille(self) -> None:
        assert all([
            _is_valid(make_valid_braille()),
            _is_valid(make_valid_braille()),
            _is_valid(make_valid_braille()),
            _is_valid(make_valid_braille())
        ])
