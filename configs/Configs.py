import configparser
import os.path

class Configuration():
    @staticmethod
    def GetConfig(filename, section_name):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), filename))
        return dict(config.items(section_name))