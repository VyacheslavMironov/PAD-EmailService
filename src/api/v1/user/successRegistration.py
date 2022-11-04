from ..base import BaseApi
from ....Service.registrationService import RegistrationService


class Api(BaseApi):
    def __init__(self, request) -> None:
        self.request = request
        super().__init__()
    
    def send(self):
        return RegistrationService(self.request).service()
