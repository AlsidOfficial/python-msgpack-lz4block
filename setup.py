from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

version = '0.2.5'

setup(
    name='msgpack-lz4block',
    packages=find_packages(),
    version=version,
    description='Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block '
                'compression.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alsid',
    license='MIT',
    install_requires=[
        'msgpack',
        'lz4'
    ],
    url='https://github.com/AlsidOfficial/python-msgpack-lz4block',
    download_url='https://github.com/AlsidOfficial/python-msgpack-lz4block/archive/refs/tags/v{}.tar.gz'.format(version)
)
