

class MetadataParser:
    @staticmethod
    def parse(env: list, labels: dict) -> tuple:
        ports = []
        domains = list()
        attributes = dict()

        meta = {**labels, **MetadataParser._env_to_dict(env)}

        for key, value in meta.items():
            if 'traefik' in key and 'frontend.rule' in key:
                domains.append(value)
                continue

            elif key == 'traefik.port':
                ports.append(value)
                continue

            elif key == 'VIRTUAL_HOST' or key == 'LETSENCRYPT_HOST':
                domains.append(value)
                continue

            elif key == 'VIRTUAL_PORT':
                ports.append(value)
                continue

            elif key[0:4] == 'DSD_':
                attributes[key[4:].upper()] = value
                continue

            elif key[0:30] == 'org.docker.services.dashboard.':
                attributes[key[30:].upper()] = value
                continue

        # support domain registration via labels
        for attribute, value in attributes.items():
            if attribute == 'DOMAIN':
                domains.append(value)

        if len(domains) > 0 and len(ports) == 0:
            ports.append(80)

        return set(domains), set(ports), attributes

    @staticmethod
    def _env_to_dict(env: list) -> dict:
        env_as_dict = dict()

        for raw_env in env:
            key, value = MetadataParser._parse_raw_env(raw_env)
            env_as_dict[key] = value

        return env_as_dict

    @staticmethod
    def _parse_raw_env(env_string: str) -> tuple:
        pos = env_string.find('=')

        if '=' not in env_string:
            raise Exception('Invalid ENV string "' + env_string + '"')

        key = env_string[0:pos]
        value = env_string[(pos + 1):]

        return key, value
