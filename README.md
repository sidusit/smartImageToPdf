# smartImageToPdf
## Converts a nested folder of images into pdf
Useful when you have collected certain images or notes and want to convert that content into a single pdf. <br>
See the example subject folder it requires. One can create as many subfolder/subchapters as needed.

## Libraries required
from fpdf import FPDF <br>
import os <br>
from PIL import Image <br>
import PIL.ImageOps <br>
import time <br>

## Libraries references
https://pypi.org/project/fpdf/   <br>
https://pypi.org/project/Pillow/

## Parameters/Variables required to be specified before running the code <br>
<b> invertFlag </b> = 'No' # Specify Yes/No here in single brackets. <br>
Specify invert flag = 'Yes' only when you want to invert colors of the input images i.e white to black and V.V <br>
<b> imageFolderName </b> = 'Subject/' # Specify the input folder directory eg 'D:/folder1/folder3/' <br>
<b> output </b> = 'PGM.pdf' #Specify the output location and filename eg. 'D:/folder1/folder2/filename.pdf' <br>
