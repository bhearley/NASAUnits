from setuptools import setup, find_packages

setup(
    name='nasaunits',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    description='A Python module with numpy and pandas functions.',
    author='Brandon Hearley',
    author_email='brandon.l.hearley@nasa.gov',
    url='https://github.com/bhearley/NASAUnits',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
