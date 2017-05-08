# coding:utf-8
'''
Created on 2017/5/6.

@author: Dxq
'''
from PIL import Image, ImageDraw, ImageFont

im = Image.open('poster_back.png')
font = 'app.ttf'
size = 50
text = '打'
ft = ImageFont.truetype(font, size)

draw = ImageDraw.ImageDraw(im)
sss = draw.textsize(text, font=ft)[0]

draw.text([320 - sss / 2, 198], text)
im.save('1.jpg')
