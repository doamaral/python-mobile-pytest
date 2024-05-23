import os
from dotenv import load_dotenv
load_dotenv(override=False)


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._platform = os.getenv("PLATFORM").lower()
