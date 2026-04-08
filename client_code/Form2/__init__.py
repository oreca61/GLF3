from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):

    data = anvil.server.call('hol_alle_kurs_daten')
    
    print(data)
    self.repeating_panel_kurs.items = data

