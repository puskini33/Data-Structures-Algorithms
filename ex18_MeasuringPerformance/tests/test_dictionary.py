from dictionary import Dictionary
from DoubleLinkedList import *


def test_hash_key():
    map_buckets = Dictionary()
    bucket_key = map_buckets.hash_key('car')
    assert isinstance(bucket_key, int) is True


def test_get_bucket():
    map_buckets = Dictionary()
    bucket_id = map_buckets.hash_key('car')
    bucket_object = map_buckets.map.get(bucket_id)
    assert bucket_object
    assert type(bucket_object) is DoubleLinkedList


def test_get_slot():
    map_buckets = Dictionary()
    bucket_object = map_buckets.get_bucket('9.0')
    key = map_buckets.set_key_to_value('9.0', 'Tesla')
    bucket_object, node = map_buckets.get_slot('9.0')
    assert node.value[1] == 'Tesla'
    assert node.value[0] == '9.0'


def test_set_key_to_value():
    map_buckets = Dictionary()
    bucket_object = map_buckets.get_bucket('fruit')

    map_buckets.set_key_to_value('fruit', 'banana')
    assert map_buckets.get_node_value('fruit') == 'banana'
    map_buckets.set_key_to_value('fruit', 'apple')
    assert map_buckets.get_node_value('fruit') == 'apple'
    assert map_buckets.get_node_value('fruit') != 'banana'


def test_delete():
    map_buckets = Dictionary()
    bucket_object = map_buckets.get_bucket('fruit')
    map_buckets.set_key_to_value('fruit', 'banana')
    map_buckets.delete('fruit')
    assert map_buckets.get_node_value('fruit') is None


if __name__ == '__main__':
    test_hash_key()
    test_get_bucket()
    test_get_slot()
    test_set_key_to_value()
    test_delete()