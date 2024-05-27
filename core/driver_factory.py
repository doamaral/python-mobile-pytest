import os
import logging
from dotenv import load_dotenv
from core.android_driver import AndroidDriver
from core.ios_driver import IOSDriver
from utils.platforms import Platforms as Platform
from utils.logger import logger

load_dotenv(override=False)


class DriverFactory:

    instance = None

    @staticmethod
    def get_instance():
        log = logger(logging.DEBUG)
        if DriverFactory.instance is None:
            platform = os.getenv('PLATFORM', 'android').lower()
            log.info('getting driver instance for %s', platform)

            match platform:
                case Platform.ANDROID.value:
                    android_driver = AndroidDriver()
                    DriverFactory.instance = android_driver.create_driver()
                case Platform.IOS.value:
                    ios_driver = IOSDriver()
                    DriverFactory.instance = ios_driver.create_driver()
                case Platform.CLOUD_ANDROID.value:
                    # TODO: Implement cloud android driver
                    raise ValueError(f'Unsupported platform: {platform}')
                case Platform.CLOUD_IOS.value:
                    # TODO: Implement cloud ios driver
                    raise ValueError(f'Unsupported platform: {platform}')
                case _:
                    raise ValueError(f'Unsupported platform: {platform}')

            log.info('driver instance set for %s', platform)

        return DriverFactory.instance
