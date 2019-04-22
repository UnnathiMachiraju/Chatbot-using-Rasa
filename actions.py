from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import json

class ActionCity(Action):
	def name(self):
		return 'action_city'
		
	def run(self, dispatcher, tracker, domain):
            cityjson = json.load(open("data/cities.json","r"))
            loc = tracker.get_slot('city')
            flag=0
            for key,value in cityjson.items():
                if loc in value:
                    response ="""This city is in {}""".format(key)
                    flag=1
            dispatcher.utter_message(response)
            return [SlotSet('city',loc)]
