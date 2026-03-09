
from paddleocr import PaddleOCR
import numpy as np
import cv2

# import datetime
# i = datetime.datetime.now()

ocr = PaddleOCR()


def parse_ocr(file):
    file_bytes = file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = ocr.predict(image)
    for res in result:
        res.print()



# # Run OCR inference on a sample image 
result = ocr.ocr("/Users/lokesh/Solix/IDP/data/invoice-template.png")

# result = ocr.ocr("image.png")

texts = result[0]["rec_texts"]

print(texts)

# for res in result:
#         res.print()

# j = datetime.datetime.now()
# print(j-i)

# # Visualize the results and save the JSON results
# for res in result:
#     res.print()
    # res.save_to_img("output")
    # res.save_to_json("output")



# import datetime
# from paddleocr import PaddleOCR
# i = datetime.datetime.now()
# ocr = PaddleOCR()
# print("Loaded successfully")
# j = datetime.datetime.now()
# print(j-i)