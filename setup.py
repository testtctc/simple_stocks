from setuptools import setup,find_packages


setup(
    name='stocks',
    version="0.1",
    author="tc",
    author_email="author@example.com",
    description="A small example package",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'lxml',
        "requests"
      ],


)