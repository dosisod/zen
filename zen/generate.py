from random import getrandbits as bits

from zen.render import BrailleArray

def _make_braille() -> BrailleArray:
    """
    Randomly generates a single braille character
    """
    return (
        (bits(1), bits(1)),
        (bits(1), bits(1)),
        (bits(1), bits(1))
    )

def _is_valid(braille: BrailleArray) -> bool:
    """
    Check whether the passed braille array is valid

    It is considered valid if there are no full columns of dots
    """
    return not (
        all([row[0] for row in braille]) or
        all([row[1] for row in braille])
    )

def make_valid_braille() -> BrailleArray:
    """
    Generate a braille character that is valid
    """
    braille=_make_braille()

    return braille if _is_valid(braille) else make_valid_braille()
