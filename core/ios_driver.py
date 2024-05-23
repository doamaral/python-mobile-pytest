from utils.mock_appium_driver import MockAppiumDriver


class IOSDriver:
    __ios_desired_caps = {}

    def __init__(self):
        self.__ios_desired_caps = {
            'platformName': 'iOS',
            'deviceName': 'iPhone Simulator',
            # Add other desired capabilities here
        }

    def create_driver(self):
        print(f'[IOSDriver] Initializing driver for {
              self.__ios_desired_caps.get('platformName')}')
        return MockAppiumDriver(self.__ios_desired_caps)
