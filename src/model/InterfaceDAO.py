from abc import ABCMeta, abstractmethod

class InterfaceDAO:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        raise NotImplementedError

    @abstractmethod
    def insert(self, object):
        raise NotImplementedError

    @abstractmethod
    def update(self, object):
        raise NotImplementedError

    @abstractmethod
    def readAll(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self, object):
        raise NotImplementedError

    @abstractmethod
    def deleteAll(self):
        raise NotImplementedError

    @abstractmethod
    def find(self, object):
        raise NotImplementedError

    @abstractmethod
    def set_up_ddbb(self):
        raise NotImplementedError
