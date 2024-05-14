# Pre requisites
- venv installed and environment active
  - `source <ENV_NAME>/bin/active`

# Passing Environment variables to Tests

## Using .env file

```
import os
from dotenv import load_dotenv

load_dotenv()
```

## Passing on Command line

`PLATFORM=iOS pytest -s`