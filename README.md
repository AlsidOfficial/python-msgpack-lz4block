# python-msgpack-lz4block
Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block compression.

This project has been created to address [this issue](https://github.com/neuecc/MessagePack-CSharp/issues/1278).

## Installation

- git clone this repo
- run setup.py install :
```
python setup.py install
```

## Usage
```python
from msgpack_lz4block import deserialize
serialized = b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga'
deserialized = deserialize(serialized)
print(deserialized)
[99, 'hoge', 'huga']
```


