import requests
from datetime import date

class RESTAPIClient:
    def __init__(self,base_url):
        self._base_url= base_url
        
    def get_replay(self,serial):
        try :
        response = requests.get(f"{self._base_url}/api/responses?serial={serial}")
        response.raise_for_status()
        return response.json()
        except Exception as e:
        raise Exception(f"Error occurred while getting data for serial {serial}:{str(e)}")
        
      @staticmethod
        def get_data(response_1, response_2):
        try:
            data = {
                "serial": 3,
                "message": {
                    "subset": {
                        "general": {
                            "information": {
                                "date": date(2021,2,1),
                                "version": 3.00
                            },
                            "quantities": {
                                "first": max(response_1["message"]["subset"]["general"]["quantities"]["first"],
                                            response_2["message"]["subset"]["general"]["quantities"]["first"]),
                                "second": max(response_1["message"]["subset"]["general"]["quantities"]["second"],
                                             response_2["message"]["subset"]["general"]["quantities"]["second"]),
                                "third": max(response_1["message"]["subset"]["general"]["quantities"]["third"],
                                            response_2["message"]["subset"]["general"]["quantities"]["third"])
                            }
                        }
                    }
                }
            }
            return data
            except Exception as e:
            raise Exception(f"Error occurred while getting Json data for posting: {str(e)}")
        
        def send_request(self,data):
            Try:
            response = requests.post(f"{self._base_url}/api/process", json=data)
            response.raise_for_status()
            except Exception as e:
            raise Exception(f"Error occurred while posting data: {str(e)}")
