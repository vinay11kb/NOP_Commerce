#read data from ini file
import  configparser

config=configparser.RawConfigParser()
config.read(r'D:\selenium_python\NOP_Commerce\Configurations\config.ini') #read ini file

class readConfig:
    #for every varaible create 1 method

    @staticmethod  #we directly access it using class name witout creating object
    def getUrl():
        url=config.get('common info','base_url') #(category,variable)
        return url

    @staticmethod
    def getEmail():
        username=config.get("common info","username")
        return username

    @staticmethod
    def getPassword():
        password=config.get("common info","password")
        return password