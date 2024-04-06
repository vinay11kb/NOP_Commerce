import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"D:\selenium_python\NOP_Commerce\Logsautomation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %P')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
