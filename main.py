from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\johnk\Downloads\Documents\link_img_second_ed_1710989270_7.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img, lang="Bengali")

# save extracted text to output.txt file
f = open("output.txt", "wb")
f.write(text.encode("utf-8"))
f.close()

# Displaying the extracted text
print(text[:-1])
