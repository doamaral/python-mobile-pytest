import os
import logging
from dotenv import load_dotenv
from utils.logger import logger
load_dotenv(override=False)


class BasePage:
    log = logger(logging.DEBUG)

    def __init__(self):
        # Super class constructor will set the platform value
        self._platform = os.getenv("PLATFORM").lower()
        self.log.info('initializing page for platform: %s', self._platform)

    def get_platform(self):
        return self._platform

    def click_button(self, locator_value, locator_strategy="id"):
        self.log.info('clicking on button: %s using strategy %s',
                      locator_value, locator_strategy)
