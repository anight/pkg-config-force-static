
import setuptools

setuptools.setup(
     name='pkg-config-force-static',
     version='0.1',
     scripts=['pkg-config'] ,
     author="Andrei Nigmatulin",
     author_email="andrei.nigmatulin@gmail.com",
     description="pkg-config wrapper tool for static linking with selected libraries",
     url="https://github.com/anight/pkg-config-force-static",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
