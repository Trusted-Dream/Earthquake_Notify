from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='Dream',
    version=__version__,
    description='Get earthquake information from Twitter.',
	url='https://github.com/Trusted-Dream/Earthquake_Notify',
    author='Dream',
    packages=find_packages('lib'),
    python_requires='>=3.9',
    install_requires=[
        'pytest',
        'urllib3',
        'python-dotenv',
    ],
	tests_require=["pytest"]
)