# msgpack-lz4block

Python lib to deserialize and decompress messages serialized by the C# lib "MessagePack-CSharp" using lz4block compression.

This project has been created to address [this issue](https://github.com/neuecc/MessagePack-CSharp/issues/1278).

## Installation

- run the above command:
```shell
pip install msgpack-lz4block
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
>>> msgpack_lz4block.deserialize(b'\x92\xd4b&\xc6\x00\x00\x00(\xf0\x17\x94 \xa8Perceval\x92\xaeOn en a gros !*\xa9de Galles')
[32, 'Perceval', ['On en a gros !', 42], 'de Galles']
```

- We got the values... but we still miss the keys. The keys are not serialized in order to optimize the data usage. We can provide the key mapping as above, we get a beautiful key/value dict:

```python
>>> key_map = ['Age', 'FirstName', ('MySubObj', ['Quote', 'MyInt']), 'LastName']
>>> msgpack_lz4block.deserialize(b'\x92\xd4b&\xc6\x00\x00\x00(\xf0\x17\x94 \xa8Perceval\x92\xaeOn en a gros !*\xa9de Galles', key_map=key_map)
{'Age': 32, 'FirstName': 'Perceval', 'MySubObj': {'Quote': 'On en a gros !', 'MyInt': 42}, 'LastName': 'de Galles'}
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
        public MySubClass MySubObj { get; set; }
        [Key(3)]
        public string LastName { get; set; }
    }

    [MessagePackObject]
    public class MySubClass
    {
        [Key(0)]
        public string Quote { get; set; }
        [Key(1)]
        public int MyInt { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var myObj = new MyClass
            {
                Age = 32,
                FirstName = "Perceval",
                LastName = "de Galles",
                MySubObj = new MySubClass
                {
                    Quote = "On en a gros !",
                    MyInt = 42
                },
            };
            var lz4Options = MessagePackSerializerOptions.Standard.WithCompression(MessagePackCompression.Lz4BlockArray);
            byte[] bytes = MessagePackSerializer.Serialize(myObj, lz4Options);
            File.WriteAllBytes("output", bytes);
        }
    }
}
```

## Dependencies:

This library depends on:

- [msgpack](https://github.com/msgpack/msgpack-python) : to deserialize the msgpack structure
- [lz4](https://github.com/python-lz4/python-lz4) : to decompress the lz4 data
