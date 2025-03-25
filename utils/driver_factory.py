from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()
    driver.implicitly_wait(10)  # Wait for elements to load
    return driver
