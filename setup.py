# coding: utf-8
from setuptools import find_packages, setup

with open('README.rst', encoding='utf-8') as fp:
    readme = fp.read()
setup(
    name='PIC',
    version='0.0.5',
    packages=find_packages(),
    install_requires=['pillow'],
    url='https://github.com/DxqS/PIC',
    license='MIT',
    author='Dxq',
    author_email='chk0125@126.com',
    description='图片合成 API',
    long_description=readme,
    keywords=[
        'PIL',
        'pillow'
    ]
)
