from msgpack_lz4block import deserialize


def test_deserialize():
    serialized = b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga'
    assert deserialize(serialized) == [99, 'hoge', 'huga']
