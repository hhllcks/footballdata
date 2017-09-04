import setuptools

setuptools.setup(
    name="footballdata",
    version="0.1.0",
    url="https://github.com/hhllcks/footballdata",

    author="Hendrik Hilleckes",
    author_email="hhllcks@gmail.com",

    description="A wrapper for the football-data.org api",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
