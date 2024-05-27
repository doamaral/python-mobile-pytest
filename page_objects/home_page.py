from page_objects.base_page import BasePage
from utils.platforms import Platforms as Platform


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.log.info(
            'this page is running over: %s', self._platform)

        # short strategy to define PLATFORM based locators when there are no much options and uses id as strategy by default
        self.__btn_login = 'com.example.appiumdemo:id/btn_login' if self._platform == Platform.ANDROID.value else "iOS_btn_loginAccessibilityId"

        # session to define PLATFORM based locators. you can handle the same component in different ways based on the platform
        match self._platform:
            case Platform.ANDROID.value:
                self.__btn_xpto = {
                    'locatorValue': 'com.example.appiumdemo:id/btn_xpto_ANDROID',
                    'locatorStrategy': 'xpath'
                }
            case Platform.IOS.value:
                self.__btn_xpto = {
                    'locatorValue': 'another.strategy.valid.ios:id/btn_xpto_IOS',
                    'locatorStrategy': 'AccessibilityId'
                }
            case Platform.CLOUD_ANDROID.value:
                self.__btn_xpto = {
                    'locatorValue': 'another.strategy.valid.CLOUD_ANDROID:id/btn_xpto_CLOUD_ANDROID',
                    'locatorStrategy': 'AccessibilityId'
                }
            case Platform.CLOUD_IOS.value:
                self.__btn_xpto = {
                    'locatorValue': 'another.strategy.valid.CLOUD_IOS:id/btn_xpto_CLOUD_IOS',
                    'locatorStrategy': 'AccessibilityId'
                }
            case _:
                raise Exception('Platform not supported')

    def click_login(self):
        self.log.info('clicking on login button: %s', self.__btn_login)

    def click_xpto(self):
        self.click_button(
            self.__btn_xpto["locatorValue"], self.__btn_xpto["locatorStrategy"])
        self.log.info('clicking on xpto button: %s',
                      self.__btn_xpto["locatorValue"])
