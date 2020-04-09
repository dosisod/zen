from random import getrandbits as bits

from zen.render import BrailleArray

"""
Randomly generates a single braille character
"""
def _make_braille() -> BrailleArray:
    return (
        (bits(1), bits(1)),
        (bits(1), bits(1)),
        (bits(1), bits(1))
    )

"""
Check if a braille array does not have 3 bots in a row
"""
def _is_valid(braille: BrailleArray) -> bool:
    return not (
        all([row[0] for row in braille]) or
        all([row[1] for row in braille])
    )

"""
Generate braille until a valid character is created, then return it
"""
def make_valid_braille() -> BrailleArray:
    braille=_make_braille()

    return braille if _is_valid(braille) else make_valid_braille()
