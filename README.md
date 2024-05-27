# Multiplatform Mobile app Test Framework
This is a sample project just to ilustrate how a multiplatform mobile test framework could look like to preserve the same code base for running tests against `iOS` or `Android` platforms.
The idea behind the abstraction is the initial information of which platform should we use. If no platform is informed, we should use `Android` as default.

## Pre requisites
- Node.js run time
- Python 3.12+
- All the environment set up for Appium solutions
  - Install Android Studio
  - Install Appium: `npm install -g appium` This is the appium server
  - Install UIAutomator2: `appium driver install uiautomator2`. The platform specific driver
  - Set JAVA_HOME and ANDROID_HOME to $PATH

- Non mandatory, but helpful
  - Install Appium Inspector: Useful to inspect the app to find elements locators
  - Install Appium doctor: Useful to check environment dependencies

for more info on setting up environment for mobile test automation using Appium, check:
- https://nshthshah.medium.com/appium-tutorial-step-by-step-android-automation-97b84de2fc55
- https://appium.io/docs/en/2.1/quickstart/

## Main libraries used
- [Pytest](https://pypi.org/project/pytest/): To support all test management
- [Dotenv](https://pypi.org/project/python-dotenv/): To support the use of `.env` files
- [Appium Client](https://pypi.org/project/Appium-Python-Client/): the API to interact with the app through drivers like `UIAutomator2` or `XCUITest`

## Project setup
- Clone the repo and cd to the folder
- Set python environment: `python3 -m venv .venv`
- Activate python environment: `source .venv/bin/active`
- Install dependencies: `python3 -m pip install -r requirements.txt`

## Project Structure
### Core package
core package is responsible for the driver management. The main idea is abstract the driver instatiation to provide a single interface to be used throught the code.

- `DriverFactory`
  - Responsible to manage which specific driver is going to be instantiated according to the `PLATFORM` environment variable
  - Make sure we have only one instance available (Singleton)
  - Tests should only call this Class to manage drivers
- `AndroidDriver` and `IOSDriver` are the specific drivers that interface with `Appium Driver` (or the Mocked version) binding the desired capabilities for each platform
- `MockAppiumDriver` is just a dummy class to mock actual Appium/Selenium drivers

### Test files
- `test_driverfactory.py` is the test file
- `hooks.py` is a file to manage hooks used on the tests
- `conftest.py` is a special pytest file to glue any file to the tests

## Running tests
In order to run the tests, we need to pass the value for PLATFORM environment variable. Currently this project supports `Android` and `iOS` values.

IMPORTANT: At this moment, only Android run depends on the full setup, since iOS version is mocking the driver.

There are 2 basic ways to set this variable value:

### Using .env file
To use env file you will need to rename `.env_sample` file to `.env` and set `PLATFORM` variable with the expected value.
```
PLATFORM=Android 
```
or
```
PLATFORM=iOS 
```
after setting up `.env` file, go to the command line and run:
- `$ pytest -s`

**WARNING**: According to `python-dotenv` [library docs](https://pypi.org/project/python-dotenv/), as we use `load_dotenv(override=False)` the precedence of environment variables value will be:
- Value of that variable in the environment.
- Value of that variable in the .env file.
- Default value, if provided.
- Empty string.

### Using on Command line
Here we inform the value for `PLATFORM` straight on the command line, as it follows:
```
$ PLATFORM=iOS pytest -s
```
or
```
$ PLATFORM=Android pytest -s
```
