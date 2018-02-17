from setuptools import setup

setup(name="tim_bot",
      version="20180216.1",
      description="reddit multi-use bot",
      url="https://github.com/timawesomeness/tim_bot",
      author="timawesomeness",
      license="AGPL",
      packages=["tim_bot"]
      install_requires=[
        "praw"
      ],
      zip_safe=False)
