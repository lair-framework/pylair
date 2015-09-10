from distutils.core import setup

setup(
    name="pylair",
    version="1.0.1",
    author='Dan Kottmann',
    author_email='djkottmann@gmail.com',
    packages=['pylair'],
    url='https://github.com/lair-framework/pylair',
    license='LICENSE',
    description='Python library for interacting with Lair 2.0 API.',
    install_requires=[
        "requests >= 2.7.0"
    ],
)
