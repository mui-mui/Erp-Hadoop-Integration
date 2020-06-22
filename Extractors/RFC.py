from Extractors.IExtractor import IExtractor
from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError
from datetime import datetime
from pathlib import Path
import os

class SapExtractor(IExtractor):
    """
    :param options:
    {fm:function module name, {args}}
    :return:
    (dictionary[]) function call result
    """
    def __init__(self, connection_config, extract_options):
        self.extractor_context = SapRfcLib.Initialization(connection_config)
        self.conn_conf = connection_config
        self.extract_options = extract_options
    def Extract(self):
        try:
            return self.extractor_context.call(self.extract_options['fm'], **self.extract_options['args'])
        except CommunicationError:
            print("%s Error - Could not connect to ERP server", (datetime.now()))
            raise
        except LogonError:
            print("%s Error - Could not log in %s. Wrong credentials?", (datetime.now()))
            raise
        except (ABAPApplicationError, ABAPRuntimeError):
            print("%s Error - ABAP error %s", (datetime.now()))
            raise

class SapRfcLib():
    @staticmethod
    def Initialization(conn_options):
        return Connection(**conn_options)