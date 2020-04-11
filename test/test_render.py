from zen.render import _render_single, render_field

def test_render_blank() -> None:
    assert _render_single((
        (0, 0),
        (0, 0),
        (0, 0)
    )) == "\u2800" == "⠀"

def test_render_full() -> None:
    assert _render_single((
        (1, 1),
        (1, 1),
        (1, 1)
    )) == "\u283F" == "⠿"

def test_render_half() -> None:
    assert _render_single((
        (1, 0),
        (0, 1),
        (1, 0)
    )) == "\u2815" == "⠕"

def test_render_field() -> None:
    dots=(
        (1, 1, 0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 0, 0)
    )

    assert render_field(dots) == "⠿⠶⠤⠀"

def test_render_field_with_odd_num_of_cols() -> None:
    dots=(
        (1, 1, 1),
        (1, 1, 1),
        (1, 1, 1)
    )

    assert render_field(dots) == "⠿⠇"
