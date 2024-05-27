import os
from dotenv import load_dotenv
from appium import webdriver
from appium.options.ios import XCUITestOptions


class IOSDriver:
    __ios_desired_caps = None

    def __init__(self):
        load_dotenv(override=False)

        self.__ios_desired_caps = XCUITestOptions()
        self.__ios_desired_caps.platform_version = os.getenv(
            'IOS_PLATFORM_VERSION', '17.5')
        self.__ios_desired_caps.device_name = os.getenv(
            'IOS_DEVICE_NAME', 'iPhone 15 Pro')
        self.__ios_desired_caps.udid = os.getenv(
            "DEVICE_UDID", "5A957BEB-A604-4CBB-9FDF-A1BA47066F59")

        self.__ios_desired_caps.app = os.getcwd() + "/app/Payload/wdiodemoapp.app"

        self.__appium_server_url = os.getenv(
            'APPIUM_SERVER_URL', 'http://localhost:4723')

    def create_driver(self):
        print('[IOSDriver] Initializing driver')
        return webdriver.Remote(self.__appium_server_url, options=self.__ios_desired_caps)
