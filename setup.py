from setuptools import setup, find_packages

setup(
    name="NEXUS-BOT",
    version="1.0.0",
    author="ArturoTF",
    author_email="arturotroyano@gmail.com",
    description="Nexus Bot first version",
    packages=find_packages(),
    install_requires=[
        "git+https://github.com/ArturoTF/pycord.git",
        "pandas==2.0.2",
        "googletrans==4.0.0-rc1",
        "google-cloud-translate==1.3.1",
        "google-cloud-texttospeech==0.2.0",
        "mysql-connector-python",
        "requests==2.31.0",
    ],
)
