#A New prompt to structure an structured data can be added here with required fields and later stiched in OpenAIModelFactory
#TODO USE INTERFACE LIKE STRUCTURES TO FURTHER BREAK THESE AND CUSTOMIZE MORE
System_Role = "Act as a bot which structures unstructured data by understanding relating fields in the data."
Filter=" First find if its an email or social_media_post or customer_review."
Email_Prompt= " If it is an email the structure should have sender, recipient, subject, body."
SocialMedia_Post_Prompt=" If it is a social_media_post, the structure should have the user_name, content, hashtags."
CustomerReview_Prompt= " If it is a customer_review the structure should have customer_name, product_name, review_text, rating(in numbers 1 to 5)."
Format_Prompt= " Return in JSON format along with type."