from abc import ABCMeta, abstractmethod, abstractproperty

class ILoader():
    __metaclass_ = ABCMeta
    @abstractmethod
    def Load(self, data):
        raise NotImplementedError

