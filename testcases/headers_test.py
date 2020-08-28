from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.header import Header
from utilities.customLogger import LogGen
from utilities.siteConfig import siteconfig
from selenium.common.exceptions import ElementNotInteractableException
import time


class Test_1:
    base_url = siteconfig.getsiteURl()
    base_xpath = siteconfig.getheaderXPATH()
    logger = LogGen.loggen()


    def test_pagetitle(self, setup):
        self.logger.info("*************** page title test ****************")
        driver = setup
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(5)
        title = driver.title
        time.sleep(3)
        driver.close()
        if title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            self.logger.info("*************** page title passed ****************")
            assert True
        else:
            driver.save_screenshot(".\\screenshots\\" + "test_pic.png")
            self.logger.info("*************** page title failed ****************")
            assert False
            
    def test_header_links(self, setup):
        self.logger.info("*************** page title test ****************")
        driver = setup
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(5)
        self.headers = Header(driver)
        header_xpaths = self.headers.header_links_xpath(self.base_xpath)
        time.sleep(3)
        result = []
        for i in header_xpaths:    
            header = driver.find_element_by_xpath(i)
            href = header.get_attribute("href")
            text = header.get_attribute("text")
            try:
                header.click()
            except ElementNotInteractableException as e:
                self.logger.info("********* {} **********".format(e))
            else:
                current_url = driver.current_url
                time.sleep(3)
                driver.back()
                if current_url == href:
                    self.logger.info("************* {} header passed **************".format(text))
                    result.append("passed")
                else:
                    self.logger.info("************* {} header failed **************".format(text))
                    driver.save_screenshot(".\\screenshots\\" + "test_pic.png")
                    result.append("failed")
        # print(result)
        if "failed" not in result:
            assert True
        else:
            assert False
        driver.close()
