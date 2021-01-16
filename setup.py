from setuptools import setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="clothes_shop",
    description="Clothes Shop Project for YouTube",
    author="Alex V",
    author_email="alex.v.engineering@gmail.com",
    long_description=readme,
    test_suite="clothes_shop/test"
)
