class MockAppiumDriver:
    def __init__(self, desired_caps):
        self.capabilities = desired_caps

    def find_element_by_id(self, element_id):
        print(f'[MockAppiumDriver] Finding element by id: {element_id}')

    def find_element_by_name(self, name):
        print(f'[MockAppiumDriver] Finding element by name: {name}')

    def find_element_by_xpath(self, xpath):
        print(f'[MockAppiumDriver] Finding element by xpath: {xpath}')
