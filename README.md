# OCR_App
Application for optical character regonition. Build in FASTAPI -> Python

Endpoint: localhost/ocr
method: POST

Example CURL:
  curl -X 'POST' \
  'http://127.0.0.1:8000/ocr' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@tesseract.PNG;type=image/png'


Instalation:
  * Install tesseract on your computer
  * clone my repo
  * create virtual env
  * instal dependencies from requirements.txt -> pip install -r ./requiremetns
  * run application -> uvicorn main:app
  * Ready!!!
