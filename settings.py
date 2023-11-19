import os
from pathlib import Path

import yaml

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

# virtual environment variables
TOKEN = os.getenv("TOKEN")

# Stages
FIRST_STATE, SECOND_STATE, THIRD_STATE, FOURTH_STATE = range(4)

# text variables
with open(os.path.join(BASE_DIR, r'config.yaml'), 'r', encoding="utf-8") as data_f:
    CONFIG = yaml.load(data_f, yaml.BaseLoader)

GREETINGS_TEXT: str = CONFIG["GREETINGS_TEXT"]
OPTIONS_FIRST_TEXT: str = CONFIG["OPTIONS_FIRST_TEXT"]
OPTIONS_FURTHER_TEXT: str = CONFIG["OPTIONS_FURTHER_TEXT"]
ABOUT_COMPANY_TEXT: str = CONFIG["ABOUT_COMPANY_TEXT"]
PRODUCTION_LEVEL_TEXT: str = CONFIG["PRODUCTION_LEVEL_TEXT"]

ORDERS_TEXT: str = CONFIG["ORDERS_TEXT"]
CHECK_CONTRACT_TEXT: str = CONFIG["CHECK_CONTRACT_TEXT"]

LOOK_CONTRACT_TEXT: str = CONFIG["LOOK_CONTRACT_TEXT"]
LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT: str = CONFIG["LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT"]

NOT_REALIZED_YET: str = CONFIG["NOT_REALIZED_YET"]
UNKNOWN_COMMAND: str = CONFIG["UNKNOWN_COMMAND"]

DB_NAME: str = CONFIG["DB_NAME"] + ".sqlite3"
CONTRACT_STATUSES: list[str] = CONFIG["CONTRACT_STATUSES"]
