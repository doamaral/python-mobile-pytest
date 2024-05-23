from base_page import BasePage
from utils.platforms import Platforms as Platform


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__btn_login = 'com.example.appiumdemo:id/btn_login' if self._platform == Platform.ANDROID.value else "iOS_btn_loginAccessibilityId"

    def click_login(self):
        print(f'Clicking on login button: {self.__btn_login}')
