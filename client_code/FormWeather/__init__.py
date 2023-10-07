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
    self._weather_url = 'https://wttr.in/'
    self._weather_format = '?format=j1' #2AF

    # Any code you write here will run before the form opens.

  def get_weather(self):     
    weather_request =  self._weather_url + self.text_box_1.text + self._weather_format
    weather_response = rq.request(weather_request)
    return weather_response.get_bytes()

  def text_box_1_pressed_enter(self, **event_args):
    info = self.get_weather().decode()
    print (f'Raw response: {info}')
    report = ''
    for item in info:
      report += ( item + '\n' )
      
    self.rich_text_weather.content = report
    


  

