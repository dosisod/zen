from pathlib import Path
import os

from zen.highscore import HighScore

SAVE_TO="./test/data/highscore"

class TestHighScore:
    def test_creating_highscore_object(self) -> None:
        hs=HighScore(save_to=SAVE_TO)
        assert hs._save_to == SAVE_TO

        hs=HighScore()
        assert hs._save_to

    def test_deletion_of_highscore_file(self) -> None:
        hs=HighScore(save_to=SAVE_TO)

        # create empty file
        Path(SAVE_TO).touch()

        assert os.path.isfile(SAVE_TO)
        hs._delete()
        assert not os.path.isfile(SAVE_TO)

    def test_creation_of_highscore_file(self) -> None:
        hs=HighScore(save_to=SAVE_TO)

        if os.path.isfile(SAVE_TO):
            os.remove(SAVE_TO)

        assert not os.path.isfile(SAVE_TO)
        hs._create()
        assert os.path.isfile(SAVE_TO)

        os.remove(SAVE_TO)

    def test_saving_data_to_highscore_file(self) -> None:
        hs=HighScore(save_to=SAVE_TO)
        hs._create()

        assertSaveFile(equals="")
        hs._save(1234)
        assertSaveFile(equals="1234")

        hs._delete()

    def test_updating_highscore(self) -> None:
        hs=HighScore()
        hs.update(1234)

        assert hs._score == 1234

    def test_score_must_be_higher_to_update(self) -> None:
        hs=HighScore()
        hs.update(-1234)

        assert hs._score == 0

    def test_writing_score_to_file(self) -> None:
        hs=HighScore(save_to=SAVE_TO)
        hs._create()

        assertSaveFile(equals="")
        hs.update(1234)
        hs.write()
        assertSaveFile(equals="1234")

        hs._delete()

    def test_push_highscore(self) -> None:
        hs=HighScore(save_to=SAVE_TO)
        hs._create()

        hs.push(1234)

        assertSaveFile(equals="1234")
        hs.push(0)
        assertSaveFile(equals="1234")

        hs._delete()

def assertSaveFile(equals: str) -> None:
    with open(SAVE_TO, "r") as f:
        assert f.read() == equals
