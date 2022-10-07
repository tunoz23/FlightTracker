import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url="https://api.sheety.co/71ba21d596e1855dea60314212e21d9b/flightDeals/prices")
        self.response.raise_for_status()
        self.sheety_data = self.response.json()["prices"]
        self.dont_have_iata_code_list = [row for row in self.sheety_data if row["iataCode"] == ""]

        self.city_names = [city["city"] for city in self.sheety_data]

        self.city_names_dont_iata = [city["city"] for city in self.dont_have_iata_code_list]

    def list_of_city_names(self):
        return self.city_names_dont_iata



