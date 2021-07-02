from setuptools import find_packages, setup

setup(
    name='msgpack-lz4block',
    packages=find_packages(),
    version='0.2.3',
    description='Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block '
                'compression.',
    author='Alsid',
    license='MIT',
    install_requires=[
        'msgpack',
        'lz4'
    ],
    url='https://github.com/AlsidOfficial/python-msgpack-lz4block',
    download_url='https://github.com/AlsidOfficial/python-msgpack-lz4block/archive/refs/tags/v0.2.3.tar.gz'
)
