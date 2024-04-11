from setuptools import setup

setup(
    name='immortal-client',
    version='0.0.3',
    packages=['immortal_client'],
    install_requires=['requests'],
    url='https://github.com/goldenhand76/immortal-client',
    author='goldenhand76',
    author_email='rezazarindast76@gmail.com',
    description='Python client for interacting with Immortals',
    long_description=open('README.md', 'r').read(),
    python_requires='>=3.6',
)