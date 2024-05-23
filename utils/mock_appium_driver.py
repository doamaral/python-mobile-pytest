class MockAppiumDriver:
    def __init__(self, desired_caps):
        self._desired_caps = desired_caps
        self._platform_name = desired_caps.get('platformName')
        self._device_name = desired_caps.get('deviceName')
        print(f'[MockAppiumDriver] Setting desired capabilities for {
              self._platform_name}')
        print(f'[MockAppiumDriver] Device name: {self._device_name}')

    def get_platform_name(self):
        return self._platform_name

    def find_element_by_id(self, element_id):
        print(f'[MockAppiumDriver] Finding element by id: {element_id}')

    def find_element_by_name(self, name):
        print(f'[MockAppiumDriver] Finding element by name: {name}')

    def find_element_by_xpath(self, xpath):
        print(f'[MockAppiumDriver] Finding element by xpath: {xpath}')
