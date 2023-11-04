import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

import requests

@anvil.server.callable
def get_tasks_by_priority(priority):
    BASE_URL = 'http://your-django-backend-url/api/backlog-items/'
    
    response = requests.get(BASE_URL, params={'priority': priority})

    # Ensure the request was successful and return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from the backend.")
