from setuptools import setup,find_packages
setup(name="load_boston",
      version="0.0.1",
      author="anam",
      author_email="anamshaikh0515@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
)