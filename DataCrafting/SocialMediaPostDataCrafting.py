from DataCrafting.AbstractDataCrafting import DataCrafting
from Models.Models import SocialMediaPost

class SocialMediaPostDataCrafting(DataCrafting):
    def craft_for_database(self, data):
        data_copy = {key: value for key, value in data.items() if key != 'type'}

        data_copy['user_name'] = "NA" if data_copy.get('user_name') is None else data_copy.get('user_name')
        data_copy['hashtags'] = "NA" if data_copy.get('hashtags') is None else "#"+"#".join(data_copy.get('hashtags'))
        data_copy['content'] = "NA" if data_copy.get('content') is None else data_copy.get('content')
        # Now, use the modified copy of the data to instantiate the CustomerReview model
        return SocialMediaPost(**data_copy)

    def craft_for_frontend(self, data):
        # Extract hashtags for easier display, etc.
        return {
            "type": "social_media_post",
            "user_name": "NA" if data["user_id"] is None else data["user_id"],
            "content": "NA" if data["content"] is None else data["content"],
            "hashtags": "NA" if data["hashtags"] is None else "#"+ "#".join(data["hashtags"])  # Assuming hashtags are comma-separated
        }