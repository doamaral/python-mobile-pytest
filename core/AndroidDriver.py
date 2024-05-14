from core.FakeAppiumDriver import FakeAppiumDriver

class AndroidDriver:
    def __init__(self):
        self.android_desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            # Add other desired capabilities here
        }
        
    def create_driver(self):
        return FakeAppiumDriver(self.android_desired_caps)