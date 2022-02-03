# weather.py

import argparse
from configparser import ConfigParser

def read_user_cli_args():
    """Handles the cli user interaction
    
    Returns
        argparse.namespace: populated namespace object
        
    """

    parser = argparse.ArgumentParser(
        description="gets weather and temp information for a city"
    )
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()

# ...

if __name__ == "__main__":
    user_args = read_user_cli_args()
    print(user_args.city, user_args.imperial)

def _get_api_key():
    """ Fetch api key from config file.
    
    Expects a config file named secrets.ini with structure 
    
        [openweather]
        api_key=<my-openweather-api-key>
        """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

