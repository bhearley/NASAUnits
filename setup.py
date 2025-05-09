from setuptools import setup, find_packages

setup(
    name='nasa-units',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    description='A Python module with numpy and pandas functions.',
    author='Your Name',
    author_email='you@example.com',
    url='https://github.com/yourusername/myproject',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
