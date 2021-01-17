## openAPI libarary imports
from lib.fuel_status.client import *
## general imports
import yaml
import asyncio
import pprint
import argparse
import os

pp = pprint.PrettyPrinter(indent=2)
parser = argparse.ArgumentParser("Mercedes API Client")

if (__name__ == '__main__'):

    client = FuelStatusApiClient()
    config = parse_config_file()

    ## start data retrieval
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # oauth2 auth
    provider = loop.run_until_complete(client.provide_o_auth2_authorization(scopes=config["scopes"],
                                                                            redirect_uri=config["redirect_uri"],
                                                                            client_id=config["client_id"],
                                                                            client_secret=config["client_secret"]))

    # get results for fuel status container
    result = loop.run_until_complete(client.get_resources_for_container_id_using_ge_t(vehicle_id=config["vin"], access_token=provider.manager._access_token))
    pp.pprint(result)


def parse_config_file():
    ### Parse config file path
    parser.add_argument('--config', default='default.yaml')
    args = parser.parse_args()
    config_file_path = os.path.join(os.getcwd(), 'configs', args.config)

    print(config_file_path)

    if not os.path.isfile(config_file_path):
        raise ValueError("Config file path does not exist.")

    ### Read config file
    with open(config_file_path, 'r') as stream:
        try:
            yaml_config = yaml.safe_load(stream)
            return yaml_config

        except yaml.YAMLError as exc:
            print("Config file cannot be opened. Please check syntax!")
            print(exc)