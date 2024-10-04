import requests

API_KEY = ""


class FlightSearch:

    def __init__(self):
        self.api_key = API_KEY

    def write_iatocode(self, cities: list):
        for city in cities:

            params = {
                "term": city["city"],
                "location_types": "airport"
            }
            headers = {
                "apikey": self.api_key
            }

            response = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=params, headers=headers)

            data = response.json()
            print(data)
            iata_code = data["locations"][0]["city"]["code"]
            print(iata_code)

            to_send_json = {
                "price": {
                    "city": city["city"],
                    "iataCode": iata_code

                }
            }
            requests.put(url=f"https://api.sheety.co/df99721342f959a56afde7623ccb9fb6/flightDeals/prices/{city['id']}"
                         , json=to_send_json)

    def write_price(self, data_dict:dict):

        for city, price in data_dict.items():

            to_send_json = {
                "price": {
                    "city": city["city"],


                }
            }







