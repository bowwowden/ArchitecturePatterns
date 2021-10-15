import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, item):
        pass

    @abc.abstractmethod
    def read(self, item):
        pass

    @abc.abstractmethod
    def update(self, item):
        pass

    @abc.abstractmethod
    def destroy(self, item):
        pass