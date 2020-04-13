from enum import Enum

from readchar import readchar as readchar # type: ignore

from typing import Optional

def _readchar(_testing: Optional[str]="") -> str:
    """
    Wrapper for the `readchar()` function, but can handle control+c

    For testing, eumlate `_readchar()` inputs by setting `_testing`
    """

    char: str=_testing if _testing else readchar()

    if char=="\x03":
        raise KeyboardInterrupt

    return char

class Action(Enum):
    """
    Different actions that a player can make
    """
    UP=0
    DOWN=1
    LEFT=2
    RIGHT=3
    ACTION=4
    SELECT=5
    OTHER=6

def _read_action(_testing: Optional[str]="") -> Action:
    """
    Read input, and return the corresponding action for that move

    If an input doesnt have a move, Action.OTHER is returned instead
    """
    char=_testing if _testing else _readchar()

    actions={
        "w": Action.UP,
        "s": Action.DOWN,
        "a": Action.LEFT,
        "d": Action.RIGHT,
        "f": Action.SELECT
    }

    return actions.get(char, Action.OTHER)

def read_until_action(_testing: Optional[str]="") -> Action:
    """
    Read user input until a valid action is made
    """
    action=_read_action(_testing)

    if action==Action.OTHER:
        return read_until_action(_testing)
    return action
