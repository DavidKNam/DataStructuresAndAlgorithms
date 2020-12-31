# Implementation of Hash Table in Python

class HashTable:
    def __init__(self, bucketSize = 16):
        self.bucket = bucketSize
        self.hashmap = [[] for _ in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        return len(key) % self.bucket

    def put(self, key, value):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for index, item in enumerate(reference):
            if item[0] == key:
                reference[index][1] = value
                return None
        reference.append([key, value])
        return None

    def get(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for index, item in enumerate(reference):
            if item[0] == key:
                return item[1]

        return -1

    def remove(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for index, item in enumerate(reference):
            if item[0] == key:
                reference.pop(index)
                return None
        return None

    def keys(self):
        if not self.hashmap:
            return None

        result = []
        for item in self.hashmap:
            if item:
                for item2 in item:
                    result.append(item2[0])

        return result

h=HashTable()
h.put('grapes',1000)
h.put('apples',10)
h.put('ora',300)
h.put('banan',200)
print(h.get('grapes'))
print(h)
h.remove('apples')
print(h)
print(h.keys())