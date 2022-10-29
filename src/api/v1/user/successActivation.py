from ..base import BaseApi
from ....Service.activationService import ActivationService


class Api(BaseApi):
    def __init__(self, request) -> None:
        self.request = request
        super().__init__()
    
    def send(self):
        return ActivationService(self.request).service()
