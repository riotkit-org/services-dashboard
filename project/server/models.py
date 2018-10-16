# project/server/models.py


class Service:
    domain = ''          # type: str
    ports = []           # type: list
    discovery_type = ''  # type: str
    attributes = {}      # type: dict

    def __init__(self, domain: str, ports: list, discovery_type: str, attributes: dict):
        self.domain = domain
        self.ports = ports
        self.discovery_type = discovery_type
        self.attributes = attributes

    def is_web_service(self) -> bool:
        return True

    def get_domain(self) -> str:
        return self.domain

    def is_enabled(self) -> bool:
        return self.get_boolean_attribute('enabled')

    def get_icon(self) -> str:
        return self.get_attribute_value('icon', 'pe-7s-global')

    def get_description(self) -> str:
        return self.get_attribute_value('description', '')

    def is_visible_only_for_admin(self) -> bool:
        return self.get_boolean_attribute('only_for_admin')

    def get_boolean_attribute(self, attribute_name: str, default=False) -> bool:
        attribute_name = attribute_name.upper()

        if attribute_name in self.attributes:
            value = self.attributes[attribute_name].lower()
            return value == 'true' or value == '1' or value == 'y' or value == 'yes'

        return default

    def get_attribute_value(self, attribute_name: str, default='pe-7s-global') -> str:
        attribute_name = attribute_name.upper()
        return self.attributes[attribute_name] if attribute_name in self.attributes else default

    def get_discovery_type(self) -> str:
        return self.discovery_type
