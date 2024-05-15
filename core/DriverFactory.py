import os
from core.AndroidDriver import AndroidDriver
from core.IOSDriver import IOSDriver
from dotenv import load_dotenv

load_dotenv()

class DriverFactory:
    instance = None

    @staticmethod
    def get_instance():
        if DriverFactory.instance is None:
            platform = os.getenv('PLATFORM', 'android').lower()

            if platform == 'android':
                android_driver = AndroidDriver()
                DriverFactory.instance = android_driver.create_driver()

            elif platform == 'ios':
                ios_driver = IOSDriver()
                DriverFactory.instance = ios_driver.create_driver()
            else:
                raise ValueError(f'Unsupported platform: {platform}')

        return DriverFactory.instance