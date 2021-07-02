from django.apps import AppConfig
import requests
from django.http import HttpResponseNotFound

class QuerygiantbombConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'querygiantbomb'


class GiantBombApi:
    def __init__(self, api_key, user_agent="test"):
        self.api_key = api_key
        self.base_url = "https://giantbomb.com/api/"

        self.headers = {
            "accept": "application/json",
            "User-Agent": user_agent
        }

        self.default_parameters = {
            'api_key': self.api_key,
            'format': 'json',
            'limit': 5,
            'page': 1,
            'offset': 0,
            'field_list': "id,name,date_added,api_detail_url,number_of_user_reviews"
        }


    def perform_request(self, url_path, parameters={}):
        url = self.base_url + url_path

        url_parameters = self.default_parameters.copy()
        url_parameters.update(parameters)

        # request backend api to always return json
        url_parameters["format"] = "json"

        response = requests.get(url,
                                headers=self.headers,
                                params=url_parameters,
                                timeout=10)

        return response.json()

    def search(self, filters):
        url_path = 'search/'
        parameters = {
            'resources': 'game'
        }

        # apply filters to parameters
        parameters.update(filters)

        # apply fields from filters
        if len(filters.get("fields",[])) > 0:
            parameters["field_list"] = ",".join(field for field in filters["fields"].split(r", "))
            del (parameters["fields"])

        results = self.perform_request(url_path, parameters)

        return results