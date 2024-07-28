"""Constants
"""

from pathlib import Path
import os

ROOT_PATH = str(Path(__file__).parent) + os.path.sep

DATA_FILE = ROOT_PATH + "data" + os.path.sep + "game.json"

ALIGNMENT = "center"
FONT_SIZE = 12
FONT_NAME = "Arial"
FONT = (FONT_NAME, FONT_SIZE, "normal")
HIGH_SCORE_FONT = (FONT_NAME, FONT_SIZE, "bold")
