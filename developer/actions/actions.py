# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

tarea = "task 1"

class action_estado_tarea_actual(Action):

     def name(self) -> Text:
         return "action_estado_tarea_actual"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
         dispatcher.utter_message(response = "utter_no_termine_tarea", tarea_actual = tarea)
#         dispatcher.utter_message(response = "utter_tarea_terminada", tarea_actual = tarea)

         return []
