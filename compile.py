from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("Loaders.Hadoop", ["Loaders/Hadoop.py"]),
    Extension("Loaders.ILoader", ["Loaders/ILoader.py"]),
    Extension("Extractors.RFC", ["Extractors/RFC.py"]),
    Extension("Extractors.IExtractor", ["Extractors/IExtractor.py"]),
    Extension("Integration.Integration", ["Integration/Integration.py"]),
    Extension("Tools.Tools", ["Tools/Tools.py"]),
    Extension("configs.Configs", ["configs/Configs.py"]),
    ]

setup(
    name = 'ErpHadoopIntegration',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)