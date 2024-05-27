import os
from dotenv import load_dotenv
from appium import webdriver
from appium.options.android import UiAutomator2Options


class AndroidDriver:
    __android_desired_caps = None

    def __init__(self):
        load_dotenv(override=False)

        self.__android_desired_caps = UiAutomator2Options()

        self.__android_desired_caps.platform_version = os.getenv(
            'ANDROID_PLATFORM_VERSION', '14.0')
        self.__android_desired_caps.device_name = os.getenv(
            'ANDROID_DEVICE_NAME', 'Pixel_3a_API_34')

        self.__android_desired_caps.app = os.getcwd() + \
            "/app/android.wdio.native.app.v1.0.8.apk"
        self.__appium_server_url = os.getenv(
            'APPIUM_SERVER_URL', 'http://localhost:4723')

    def create_driver(self):
        print('[AndroidDriver] Initializing')
        return webdriver.Remote(self.__appium_server_url, options=self.__android_desired_caps)
