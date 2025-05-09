from setuptools import setup, find_packages

setup(
    name='nasaunits',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'json',
        'response',
    ],
    description='A Python module for unit conversion with the NASA GRC Granta MI Database.',
    author='Brandon Hearley',
    author_email='brandon.l.hearley@nasa.gov',
    url='https://github.com/bhearley/NASAUnits',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
