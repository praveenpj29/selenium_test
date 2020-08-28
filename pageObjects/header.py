class Header:
    # base_xpath = "//*[@id='nav-xshop/a']"

    def __init__(self, driver):
        self.driver = driver

    def header_links_xpath(self, base_xpath):
        header_links = len(self.driver.find_elements_by_xpath(base_xpath))
        header_links_xpath = [] 
        for i in range(header_links):
            header_links_xpath.append(base_xpath + "[{}]".format(i + 1))
        return header_links_xpath
