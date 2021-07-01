import msgpack
import lz4.block


def deserialize(bytes_data, key_map=None, buffer_size=100 * 1024 * 1024):
    """
       Deserialize the bytes array data outputted by the MessagePack-CSharp lib using using lz4block compression
       :param bytes_data: Serialized bytes array data that has been generated by the MessagePack-CSharp lib using using
       lz4block compression.
       :param key_map: A key list to produce a key value dict.
       :param buffer_size: Buffer size to be used when decompressing.
       :return: deserialized data
   """
    deserialized = msgpack.unpackb(bytes_data)
    decompressed = b''
    for data in deserialized:
        if isinstance(data, bytes):
            decompressed += lz4.block.decompress(data, uncompressed_size=buffer_size)
    obj = msgpack.unpackb(decompressed)
    if key_map is not None:
        if not isinstance(key_map, list):
            raise Exception('The key_map should be a list')
        elif len(obj) != len(key_map):
            raise Exception('The key_map list should be the same length has the object')
        else:
            dict_obj = {}
            for index in range(0, len(key_map)):
                dict_obj[key_map[index]] = obj[index]
            return dict_obj
    return obj
