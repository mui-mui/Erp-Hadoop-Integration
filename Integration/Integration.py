class DataIntegration():
    def __init__(self, IExtractor, ILoader):
        self.extractor = IExtractor
        self.loader = ILoader
    def Read(self):
        return self.extractor.Extract()
    def Write(self):
        data = self.Read()
        self.loader.Load(data)