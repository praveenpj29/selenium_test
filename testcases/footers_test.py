from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.footer import Footer
from utilities.customLogger import LogGen
from utilities.siteConfig import siteconfig
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd
import time

class Test_1:
    base_url = siteconfig.getsiteURl()
    base_xpath = siteconfig.getfooterXPATH()
    logger = LogGen.loggen()

    def test_footer_links(self, setup):
        self.logger.info("*************** footer links test started **************")
        driver = setup
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(3)
        footers = Footer(driver)
        footer_xpath = footers.footer_links_xpath(self.base_xpath)
        time.sleep(3)
        df = {
            "S.no": [],
            "Link_name": [],
            "XPATH": [],
            "URL": [],
            "Directed URL": [],
            "Validation": []
        }
        result = []
        for n, i in enumerate(footer_xpath):
            footer = driver.find_element_by_xpath(i)
            footer.location_once_scrolled_into_view
            href = footer.get_attribute("href")
            text = footer.get_attribute("text")
            try:
                footer.click()
            except ElementNotInteractableException as e:
                self.logger.info("**************** {} ************".format(e))
                self.logger.info("************  {} footer failed *********".format(text))
                df["Validation"].append("failed")
                result.append("failed")
            else:
                current_url = driver.current_url
                time.sleep(1)
                driver.back()
                df["Validation"].append("passed")
                self.logger.info("************ {} footer passed *********".format(text))
                result.append("passed")
            finally:
                df["S.no"].append(n + 1)
                df["Link_name"].append(text)
                df["URL"].append(href)
                df["Directed URL"].append(current_url)
                df["XPATH"].append(i)
        
        Data = pd.DataFrame(df, index=df["S.no"])
        output = pd.ExcelWriter(".//reports/footers_links_validation.xlsx")
        Data.to_excel(output)
        output.save()

        if "failed" not in result:
            assert True
        else:
            assert False
            
        driver.close()
