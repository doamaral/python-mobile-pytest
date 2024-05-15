# Pre requisites
- git clone
- cd to the project folder 
- `python3 -m venv .venv`
- `source .venv/bin/active`
- `python3 -m pip install -r requirements.txt`

# Structure
## core package
core package is responsible for the driver management.
- `DriverFactory`
  - Responsible to manage which specific driver is going to be instantiated according to the `PLATFORM` environment variable
  - Make sure we have only one instance available (Singleton)
- `AndroidDriver` and `IOSDriver` are the specific drivers that interface with `FakeAppiumDriver` binding the desired capabilities for each driver
- `FakeAppiumDriver` is just a dummy class to mock actual Appium/Selenium drivers

## tests
- `test_driverfactory.py` is the test file
- `hooks.py` is a file to manage hooks used on the tests
- `conftest.py` is a special pytest file to glue any file to the tests

# Passing Environment variables to Tests
## Using .env file

```
import os
from dotenv import load_dotenv

load_dotenv()
```

## Passing on Command line

`PLATFORM=iOS pytest -s`