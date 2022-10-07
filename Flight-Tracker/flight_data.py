API_KEY = "XVjgjc41CXWtzvRzyR-JzMiH4zC0WUUi"
import datetime
import requests
import json


class FlightData:

    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.price = 0

        self.departure_city = "LON"

        self.data = {}

        self.headers = {

            "apikey": "XVjgjc41CXWtzvRzyR-JzMiH4zC0WUUi"

        }

    def search_for_price(self, cities_iata_code: list, cities_name: list):
        six_months = datetime.datetime.now() + datetime.timedelta(days=180)
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

        headers = {
            "apikey": API_KEY
        }

        city_price_dict = {}

        for iata_code in cities_iata_code:
            params = {

                "fly_from": "city:LON",
                "fly_to": f"city:{iata_code}",
                "date_from": tomorrow.strftime("%d/%m/%Y"),
                "date_to": six_months.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "curr": "GBP"
            }
            respond = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=params, headers=headers)

            self.data = respond.json()

            self.price = self.data["data"][0]["price"]


            city_price_dict[iata_code] = f"{self.price}£"

        print(city_price_dict)