from setuptools import find_packages, setup

setup(
    name='python-msgpack-lz4block',
    packages=find_packages(),
    version='0.2.1',
    description='Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block '
                'compression.',
    author='Alsid',
    license='MIT',
    install_requires=[
        'msgpack',
        'lz4'
    ],
)
