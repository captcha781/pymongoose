from setuptools import setup

setup(
    name="pymongoose",
    version="0.0.1",
    description="A mongoose js implementation in python to use mongodb easily in python",
    url="https://github.com/captcha781/py-mongoose",
    author="iamrealbhuvi",
    author_email="bhuvibhuvi541@gmail.com",
    license="MIT",
    packages=["pymongoose"],
    install_requires=[
        "pymongo>=4.5.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
