# coding:utf-8
'''
Created on 2017/5/3.

@author: Dxq
'''
from PIL import Image, ImageDraw, ImageFont


class Poster(object):
    """
    海报对象，用于生成合成海报
    """

    def __init__(self, path=None, save_path=None):
        self.path = path
        self.poster = Image.open(path)
        self.size = self.poster.size
        self.save_path = save_path
        self.back = Image.new("RGBA", self.size, color=(255, 255, 255, 1))

    def add_img(self, path=None, position=None):
        back = self.back
        poster = self.poster
        self_pic = Image.open(path)
        self_wid, self_hei = self_pic.size
        show_wid = position[2]
        if self_hei > self_wid:
            r = float(self_hei * show_wid) / self_wid
            self_pic = self_pic.resize((show_wid, int(r)), Image.ANTIALIAS)
            box = (position[0], position[1], position[0] + show_wid, position[1] + int(r))
        else:
            r = float(self_wid * show_wid) / self_hei
            self_pic = self_pic.resize((int(r), show_wid), Image.ANTIALIAS)
            box = (position[0], position[1], position[0] + int(r), position[1] + show_wid)
        back.paste(self_pic, box)

        r, g, b, a = poster.split()
        back.paste(poster, (0, 0, self.size[0], self.size[1]), mask=a)
        self.poster = back
        # back.save(self.save_path)
        return True

    def add_text(self, text, font, color="#000000",
                 position=None, vertical=False, horizon=False, mode=None):

        draw = ImageDraw.ImageDraw(self.back, mode)
        size = position[2]
        ft = ImageFont.truetype(font, size)

        x = (self.size[0] - self.textsize(text, size, ft, mode)[0]) / 2 if horizon else position[0]
        y = (self.size[1] - self.textsize(text, size, ft, mode)[1]) / 2 if vertical else position[1]

        draw.text([x, y], text, font=ft, fill=color)
        return True

    def add_mul_text(self, text, font, color="#000000",
                     position=None, vertical=False, horizon=False, mode=None,
                     spacing=4, align="center"):

        draw = ImageDraw.ImageDraw(self.back, mode)
        size = position[2]
        ft = ImageFont.truetype(font, size) if font else font
        x = (self.size[0] - self.textsize(text, ft, mode)[0]) / 2 if horizon else position[0]
        y = (self.size[1] - self.textsize(text, ft, mode)[1]) / 2 if vertical else position[1]
        return draw.multiline_text([x, y], text, fill=color, font=ft, anchor=None, spacing=spacing, align=align)

    def textsize(self, text, font=None, mode=None):
        return ImageDraw.ImageDraw(self.back, mode).textsize(text, font=font)

    def save(self):
        self.poster.save(self.save_path)
        return True
