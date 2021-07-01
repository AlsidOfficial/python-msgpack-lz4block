# python-msgpack-lz4block

Deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block compression.

This project has been created to address [this issue](https://github.com/neuecc/MessagePack-CSharp/issues/1278).

## Installation

- Download the [latest release](https://github.com/AlsidOfficial/python-msgpack-lz4block/releases/latest)
- run setup.py install :

```
python setup.py install
```

## Usage

The ***deserialize*** function allows to deserialize a c# object that has been MessagePackSerialized using
Lz4BlockArray compression.

- Begin by importing the msgpack_lz4block module :
```python
>>> import msgpack_lz4block
```

- Now, let’s deserialize a bytes array (that was generated using MessagePack + Lz4BlockArray) :

```python
>>> msgpack_lz4block.deserialize(b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga')
[99, 'hoge', 'huga']
```

- We got the values... but we still miss the keys. The keys are not serialized in order to optimize the data usage. We can provide the key mapping as above, we get a beautyful key/value dict:

```python
>>> msgpack_lz4block.deserialize(b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga', key_map=['Age', 'FistName', 'LastName'])
{'Age': 99, 'FistName': 'hoge', 'LastName': 'huga'}
```

- That's all, we successfully deserialized the data that was generated by the above c# code

```c#
using MessagePack;
using System.IO;

namespace msgpackWithLz4
{
    [MessagePackObject]
    public class MyClass
    {
        [Key(0)]
        public int Age { get; set; }

        [Key(1)]
        public string FirstName { get; set; }

        [Key(2)]
        public string LastName { get; set; }
        [IgnoreMember]
        public string FullName { get { return FirstName + LastName; } }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var mc = new MyClass
            {
                Age = 99,
                FirstName = "hoge",
                LastName = "huga",
            };
            var lz4Options = MessagePackSerializerOptions.Standard.WithCompression(MessagePackCompression.Lz4BlockArray);
            byte[] bytes = MessagePackSerializer.Serialize(mc, lz4Options);
            File.WriteAllBytes("output", bytes);
        }
    }
}
```

## Dependencies:

This library depends on:

- [msgpack](https://github.com/msgpack/msgpack-python) : to deserialize the msgpack structure
- [lz4](https://github.com/python-lz4/python-lz4) : to decompress the lz4 data
