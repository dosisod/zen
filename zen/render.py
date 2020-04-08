from typing import Tuple, Sequence, List

BrailleArray=Tuple[
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int]
]

"""
Convert a 2x3 braille array into an actual braille character
"""
def _render_single(braille: BrailleArray) -> str:
    code=0

    for i in range(6):
        code+=braille[i % 3][((i+3) // 3) - 1] * pow(2, i)

    return chr(0x2800 + code)

BrailleArrayN=Tuple[
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...]
]

"""
Convert 3 rows of N length arrays into a braille string
"""
def render_field(braille_arr: BrailleArrayN) -> str:
    def chunk(arr: Tuple[int, ...]) -> List[Tuple[int, int]]:
        pairs: List[Tuple[int, int]]=[]

        for i in range(0, len(arr), 2):
            pair=arr[i:i+2]

            pairs.append(
                pair if len(pair)==2 else (pair[0], 0) # type: ignore
            )

        return pairs

    row1=chunk(braille_arr[0])
    row2=chunk(braille_arr[1])
    row3=chunk(braille_arr[2])

    rendered=""
    for i in range(len(row1)):
        rendered+=_render_single((
            row1[i],
            row2[i],
            row3[i]
        ))

    return rendered