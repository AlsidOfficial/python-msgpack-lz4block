from setuptools import find_packages, setup

setup(
    name='msgpack-lz4block',
    packages=find_packages(),
    version='0.2.2',
    description='Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block '
                'compression.',
    author='Alsid',
    license='MIT',
    install_requires=[
        'msgpack',
        'lz4'
    ],
    download_url='https://github.com/AlsidOfficial/python-msgpack-lz4block/archive/refs/tags/v0.2.2.tar.gz'
)
