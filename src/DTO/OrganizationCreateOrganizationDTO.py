class OrganizationCreateOrganizationDTO:
    def __init__(self,  first_name: str, email: str, template: str|None) -> None:
        self.first_name = first_name
        self.email = email
        self.template = template
    