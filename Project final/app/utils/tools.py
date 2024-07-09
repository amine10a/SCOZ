import os 
from googletrans import Translator


# Function to save DataFrame to Excel
def save_to_excel(df, base_filename):
    directory = "download"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, base_filename)
    counter = 1
    while os.path.exists(filename):
        filename = os.path.join(directory, f"{os.path.splitext(base_filename)[0]}_{counter}.xlsx")
        counter += 1

    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")
    
    return filename
#function to reverse date

def reverse_date_format(date_str):
    parts = date_str.split('-')
    reversed_date_str = f"{parts[2]}-{parts[1]}-{parts[0]}"
    return reversed_date_str

#function to transalte de to en 
def translate_de_to_en(text):
    translator = Translator()
    translation = translator.translate(text, src='de', dest='en')
    return translation.text if translation else text

# in main for impoort from another script
if __name__ == "__main__":
    save_to_excel()
    reverse_date_format()
    translate_de_to_en()