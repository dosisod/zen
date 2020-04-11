from zen.ui import _readchar, _read_action, read_until_action, Action

def test_getting_single_char() -> None:
    assert _readchar(_testing="a")=="a"

def test_control_c_raises_keyboard_interrupt() -> None:
    try:
        _readchar(_testing="\x03")
    except KeyboardInterrupt:
        return None

    assert False

def test_w_is_action_up() -> None:
    assert _read_action(_testing="w")==Action.UP

def test_s_is_action_down() -> None:
    assert _read_action(_testing="s")==Action.DOWN

def test_a_is_action_left() -> None:
    assert _read_action(_testing="a")==Action.LEFT

def test_d_is_action_right() -> None:
    assert _read_action(_testing="d")==Action.RIGHT

def test_f_is_action_select() -> None:
    assert _read_action(_testing="f")==Action.SELECT

def test_unrecognized_key_is_action_other() -> None:
    assert _read_action(_testing="invalid character")==Action.OTHER

def test_read_until_action_returns_action_if_valid() -> None:
    assert read_until_action(_testing="w")==Action.UP

def test_read_until_action_looping_with_invalid_action() -> None:
    try:
        read_until_action(_testing="invalid character")
    except RecursionError:
        return None

    assert False
