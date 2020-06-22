from Extractors.RFC import SapExtractor
from Loaders.Hadoop import HadoopLoader
from Integration.Integration import DataIntegration
from configs.Configs import Configuration

#
# Options to extract data from sap erp
#

# {Function module name, {FM arguments}}
extract_options = {"fm": "*******",
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
                        "E_TABLE": "**********"
                    },
                "format": "parquet",
                "compress": "gzip"}

#
# Create extractor and loader for Data Integration
#

# create sap rfc extractor
extractor_rfc = SapExtractor(Configuration.GetConfig("sapnwrfc.cfg", "connection"), extract_options)
# create impala loader
loader_hadoop = HadoopLoader(Configuration.GetConfig("impala.cfg","connection"), load_options)

#
# Write data
#

# Create integration
data_integration = DataIntegration(extractor_rfc,loader_hadoop)
# Write data to impala
data_integration.Write()


