from ._anvil_designer import FormWeatherTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http as rq

class FormWeather(FormWeatherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.weather_url = 'https://wttr.in/'

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    print(f'Received new location : {self.text_box_1.text}')
    weather_request =  self.weather_url + self.text_box_1.text
    weather_response = rq.request(weather_request)
    self.text_weather_info.text = weather_response.

  def text_box_1_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    pass


