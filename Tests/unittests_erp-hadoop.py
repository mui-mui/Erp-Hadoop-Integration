import unittest
from Extractors.RFC import SapExtractor
from Loaders.Hadoop import HadoopLoader
from Integration.Integration import DataIntegration
from configs.Configs import Configuration



class TestSapExtractor(unittest.TestCase):
    """
    Testing SAP RFC Connector
    """
    def setUp(self):
        extract_options = {"fm": "ZFM_GET_2LIS_17_I3HDR", "args": {}}  # {Function module name, {FM arguments}}
        self.extractor = SapExtractor(Configuration.GetConfig("sapnwrfc.cfg", "connection"), extract_options)
    def testExtract(self):
        """
        Testing Extract method
        """
        data = self.extractor.Extract()

        # Verify the returned answer is of type dictionary
        self.assertIsInstance(data, dict, "Should be type dict")

        # Verify that the returned dictionary has the key 'E_TABLE'
        self.assertTrue(data.get("E_TABLE"), False)


class TestHadoopLoader(unittest.TestCase):
    """
    Testing Hadoop connectors
    """
    def setUp(self):
        self.shortDescription()
        self.load_options = {"projection": {"E_TABLE": "dwh_dm.zfm_get_2lis_17_i3hdr_parquet"}, "format": "parquet",
                        "compress": "gzip"}
        extractor = HadoopLoader(Configuration.GetConfig("impala.cfg","connection"), self.load_options)
        self.loader_Ctx=extractor.loader_context # get impala loader context
        self.conn_config = extractor.conn_config # connection string
    def testLoad(self):
        self.shortDescription()
        """
        Testing load method
        :return:
        """
        # Checking that connecting to the database does not raise an exception
        try:
            self.loader_Ctx.read.jdbc(url=self.conn_config["url"],
                                 table=self.load_options["projection"]["E_TABLE"],
                                 properties={"user": self.conn_config["user"], "password": self.conn_config["password"]})  # запись данных в соответствующую таблицу бд hadoop
        except:
            raise BaseException("Should be without exception")


if __name__ == '__main__':
    unittest.main()