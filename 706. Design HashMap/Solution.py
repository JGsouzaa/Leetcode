class MyHashMap:

    def __init__(self):
        self.length = 1000
        self.map = [None] * self.length
    def put(self, key: int, value: int) -> None:
        index = key % self.length
        if self.map[index] is None:
            #creates an array inside the value to store the key-value
            self.map[index] = []
        for i, (x, y) in enumerate(self.map[index]):
            if x == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))
    def get(self, key: int) -> int:
        index = key % self.length
        if self.map[index] is None:
            return -1
        for existing_key, existing_value in self.map[index]:
            if existing_key == key:
                return existing_value
        return -1
    def remove(self, key: int) -> None:
        index = key % self.length
        if self.map[index] is None:
            return
        for i, (existing_key, existing_value) in enumerate(self.map[index]):
            if existing_key == key:
                del self.map[index][i]
                return