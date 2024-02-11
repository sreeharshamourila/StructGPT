from OpenAIClientInterface.OpenAIClient import OpenAIClientSingleton
from OpenAIClientInterface.MainPromptConfig import System_Role,SocialMedia_Post_Prompt,CustomerReview_Prompt,Format_Prompt, Filter, Email_Prompt

class ModelFactory:
    @staticmethod
    def create_model(model_name, **kwargs):
        # Assuming 'client' is the singleton instance of your OpenAI client
        client = OpenAIClientSingleton.get_instance()
        if model_name == "gpt-3.5-turbo":
            # Additional configuration or preprocessing can go here
            return client.chat.completions.create(model=model_name, **kwargs)
        # Add other models here as elif statements
        else:
            raise ValueError("Unsupported model name")

    @staticmethod
    def generate_messages(text_input):
        # Example of a simple structure, can be expanded to handle different types
        system_prompt = System_Role+ Filter + Email_Prompt +SocialMedia_Post_Prompt + CustomerReview_Prompt +Format_Prompt
        user_message = {'role': 'user', 'content': text_input}
        system_message = {'role': 'system', 'content': system_prompt}
        return [system_message, user_message]