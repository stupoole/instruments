import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license = fh.read()

setuptools.setup(
    name='instruments',
    version='0.1',
    license=license,
    packages=setuptools.find_packages(
        exclude=('docs')
    ),
    url='https://github.com/stupoole/instruments',
    install_requires=[
        'numpy',
        'pyvisa',
        'paramiko',
        'pyserial'
    ],
    include_package_data=True,
)