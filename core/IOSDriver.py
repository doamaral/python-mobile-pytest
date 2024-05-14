from core.FakeAppiumDriver import FakeAppiumDriver

class IOSDriver:
    def __init__(self):
        self.ios_desired_caps = {
            'platformName': 'iOS',
            'deviceName': 'iPhone Simulator',
            # Add other desired capabilities here
        }
    
    def create_driver(self):
        return FakeAppiumDriver(self.ios_desired_caps)