# NASA Units

NASA Units is a Python module for automatic unit conversion.

---

## Installation

You can install the package directly from GitHub.
For new installation:

```bash
pip install git+https://github.com/bhearley/NASAUnits.git
```

For updating an existing installation:

```bash
pip install --force-reinstall git+https://github.com/bhearley/NASAUnits.git
```

---

## Usage

To use the module

1. Import the module
   
```bash
from nasaunits import UnitConversion
```

2. Define Source Unit, Source Value, and Target Unit
Source and Target Units must be strings present in the unit library. The unit library can be found and added to at: https://github.com/bhearley/NASAUnits/new/main/unit_library.json

```bash
source_unit = '°C'
source_value = 316
target_value = '°F'
```
   
3. Perform Conversion
```bash
target_value = UnitConversion(source_unit, source_value, target_value)
```

---

## Dependencies
- requests

These are installed automatically with the package.

---
## Contact
For questions or feedback, contact Brandon Hearley at brandon.l.hearley@nasa.gov
