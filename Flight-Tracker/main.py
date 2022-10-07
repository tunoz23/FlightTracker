# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
FlightData = FlightData()
FlightSearch = FlightSearch()
GoogleSheetData = DataManager()


#FlightSearch.write_iatocode(GoogleSheetData.dont_have_iata_code_list)
#FlightData.search(cities=
print(GoogleSheetData.sheety_data)
