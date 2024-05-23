from utils.mock_appium_driver import MockAppiumDriver


class AndroidDriver:
    __android_desired_caps = {}

    def __init__(self):
        self.__android_desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            # Add other desired capabilities here
        }

    def create_driver(self):
        print(f'[AndroidDriver] Initializing driver for {
              self.__android_desired_caps.get('platformName')}')
        return MockAppiumDriver(self.__android_desired_caps)
