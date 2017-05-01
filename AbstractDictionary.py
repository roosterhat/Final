from AbstractCollection import AbstractCollection

class AbstractDictionary(AbstractCollection):
    def __getitem__(self, item):
        raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def add(self,item):
        self.insert(len(self),item)

    def delete(self,key):
        self.remove(key)

    def insert(self,key,item):
        raise NotImplementedError()

    def remove(self,key):
        raise NotImplementedError()

    def pop(self):
        raise NotImplementedError()

    def index(self,key):
        raise NotImplementedError()

    def get(self,index):
        raise NotImplementedError()

