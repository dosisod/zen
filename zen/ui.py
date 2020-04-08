from enum import Enum

from readchar import readchar as readchar # type: ignore

from typing import Optional

"""
Override the readchar() function from readchar, but allow for control+c

If _testing is set, that will used, otherwise keys are read from user
"""
def _readchar(_testing: Optional[str]="") -> str:
    char: str=_testing if _testing else readchar()

    if char=="\x03":
        raise KeyboardInterrupt

    return char

"""
Enum class with all the possible moves a player could make
"""
class Action(Enum):
    UP=0
    DOWN=1
    LEFT=2
    RIGHT=3
    ACTION=4
    SELECT=5
    OTHER=6

"""
Read input, and return the corresponding action for that move

If an input doesnt have a move, Action.OTHER is returned instead
"""
def _read_action(_testing: Optional[str]="") -> Action:
    char=_testing if _testing else _readchar()

    actions={
        "w": Action.UP,
        "s": Action.DOWN,
        "a": Action.LEFT,
        "d": Action.RIGHT,
        "f": Action.SELECT
    }

    return actions.get(char, Action.OTHER)

"""
Continuously read input until an action that isnt "OTHER" is returned
"""
def read_until_action(_testing: Optional[str]="") -> Action:
    action=_read_action(_testing)

    if action==Action.OTHER:
        return read_until_action(_testing)
    return action
