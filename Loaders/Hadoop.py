from Loaders.ILoader import ILoader
from configs.Configs import Configuration
from decimal import Decimal
from Tools.Tools import Tools

class HadoopLoader(ILoader):
    """
            :param: extract_options
            dictionary projection { name_hadoop_table: name_sap_table } - соответвие извлекаемых таблиц erp таблицам hadoop
            string format_hadoop_table - формат таблицы в hadoop
            string compress_hadoop_table - тип сжатия таблицы в hadoop

    """
    def __init__(self, connection_config, extract_options):
        self.loader_context = PySparkLib.Initialization()
        self.conn_config = connection_config # данные для подключения к бд
        self.extract_options = extract_options
    def Load(self, data):
        from pyspark.sql.types import Row
        if not isinstance(data, dict):
            print("Error - the data object must be a dictionary")
            return
        table_projection = self.extract_options["projection"]
        table_format = self.extract_options["format"]
        table_compress = self.extract_options["compress"]

        for tablename_erp in table_projection.keys():
            df = self.loader_context.createDataFrame(Row(**x) for x in data[tablename_erp])  # creating a dataframe
            try:
                # write dataframe to impala db relevant table
                df.write.format(table_format).option("compression", table_compress).mode("append").jdbc(url=self.conn_config["url"],
                                                                                                        table=table_projection[tablename_erp],
                                                                                                        properties={"user": self.conn_config["user"], "password": self.conn_config["password"]})

            except Exception as e:
                if (e.__str__().find("CREATE TABLE") != -1):
                    raise Exception("ERROR: Table '%s' does not exist. Before recording, please create a table %s" % (
                    table_projection[tablename_erp], table_projection[tablename_erp]))
                raise

class PySparkLib:
    @staticmethod
    def Initialization():
        """
        pyspark library init
        :return: SQLContext object
        """
        from pyspark import SparkContext
        from pyspark.sql import SQLContext
        sc = SparkContext()
        return SQLContext(sc)

if __name__ == '__main__':
    print(PySparkLib.__doc__)
    print(HadoopLoader.__doc__)