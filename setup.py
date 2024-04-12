from setuptools import setup, find_packages

setup(
    name="NEXUS-BOT",
    version="0.1.0",
    author="ArturoTF",
    author_email="arturotroyano@gmail.com",
    description="Nexus Bot en desarrollo.",
    packages=find_packages(),
    install_requires=[
        "py-cord==2.0.0b1",
        "pandas==2.0.2",
        "googletrans==4.0.0-rc1",
        "google-cloud-translate==1.3.1",
        "google-cloud-texttospeech==0.2.0",
        "mysql-connector-python",
    ],
)
