from ._anvil_designer import FormMainTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from ..FormWeather import FormWeather
from ..FormTasks import FormTasks


class FormMain(FormMainTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def link_weather_click(self, **event_args):
        """This method is called when the link is clicked"""
        weather_panel = FormWeather()
        get_open_form().content_panel.clear()
        get_open_form().content_panel.add_component(weather_panel)

    def link_tasks_click(self, **event_args):
      task_panel = FormTasks()
      get_open_form().content_panel.clear()
      get_open_form().content_panel.add_component(task_panel)

    
