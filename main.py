import sys

import openpyxl
from openpyxl import drawing
from openpyxl.drawing import image


# It is not required for one to create a workbook on
# filesystem, therefore creating a virtual workbook
if len(sys.argv) < 5:
    print("Usage: add_image [file_to_add] [list_number] [cell] [image] [filename_to_save]\n"
          "Example: add_image report.xlsx  2  B55  pic.png  result.xlsx")
    exit()
wrkb = openpyxl.load_workbook(sys.argv[1])

# Number of sheets in the workbook (1 sheet in our case)
ws = wrkb.worksheets[(int(sys.argv[2]) - 1)]

# Adding a row of data to the worksheet (used to
# distinguish previous excel data from the image)

# A wrapper over PIL.Image, used to provide image
# inclusion properties to openpyxl library
img = openpyxl.drawing.image.Image(sys.argv[4])

# The Coordinates where the image would be pasted
# (an image could span several rows and columns
# depending on it's size)
img.anchor = sys.argv[3]

# Adding the image to the worksheet
# (with attributes like position)
ws.add_image(img)


# Saving the workbook created under the name of out.xlsx
wrkb.save(sys.argv[5])
wrkb.close()