import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    setuptools.setup(
    name="trello_client-basics-api-dimazey", version="0.0.1", author="Dimazey", 
    author_email="mof@list.ru", description="trello client", long_description=long_description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/Dimazey/trello_kl", 
    packages=setuptools.find_packages(), 
    classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], 
    python_requires='>=3.6',)