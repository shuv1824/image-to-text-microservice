import pathlib
import pytesseract
from PIL import Image

BASE_DIR = pathlib.Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

dummyImg = IMAGE_DIR / "dummy.png"

preds = pytesseract.image_to_string(Image.open(dummyImg))
predictions = [x for x in preds.split("\n")]

print(predictions)
