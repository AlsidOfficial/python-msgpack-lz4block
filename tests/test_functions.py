from msgpack_lz4block import deserialize


def test_deserialize():
    serialized = b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga'
    assert deserialize(serialized) == [99, 'hoge', 'huga']


def test_deserialize_with_key_map():
    serialized = b'\x92\xd4b\x0c\xc6\x00\x00\x00\r\xc0\x93c\xa4hoge\xa4huga'
    assert deserialize(serialized, key_map=['Age', 'FistName', 'LastName']) == {'Age': 99, 'FistName': 'hoge',
                                                                                'LastName': 'huga'}


def test_deserialized_with_sub_obj_key_map():
    serialized = b'\x92\xd4b\x15\xc6\x00\x00\x00\x17\xf0\x06\x94c\xa4hoge\x92\xa6coucou*\xa4huga'
    key_map = ['Age', 'FirstName', ('MySubObj', ['MyStr', 'MyInt']), 'LastName']
    deserialized =deserialize(serialized, key_map)
    assert deserialized == {'Age': 99, 'FirstName': 'hoge',
                                                'MySubObj': {'MyStr': 'coucou', 'MyInt': 42}, 'LastName': 'huga'}
