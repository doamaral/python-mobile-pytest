import os
from dotenv import load_dotenv
from core.android_driver import AndroidDriver
from core.ios_driver import IOSDriver
from utils.platforms import Platforms as Platform
load_dotenv(override=False)


class DriverFactory:

    instance = None

    @staticmethod
    def get_instance():
        """
        Returns the instance of the driver based on the platform 
        specified in the environment variable 'PLATFORM'.

        If the instance is not already created, it creates a new instance of the 
        driver based on the platform. The platform can be either 'android' or 'ios'.

        Returns:
            The instance of the driver.

        Raises:
            ValueError: If the platform specified is not supported.
        """
        if DriverFactory.instance is None:
            platform = os.getenv('PLATFORM', 'android').lower()

            if platform == Platform.ANDROID.value:
                android_driver = AndroidDriver()
                DriverFactory.instance = android_driver.create_driver()

            elif platform == Platform.IOS.value:
                ios_driver = IOSDriver()
                DriverFactory.instance = ios_driver.create_driver()
            else:
                raise ValueError(f'Unsupported platform: {platform}')

        return DriverFactory.instance
