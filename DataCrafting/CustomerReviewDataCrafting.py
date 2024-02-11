from DataCrafting.AbstractDataCrafting import DataCrafting
from Models.Models import CustomerReview


class CustomerReviewDataCrafting(DataCrafting):
    def craft_for_database(self, data):
        data_copy = {key: value for key, value in data.items() if key != 'type'}

        # Convert the necessary fields to their appropriate types
        # Note: It's a good practice to validate or try-except these conversions for real applications
        data_copy['customer_name'] =   "NA" if data_copy.get("customer_name") is None else data_copy.get("customer_name")
        data_copy['product_name'] =  "NA" if data_copy.get("product_name") is None else data_copy.get("product_name")
        data_copy['rating'] =  0 if data_copy.get("rating") is None else int(data_copy.get("rating"))

        return CustomerReview(**data_copy)


    def craft_for_frontend(self, data):
        # Adjust the review structure for frontend display
        return {
            "type": "customer_review",
            "customer_name": "NA" if data["customer_name"] is None else data["customer_name"],
            "product_name": "NA" if data["product_name"] is None else data["product_name"],
            "review_text": data["review_text"],
            "rating": "NA" if data["rating"] is None else data["rating"]
        }