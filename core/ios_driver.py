from utils.mock_appium_driver import MockAppiumDriver

class IOSDriver:
    def __init__(self):
        self.ios_desired_caps = {
            'platformName': 'iOS',
            'deviceName': 'iPhone Simulator',
            # Add other desired capabilities here
        }
    
    def create_driver(self):
        return MockAppiumDriver(self.ios_desired_caps)