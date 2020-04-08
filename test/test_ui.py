from zen.ui import _readchar, _read_action, read_until_action, Action

class TestUI:
    def test_getting_single_char(self) -> None:
        assert _readchar(_testing="a")=="a"

    def test_control_c_raises_keyboard_interrupt(self) -> None:
        try:
            _readchar(_testing="\x03")
        except KeyboardInterrupt:
            return None

        assert False

    def test_w_is_action_up(self) -> None:
        assert _read_action(_testing="w")==Action.UP

    def test_s_is_action_down(self) -> None:
        assert _read_action(_testing="s")==Action.DOWN

    def test_a_is_action_left(self) -> None:
        assert _read_action(_testing="a")==Action.LEFT

    def test_d_is_action_right(self) -> None:
        assert _read_action(_testing="d")==Action.RIGHT

    def test_f_is_action_select(self) -> None:
        assert _read_action(_testing="f")==Action.SELECT

    def test_unrecognized_key_is_action_other(self) -> None:
        assert _read_action(_testing="invalid character")==Action.OTHER

    def test_read_until_action_returns_action_if_valid(self) -> None:
        assert read_until_action(_testing="w")==Action.UP

    def test_read_until_action_looping_with_invalid_action(self) -> None:
        try:
            read_until_action(_testing="invalid character")
        except RecursionError:
            return None

        assert False
