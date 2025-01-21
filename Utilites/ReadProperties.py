import configparser
from configparser import ConfigParser, NoSectionError

config = configparser.RawConfigParser()

config.read(".\\Configuration\\config.ini")

class readconfig():
    @staticmethod
    def getappurl():
        url = config.get('common data', 'baseurl')
        return url

    '''
    def getappurl():
        config = ConfigParser()
        #config.read('.\\Configuration\\config.ini')
        try:
            return config.get('common data', 'baseurl')
        except NoSectionError:
            print("Error: 'common data' section is missing in the configuration file.")
            return None
    '''

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password


