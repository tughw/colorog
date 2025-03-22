# colorog

[![PyPI version](https://img.shields.io/pypi/v/colorog.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/colorog)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/colorog.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/colorog)
[![GitHub Actions status](https://github.com/termcolor/termcolor/workflows/Test/badge.svg)](https://github.com/termcolor/termcolor/actions)
[![Licence](https://img.shields.io/pypi/l/colorog)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

![colors.png](colors.png)

## Installation

### From PyPI

```bash
python3 -m pip install --upgrade colorog
```

### Demo

To see demo output, run:

```bash
python3 -m colorog
```

## Example

```python
from colorog import log_info, log_success

log_info("This is info")
log_success("This is success")
# ...
```
