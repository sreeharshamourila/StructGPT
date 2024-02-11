from DataCrafting.EmailDataCrafting import EmailDataCrafting
from DataCrafting.SocialMediaPostDataCrafting import  SocialMediaPostDataCrafting
from DataCrafting.CustomerReviewDataCrafting import  CustomerReviewDataCrafting

# Factory for deciding which class to use
class DataCraftingFactory:
    @staticmethod
    def get_crafter(data_type):
        if data_type == 'email':
            return EmailDataCrafting()
        elif data_type == 'social_media_post':
            return SocialMediaPostDataCrafting()
        elif data_type == 'customer_review':
            return CustomerReviewDataCrafting()
        else:
            return {"type": "It is neigther a email, nor a social media port nor a customer review"}