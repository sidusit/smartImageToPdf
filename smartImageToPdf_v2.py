# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 00:10:55 2020

@author: sidus
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:42:38 2020

@author: sidus
"""

from fpdf import FPDF
import os
from PIL import Image
import PIL.ImageOps
import time

# Configure here
# Specify invert flag only when you want to invert colors of the input images
invertFlag = 'No' # Specify Yes/No here in single brackets
imageFolderName = 'D:/StudyMaterial/Courses/Subject/'
output = 'D:/StudyMaterial/Courses/PGM_temp.pdf'

def processImage(imagePath, invertFlag, pdfObj):
    if invertFlag == 'Yes':
        # print('inverting image: ', imagePath+ ' ...')
        img = Image.open(imagePath)
        img = img.convert('L')
        img = PIL.ImageOps.invert(img)
        imagePath = imagePath.replace('imageFolders','inverted')
        split = os.path.splitext(imagePath)
        imagePre = split[0]
        invertSubFolder = '/'.join(imagePre.split('/')[:-1])+'/'
        if not os.path.exists(invertSubFolder):
            os.makedirs(invertSubFolder)
        img.save(imagePre+'_inverted.png')
        imagePath = imagePre+'_inverted.png'
    
    img = Image.open(imagePath)
    print('adding image: ', imagePath, ' to pdf...')
    pdfObj.add_page()
    pdfObj.image(imagePath, x= 15 , y = 30, w = 270)
    pdfObj.set_font('Arial', 'I', 10)
    split = imagePath.split('/')
    pdfObj.cell(0, 5, '/'.join(split[:-1]) , 0, 1, 'C')
    pdfObj.cell(0, 5, '/'.join(split[-1:]) , 0, 1, 'C')

def recurChapters(path, invertFlag, pdfObj):
    subDirecItems = os.listdir(path)
    subDirecItems.sort()
    for item in subDirecItems:
        if os.path.isdir(path+item):
            print('Processing ', item)
            newPath = path+item+'/'
            recurChapters(newPath, invertFlag, pdfObj)
        else:
            newPath = path+item
            processImage(newPath, invertFlag, pdfObj)

if not os.path.exists('pdf/'):
    os.makedirs('pdf/')

if not os.path.exists('invert/'):
    os.makedirs('invert/')

# Code to identify the depth of the folders
pdfObj = FPDF(orientation='L')
startTime = time.time()
recurChapters(imageFolderName, invertFlag, pdfObj)
print('Saving output to pdf')
pdfObj.output(output)
endTime = time.time()
print('Completed all processes successfully in ',round(endTime-startTime,2),' seconds')