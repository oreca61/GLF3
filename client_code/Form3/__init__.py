from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Form2 import Form2


class Form3(Form3Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    self.kurse_laden()

  def kurse_laden(self):
    daten = anvil.server.call('hole_verfuegbare_mitglieder',self.item.kurs_id)
    
    
    print(daten)
