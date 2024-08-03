import requests

sheety_endpt="endpt"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpt=sheety_endpt
        self.destination_data={}

    def get_destination_data(self):
        response = requests.get(self.endpt)
        print(response.status_code)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.endpt}/{city['id']}",
                json=new_data
            )
            print(response.text)


