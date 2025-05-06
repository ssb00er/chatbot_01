# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionPlaceOrder(Action):

    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        item = tracker.get_slot('item')
        
        dispatcher.utter_message(text=f"Your order for {item} has been placed.")
        return []



class ActionShowMenu(Action):

    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        menu = """
        Here is our menu:
        1. Margherita Pizza - $10
        2. Pepperoni Pizza - $12
        3. BBQ Chicken Pizza - $15
        4. Veggie Pizza - $11
        5. Cheeseburger - $8
        6. Bacon Burger - $9
        7. Veggie Burger - $7
        8. Caesar Salad - $7
        9. Greek Salad - $8
        10. Garden Salad - $6
        """
        
        dispatcher.utter_message(text=menu)
        return []
    

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry, I didn't understand that. Can you please rephrase?")
        return []



class ActionCancelOrder(Action):

    def name(self) -> Text:
        return "action_cancel_order"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your order has been canceled.")
        return [SlotSet("item", None)]