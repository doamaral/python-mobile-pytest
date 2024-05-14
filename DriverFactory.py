import os
from dotenv import load_dotenv

load_dotenv()

class DriverFactory:
    instance = None

    @staticmethod
    def get_instance():
        if DriverFactory.instance is None:
            platform = os.getenv('PLATFORM', 'android').lower()

            if platform == 'android':
                desired_caps = {
                    'platformName': 'Android',
                    'deviceName': 'Android Emulator',
                    # Add other desired capabilities here
                }
                print("##### Android")
            elif platform == 'ios':
                desired_caps = {
                    'platformName': 'iOS',
                    'deviceName': 'iPhone Simulator',
                    # Add other desired capabilities here
                }
                print("##### iOS")
            else:
                raise ValueError(f'Unsupported platform: {platform}')

        return DriverFactory.instance