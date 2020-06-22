from abc import ABCMeta, abstractmethod, abstractproperty

class IExtractor():
    __metaclass_ = ABCMeta
    @abstractmethod
    def Extract(self, *args, **kwargs):
        raise NotImplementedError

