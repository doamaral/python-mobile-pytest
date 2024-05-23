import os
from dotenv import load_dotenv
load_dotenv(override=False)


class BasePage:
    def __init__(self):
        # Super class constructor will set the platform value
        self._platform = os.getenv("PLATFORM").lower()

    def get_platform(self):
        return self._platform
