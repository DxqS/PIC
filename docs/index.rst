.. pic documentation master file, created by
   sphinx-quickstart on Thu May  4 22:38:49 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pic's documentation!
===============================

pic: Python Image Composition用 Python 实现图片合成
==============================

海报生成API，基于 PIL，全面优化接口，更有 Python 范儿。


用来干啥
----------------

一些常见的场景

* 宣传海报自定义合成
* ... [1]_

总而言之，可用来实现各种图片合成

..  [1] 想怎么合就怎么合


轻松安装
----------------

**pic 适合任意版本python

可以通过以下方式安装

1. 从 PYPI 官方源下载安装 (在国内使用可能比较慢或不稳定)::

    pip install -U PIC

简单上手
----------------


登陆微信::

    # 导入模块
    from PIC import *
    # 初始化机器人，扫码登陆
    poster = Poster()

添加图片::

    res = poster.add_img()

添加文案::

    poster.add_text()

保存::

    poster.save()

模块特色
----------------


说明文档
----------------

http://pic.readthedocs.io

项目主页
----------------

http://github.com/DxqS/PIC


--------


