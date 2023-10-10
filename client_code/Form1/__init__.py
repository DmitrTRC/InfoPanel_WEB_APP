from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from ..FormWeather import FormWeather

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()


  def link_weather_click(self, **event_args):
    """This method is called when the link is clicked"""
    weather_panel = FormWeather()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(weather_panel)
    
    

