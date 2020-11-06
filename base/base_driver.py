from appium import webdriver
from base.init_driver import init_driver

class BaseDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = init_driver()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
        cls.driver = None

if __name__ == "__main__":
    BaseDriver().get_driver()
