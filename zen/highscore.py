from typing import Optional
from pathlib import Path
import os

class HighScore:
    """
    Allows for easy creation, deletion, and modification of highscore files
    """

    _score=0

    def __init__(self, save_to: str="./highscore") -> None:
        self._save_to=save_to

    def _delete(self) -> None:
        """
        Deletes the highscore file
        """
        os.remove(self._save_to)

    def _create(self) -> None:
        """
        Creates the highscore file if it hasnt been already
        """
        Path(self._save_to).touch()

    def _save(self, score: int) -> None:
        """
        Force save the passed score to the highscore file
        """
        with open(self._save_to, "w") as f:
            f.write(str(score))

    def write(self) -> None:
        """
        Write the current score to the highscore file
        """
        self._save(self._score)

    def update(self, score: int) -> None:
        """
        Replace the internal highscore if the passed score is higher
        """
        if score >= self._score:
            self._score=score

    def push(self, score: int) -> None:
        """
        Push the passed score to the highscore file if it is higher
        """
        self.update(score)
        self.write()
