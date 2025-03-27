# navigator-qa-smoke-tests

This repository contains smoke tests for the **navigator.ba** website. The tests are written using **Selenium** and **pytest** and aim to verify basic functionalities and key elements of the homepage.

## Prerequisites

Before running the tests, ensure that the following are installed:

- Python 3.13.1
- Selenium 4.30.0
- pytest 8.3.5
- WebDriver (e.g., ChromeDriver or GeckoDriver) - Make sure the appropriate WebDriver for your browser is installed and accessible.

## Installation

### 1. Clone the Repository:

Clone this repository to your local machine:
```bash
git clone https://github.com/gteodora/navigator-qa-smoke-tests.git
```

### 2. Install dependencies:

Clone this repository to your local machine:
```bash
pip install -r requirements.txt
```

## Running tests:

```bash
pytest -s -v
```

## Project structure:

navigator-qa-smoke-tests/
│
├── pages/              # Page Objects (POM)
│   ├── __init__.py
│   ├── homepage_page.py
│   └── categories_page.py
│
├── tests/              # Smoke tests
│   ├── __init__.py
│   ├── test_homepage.py
│   ├── test_categories.py
│   └── test_theaters.py
│
├── utils/
|   ├── driver_factory.py
├── README.md
└── requirements.txt

## TODO

- API tests (pytest and requests)
- More tests for all categories
- Smoke tests for searching
- Smoke tests for creating place
- Smoke tests for suggesting changes

## Author:

https://github.com/gteodora


