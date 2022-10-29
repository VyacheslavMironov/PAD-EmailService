from ..base import BaseApi
from ....Service.createOrganizationService import CreateOrganizationService


class Api(BaseApi):
    def __init__(self, request) -> None:
        self.request = request
        super().__init__()
    
    def send(self):
        return CreateOrganizationService(self.request).service()
