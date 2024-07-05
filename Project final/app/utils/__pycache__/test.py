from googletrans import Translator

def translate_de_to_en(text):
    translator = Translator()
    translation = translator.translate(text, src='de', dest='en')
    return translation.text

# Example usage
category = "Architekten & Planungsbüros"
category = translate_de_to_en(category)
print(category)