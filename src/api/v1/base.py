from abc import ABC, abstractclassmethod


class BaseApi(ABC):

    @abstractclassmethod
    def send(self):
        pass
