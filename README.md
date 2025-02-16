# gowtham_hello

## Overview
gowtham_hello is a lightweight Python package that prints a greeting message. It serves as a basic example for creating, packaging, and distributing a Python module. This repository includes the package source code, setup instructions, and a test script to verify installation.

## Project Structure
```
gowtham_hello/
│── gowtham_hello/
│   ├── __init__.py
│   ├── main.py
│── testing/
│   ├── main.py
│── setup.py
│── README.md
```

- `__init__.py`: Initializes the package and imports necessary modules.
- `main.py`: Contains the `hello()` function that prints a greeting message.
- `setup.py`: Defines package metadata and dependencies.
- `testing/main.py`: Used to test the installed package.
- `README.md`: Documentation for the package.

## Installation
To install the package, use the following command:

```
pip install .
```

If you want to create a distributable package, run:

```
python setup.py sdist bdist_wheel
```

This will generate a package file named:
```
dist/gowtham_hello-0.3-py3-none-any.whl
```

## Testing
After installing the package, you can test it using the `testing` folder:

```python
from gowtham_hello.main import hello

hello()
```

You should see the following output on the screen:
```
Hello this is Gowtham!
```

## Requirements
This package requires:
- Python 3.x
- `numpy` version 2.0 or later

## Notes
- Ensure that the `setup.py` file has correct spellings for `packages` and `install_requires`.
- If any issues occur during installation, check dependencies and Python version.

## Author
Gowtham Tadavarthy

## License
This project is licensed under the MIT License.

