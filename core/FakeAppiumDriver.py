class FakeAppiumDriver:
    def __init__(self, desired_caps):
        print('Initializing FakeAppiumDriver')
        self._desired_caps = desired_caps
        self._platformName = desired_caps.get('platformName')
        self._deviceName = desired_caps.get('deviceName')
        
        print(f'Platform name: {self._platformName}')
        print(f'Device name: {self._deviceName}')

    def find_element_by_id(self, id):
        print(f'Finding element by id: {id}')

    def find_element_by_name(self, name):
        print(f'Finding element by name: {name}')

    def find_element_by_xpath(self, xpath):
        print(f'Finding element by xpath: {xpath}')
