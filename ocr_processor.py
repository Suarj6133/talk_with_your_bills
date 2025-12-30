
import pytesseract
import os

# 1. Set the path to the Tesseract executable (Required since it's not on the System PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\suraj.kumar35_delhiv\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

INPUT_FOLDER = "image_cleaning_one_folder"
OUTPUT_FILE = "extracted_text.txt"

def perform_ocr(INPUT_FOLDER,OUTPUT_FILE):
    all_extracted_text = ""
    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith((".png", ".jpeg", ".jpg")):
            image_path = os.path.join(INPUT_FOLDER,filename)
            try:
                text = pytesseract.image_to_string(image_path)
                print(f"image_extracted from filename{text}")
                print("-"*20)
                print(text.strip)
                print("-"*20)
                all_extracted_text += f"\n-- Text from {filename}--\n{text}\n"
            except Exception as e:
                print(f"error in {filename}{error}")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(all_extracted_text)

    print (f"complete ocr done")




if __name__ == "__main__":
    perform_ocr(INPUT_FOLDER, OUTPUT_FILE)


