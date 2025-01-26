import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        current_directory = os.path.dirname(__file__)
        log_file = os.path.join(current_directory, 'automation.log')
        logger = logging.getLogger()
        fhandler = logging.FileHandler(log_file, mode='a')
        #fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
