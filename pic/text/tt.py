# coding:utf-8
'''
Created on 2017/5/6.

@author: Dxq
'''
from pic.api.poster import Poster

poster = Poster('poster_back.png', 'save_path.jpg')
poster.add_img('mat1.jpg', (313, 71, 120))
ft = 'app.ttf'
poster.add_mul_text('打d发发嘎\n嘎嘎dassa发', ft, color="#ffffff", position=(200, 300, 50), horizon=True,vertical=True)
# poster.add_mul_text('aaa\n大的', ft, color="#ffffff", position=(200, 300, 100), align="center")
poster.save()
