from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = FastAPI()

@app.post('/ocr')
def ocr(image: UploadFile = File(...)):
    filepath = 'txtFile'
    with open(filepath, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(filepath, lang='eng')

