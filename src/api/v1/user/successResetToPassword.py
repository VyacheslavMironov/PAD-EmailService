from ..base import BaseApi
from ....Service.resetToPasswordService import ResetToPasswordService


class Api(BaseApi):
    def __init__(self, request) -> None:
        self.request = request
        super().__init__()
    
    def send(self):
        return ResetToPasswordService(self.request).service()
