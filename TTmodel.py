# dynamic_tt_translation_textblob.py

# Import necessary libraries
# from textblob import TextBlob
# from textblob.exceptions import NotTranslated

# # Function to perform text-to-text translation using TextBlob
# def translate_text(text: str, target_lang: str):
#     blob = TextBlob(text)
    
#     # Perform translation to the target language
#     try:
#         translated_text = str(blob.translate(to=target_lang))
#         return str(translated_text)
#     except NotTranslated:
#         return "The text was not translated."
#     except Exception as e:
#         return f"Error during translation: {str(e)}"


from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str) -> str:
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated_text = translator.translate(text)
        return f"Translated text to {target_lang}: {translated_text}"
    except Exception as e:
        return f"Error during translation: {str(e)}"




# user input
# Example usage
# if __name__ == "__main__":
#     # User input for text and target language
#     input_text = input("Enter the text to translate: ")
#     target_lang = input("Enter the target language code (e.g., 'fr' for French): ")

#     # Perform translation
#     translated_text = translate_text(input_text, target_lang)
    
#     # Print the translated text
#     print(f"Translated text to {target_lang}: {translated_text}")

















# # dynamic_tt_translation.py
# # Import necessary libraries
# import os
# from transformers import MarianMTModel, MarianTokenizer
# # Dictionary mapping language pairs to MarianMT model names
# language_pair_models = {
#     ('en', 'fr'): 'Helsinki-NLP/opus-mt-en-fr',  # English to French
#     ('fr', 'en'): 'Helsinki-NLP/opus-mt-fr-en',  # French to English
#     ('en', 'de'): 'Helsinki-NLP/opus-mt-en-de',  # English to German
#     ('de', 'en'): 'Helsinki-NLP/opus-mt-de-en',  # German to English
#     ('en', 'es'): 'Helsinki-NLP/opus-mt-en-es',  # English to Spanish
#     ('es', 'en'): 'Helsinki-NLP/opus-mt-es-en',  # Spanish to English
#     # Add more language pairs as needed
# }

# # Function to load model and tokenizer based on language pair
# def load_model_and_tokenizer(source_lang: str, target_lang: str,cache_dir = './models_cache'):
#     model_name = language_pair_models.get((source_lang, target_lang))
    
#     if model_name is None:
#         raise ValueError(f"Translation model for {source_lang} to {target_lang} not available.")
    

#     os.makedirs(cache_dir,exist_ok=True)


#     # Load the appropriate model and tokenizer
#     tokenizer = MarianTokenizer.from_pretrained(model_name,cache_dir=cache_dir)
#     model = MarianMTModel.from_pretrained(model_name,cache_dir = cache_dir)
#     return model, tokenizer

# # Function to perform text-to-text translation
# def translate_text(text: str, source_lang: str, target_lang: str):
#     # Load the correct model and tokenizer based on the selected language pair
#     model, tokenizer = load_model_and_tokenizer(source_lang, target_lang)
    
#     # Tokenize the input text
#     tokenized_text = tokenizer(text, return_tensors="pt", padding=True)
    
#     # Generate the translation using the model
#     translated_tokens = model.generate(**tokenized_text)
    
#     # Decode the tokens to get the translated text
#     translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
#     return translated_text

# # Example usage
# if __name__ == "__main__":
#     # User input for text, source language, and target language
#     input_text = input("Enter the text to translate: ")
#     source_lang = input("Enter the source language code (e.g., 'en' for English): ")
#     target_lang = input("Enter the target language code (e.g., 'fr' for French): ")
    
#     # Perform translation
#     try:
#         translated_text = translate_text(input_text, source_lang, target_lang)
        
#         # Print the translated text
#         print(f"Translated text ({source_lang} to {target_lang}): {translated_text}")
    
#     except ValueError as e:
#         print(e)
