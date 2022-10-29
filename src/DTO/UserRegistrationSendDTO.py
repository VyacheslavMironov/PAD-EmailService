class UserRegistrationSendDTO:
    def __init__(self,  first_name: str, email: str, password: str, template: str|None) -> None:
        self.first_name = first_name
        self.email = email
        self.password = password
        self.template = template
