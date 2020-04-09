from typing import Optional
from pathlib import Path
import os

"""
Allows for easy creation, deletion, and modification of highscore files
"""
class HighScore:
    _score=0

    def __init__(self, save_to: str="./highscore") -> None:
        self._save_to=save_to

    """
    Deletes the highscore file
    """
    def _delete(self) -> None:
        os.remove(self._save_to)

    """
    Creates the highscore file if it hasnt been already
    """
    def _create(self) -> None:
        Path(self._save_to).touch()

    """
    Force save the passed score to the highscore file
    """
    def _save(self, score: int) -> None:
        with open(self._save_to, "w") as f:
            f.write(str(score))

    """
    Write the current score to the highscore file
    """
    def write(self) -> None:
        self._save(self._score)

    """
    Replace the internal highscore if the passed score is higher
    """
    def update(self, score: int) -> None:
        if score >= self._score:
            self._score=score

    """
    Push the passed score to the highscore file if it is higher
    """
    def push(self, score: int) -> None:
        self.update(score)
        self.write()
