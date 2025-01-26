import configparser
import os
from configparser import ConfigParser, NoSectionError

#config = configparser.RawConfigParser()
#config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
#config.read(config_path)
#config.read(".\\Configuration\\config.ini")
#config.read(".\\config.ini")

class readconfig():
    @staticmethod
    def getappurl():
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Construct the absolute path to config.ini
        config_path = os.path.abspath(os.path.join(current_directory, '..', 'Configuration', 'config.ini'))

        # Debug: Print the resolved path
        print(f"Resolved config path: {config_path}")

        # Verify the file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Read the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve the URL
        try:
            url = config.get('common data', 'webtoolsUrl')
            return url
        except configparser.NoSectionError:
            raise Exception("The 'common data' section is missing in the configuration file.")
        except configparser.NoOptionError:
            raise Exception("The 'webtoolsUrl' option is missing in the 'common data' section.")

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
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Construct the absolute path to config.ini
        config_path = os.path.abspath(os.path.join(current_directory, '..', 'Configuration', 'config.ini'))

        # Debug: Print the resolved path
        print(f"Resolved config path: {config_path}")

        # Verify the file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Read the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve the URL
        try:
            username = config.get('common data', 'username')
            return username
        except configparser.NoSectionError:
            raise Exception("The 'common data' section is missing in the configuration file.")
        except configparser.NoOptionError:
            raise Exception("The 'webtoolsUrl' option is missing in the 'common data' section.")

    @staticmethod
    def get_password():
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Construct the absolute path to config.ini
        config_path = os.path.abspath(os.path.join(current_directory, '..', 'Configuration', 'config.ini'))

        # Debug: Print the resolved path
        print(f"Resolved config path: {config_path}")

        # Verify the file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Read the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve the URL
        try:
            password = config.get('common data', 'password')
            return password
        except configparser.NoSectionError:
            raise Exception("The 'common data' section is missing in the configuration file.")
        except configparser.NoOptionError:
            raise Exception("The 'webtoolsUrl' option is missing in the 'common data' section.")

        #password = config.get('common data', 'password')
        #return password

    @staticmethod
    def get_webtoolsusername():
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Construct the absolute path to config.ini
        config_path = os.path.abspath(os.path.join(current_directory, '..', 'Configuration', 'config.ini'))

        # Debug: Print the resolved path
        print(f"Resolved config path: {config_path}")

        # Verify the file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Read the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve the URL
        try:
            username = config.get('common data', 'Webtools_username')
            return username
        except configparser.NoSectionError:
            raise Exception("The 'common data' section is missing in the configuration file.")
        except configparser.NoOptionError:
            raise Exception("The 'webtoolsUrl' option is missing in the 'common data' section.")

        #username = config.get('common data', 'Webtools_username')
        #return username

    @staticmethod
    def get_webtoolspassword():
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Construct the absolute path to config.ini
        config_path = os.path.abspath(os.path.join(current_directory, '..', 'Configuration', 'config.ini'))

        # Debug: Print the resolved path
        print(f"Resolved config path: {config_path}")

        # Verify the file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Read the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve the URL
        try:
            password = config.get('common data', 'Webtools_password')
            return password
        except configparser.NoSectionError:
            raise Exception("The 'common data' section is missing in the configuration file.")
        except configparser.NoOptionError:
            raise Exception("The 'webtoolsUrl' option is missing in the 'common data' section.")

        #password = config.get('common data', 'Webtools_password')
        #return password

