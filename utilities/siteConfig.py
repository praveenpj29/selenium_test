import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class siteconfig:
    @staticmethod
    def getsiteURl():
        url = config.get('amazon info', 'baseURL')
        return url
    
    @staticmethod
    def getheaderXPATH():
        xpath = config.get('amazon info', 'header_xpath')
        return xpath