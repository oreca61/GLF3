import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

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

@anvil.server.callable
def hol_alle_kurs_daten():
  with sqlite3.connect(data_files["ALTUNTAS_Muhammet_fitnessstudio.db"]) as conn:
    
    conn.row_factory = sqlite3.Row

    
    cursor = conn.cursor()

    query = """
    SELECT
    k.kurs_id,
    
    k.bezeichnung AS kurs,
    
    k.wochentag, 
    k.uhrzeit, 
    t.vorname || ' ' || t.nachname AS trainer,
    
    COUNT(a.anmelde_id) AS aktuelle_teilnehmer,
    k.max_teilnehmer
    
FROM kurse as k

 JOIN trainer t  ON k.trainer_id = t.trainer_id
LEFT JOIN anmeldung a ON k.kurs_id = a.kurs_id
 
GROUP BY k.kurs_id
 ORDER  BY  k.wochentag, k.uhrzeit"""

    cursor.execute(query)

    rows = cursor.fetchall()

    
    return [dict(row) for row in rows]


def hole_verfuegbare_mitglieder(kurs_id):
  with sqlite3.connect(data_files["Fittnes.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """
        SELECT
            m.mitglied_id,
             m.vorname,
             m.nachname
         FROM  mitglied  m
        
        WHERE m.mitglied_id NOT IN (
            SELECT a.mitglied_id
              FROM anmeldung a
            WHERE a.kurs_id = ?
            
        )
        ORDER BY m.nachname, 
        m.vorname
        
        """

    cursor.execute(query, (kurs_id,))
    
    rows = cursor.fetchall()

    
    return [dict(row) for row in rows]