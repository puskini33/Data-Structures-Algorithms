from DoubleLinkedList import *


class Dictionary(object):
    def __init__(self, num_buckets=3):
        """Initializes a Map with the given number of buckets."""
        self.map = DoubleLinkedList()
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key) -> int:
        """Given a key this will create a number and then convert it to
        an index for the Map's buckets."""
        return hash(key) % self.map.count()  # an integer is generated that indexes the bucket

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key)  # given a key, the bucket ID is returned
        return self.map.get(bucket_id)  # returns the DLL object at the given index

    def get_slot(self, key, default=None) -> "bucket and node or bucket and None":
        """ Returns either the bucket and node for a slot, or None, None"""
        bucket = self.get_bucket(key)  # the bucket is identified

        if bucket:
            node = bucket.begin  # the first node in the bucket is identified
            i = 0

            while node:
                if key == node.value[0]:  # node.value[0] is key, node.value[1] is the value in the tuple, or the list
                    return bucket, node  # each node could have a tuple as a value
                else:
                    node = node.next
                    i += 1

        # fall through for both if and while above
        return bucket, None

    def get(self, key, default=None):
        """Returns the value in a bucket for a given bucket_key, or the default(i.e., just the node)."""
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node  # the node.value is returned

    def set_key_to_value(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)  # the value of the slot is a tuple
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def print_list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next


map_dictionaries = Dictionary()
print(map_dictionaries.hash_key("cars"))
map_dictionaries.get_bucket("cars")
map_dictionaries.get("cars")