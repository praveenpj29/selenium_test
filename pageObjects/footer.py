class Footer:

    def __init__(self, driver):
        self.driver = driver
    
    def footer_links_xpath(self, base_xpath):
        footer_links = len(self.driver.find_elements_by_xpath(base_xpath))
        footer_links_xpath = []
        for i in range(footer_links):
            footer_links_xpath.append(base_xpath + "//preceding::a[1]//following::a[{}]".format(i + 1))
        return footer_links_xpath