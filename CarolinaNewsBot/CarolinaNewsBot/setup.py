from setuptools import find_packages, setup

setup(
    name="CarolinaNewsBot",
    packages=find_packages(exclude=["CarolinaNewsBot_tests"]),
    install_requires=[
        "dagster==1.6.13",
        "dagster-webserver==1.6.13",
        "beautifulsoup4==4.12.3",
        "GoogleNews==1.6.14",
        "tweepy==4.14.0",
        "openai==1.14.3",
        "unidecode==1.3.8",
        "gensim==4.3.2",
        "scipy==1.12.0",
        "pandas==2.2.1",
        "nltk==3.8.1",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
