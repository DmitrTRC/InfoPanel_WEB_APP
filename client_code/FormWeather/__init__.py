import anvil.google.auth, anvil.google.drive
import anvil.tables as tables
import anvil.tables.query as q
import anvil.users

from ._anvil_designer import FormWeatherTemplate
from anvil import *
import anvil.server
from anvil.google.drive import app_files
from anvil.tables import app_tables

from utils import report



class FormWeather(FormWeatherTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        

        # Any code you write here will run before the form opens.

  

    def text_box_1_pressed_enter(self, **event_args):
        info_json = anvil.server.call('get_weather', self.text_box_1.text)
        print(f'Raw response: {info_json}')

        self.rich_text_weather.content = report.format_weather_report(info_json)
