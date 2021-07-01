import msgpack
import lz4.block


def deserialize(bytes_data, buffer_size=100 * 1024 * 1024):
    """
       Deserialize the bytes array data outputted by the MessagePack-CSharp lib using using lz4block compression
       :param bytes_data: Serialized bytes array data that has been generated by the MessagePack-CSharp lib using using
       lz4block compression.
       :param buffer_size: Buffer size to be used when decompressing.
       :return: deserialized data
   """
    deserialized = msgpack.unpackb(bytes_data)
    decompressed = b''
    for data in deserialized:
        if isinstance(data, bytes):
            decompressed += lz4.block.decompress(data, uncompressed_size=buffer_size)
    result = msgpack.unpackb(decompressed)
    return result