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
             
         dispatcher.utter_message(response = "utter_tarea_no_terminada", tarea_actual = tarea)
#         dispatcher.utter_message(response = "utter_tarea_terminada", tarea_actual = tarea)

         return []

class action_nueva_tarea(Action):

     def name(self) -> Text:
         return "action_nueva_tarea"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
         dispatcher.utter_message(text="la tarea 1")

         return []

class action_confirmar_asistencia(Action):

     def name(self) -> Text:
         return "action_confirmar_asistencia"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hora = tracker.get_slot("horario")
        dispatcher.utter_message(text="la tarea 1")

        return []

class action_confirmar_asistencia(Action):

     def name(self) -> Text:
         return "action_inconveniente"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="no se manejar bd")

        return []