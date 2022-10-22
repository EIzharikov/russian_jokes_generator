"""
Useful constant variables
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CUSTOM_MODEL_FOLDER = PROJECT_ROOT / 'models' / 'models_config' / 'custom'
PRETRAINED_MODEL_FOLDER = PROJECT_ROOT / 'models' / 'models_config' / 'pretrained'
PATH_TO_SAVE = PROJECT_ROOT

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
MESSAGE_ENTRY_BOX_COLOR = "#2C3E50"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
