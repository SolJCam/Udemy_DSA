import pdb


class hash_table:
    def __init__(self, size):
        if type(size) == int:
            self.data = [[] for arr in range(size)]

    def _hash(self, key):
        sum = 0
        for ec in key: 
            sum += ord(ec)
        hash = round(sum/len(key))
        return hash

    def set(self, k, v):
        address = self._hash(k)
        self.data[address].append([k,v])  # appeding a list due to avoid collisions i.e. future data being put in the same place in memory

    def get(self, k):
        address = self._hash(k)
        if len(self.data[address]) > 1:
            for arr in self.data[address]:
                if arr[0] == k:
                  return arr[1]
        else:
            v = self.data[address][0][1]
            return v



