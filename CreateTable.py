from Extractors.RFC import SapExtractor
from Loaders.Hadoop import HadoopLoader
from Integration.Integration import DataIntegration
from configs.Configs import Configuration
from pyspark import SparkContext, SparkConf
from decimal import Decimal
from pyspark.sql import HiveContext, SQLContext, functions
from pyspark.sql.types import Row

#
# Options to extract data from sap erp
#

# {Function module name, {FM arguments}}
extract_options = {"fm": "********",
                   "args":
                       {

                       }
                   }

#
# Options to load data from Impala db
#

#{"projection": {[erp_table]: [impala_table]}}
load_options = {"projection":
                    {
                        "E_TABLE": "***********"
                    },
                "format": "parquet",
                "compress": "gzip"}


extractor_rfc = SapExtractor(Configuration.GetConfig("sapnwrfc.cfg", "connection"), extract_options)
data = extractor_rfc.Extract()

sc = SparkContext()
sc.setLogLevel("ERROR")
sqlCtx = SQLContext(sc)

for tablename_erp in load_options['projection'].keys():
    df = sqlCtx.createDataFrame(Row(**x) for x in data[tablename_erp][0])  # creating a dataframe
    df_empty = sqlCtx.createDataFrame([], schema=df.schema)
    df_empty.write.format(load_options["format"]).option("compression", load_options["compress"])\
        .saveAsTable(
            name=load_options['projection'][tablename_erp],
            mode="append")







