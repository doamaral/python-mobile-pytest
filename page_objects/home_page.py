import os
from utils.platforms import Platforms as Platform


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_login = 'com.example.appiumdemo:id/btn_login' if os.getenv(
            "PLATFORM").lower() == Platform.ANDROID.value else "iOS_btn_loginAccessibilityId"

    def click_login(self):
        print(f'Clicking on login button: {self.__btn_login}')
