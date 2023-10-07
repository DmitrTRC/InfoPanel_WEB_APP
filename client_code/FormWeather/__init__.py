import anvil.google.auth, anvil.google.drive
import anvil.http as rq
import anvil.tables as tables
import anvil.tables.query as q
import anvil.users

from ._anvil_designer import FormWeatherTemplate
from anvil import *
from anvil.google.drive import app_files
from anvil.tables import app_tables

from utils import report


class FormWeather(FormWeatherTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self._weather_url = 'https://wttr.in/'
        self._weather_format = '?format=j1'  # 2AF

        # Any code you write here will run before the form opens.

    def get_weather(self):
        weather_request = self._weather_url + self.text_box_1.text + self._weather_format
        weather_response = rq.request(weather_request, json=True)
        return weather_response

    def text_box_1_pressed_enter(self, **event_args):
        info_json = self.get_weather()
        print(f'Raw response: {info_json}')

        self.rich_text_weather.content = report.format_weather_report(info_json)
