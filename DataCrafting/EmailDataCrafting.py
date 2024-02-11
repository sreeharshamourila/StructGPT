from DataCrafting.AbstractDataCrafting import DataCrafting
from Models.Models import Email

class EmailDataCrafting(DataCrafting):
    def craft_for_database(self, data):
        data_copy = {key: value for key, value in data.items() if key != 'type'}
        data_copy['sender'] = "NA" if data_copy.get("sender") is None else data_copy.get("sender")
        data_copy['recipient'] = "NA" if data_copy.get("recipient") is None else data_copy.get("recipient")
        data_copy["subject"] = "NA" if data_copy.get("subject") is None else data_copy.get("subject")
        data_copy["body"] = "NA" if data_copy.get("body") is None else data_copy.get("body")
        return Email(**data_copy)

    def craft_for_frontend(self, data):
        # Simplify or modify the data structure for frontend needs
        return {
            "type" : "email",
            "sender": "NA" if data["sender"] is None else data["sender"],
            "recipient": "NA" if data["recipient"] is None else data["recipient"],
            "subject": "NA" if data["subject"] is None else data["subject"],
            "body": "NA" if data["body"] is None else data["body"]
        }
