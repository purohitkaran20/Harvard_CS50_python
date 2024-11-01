import sys

class Jar:
    def __init__(self, capacity=12, size=0):
            self.capacity = capacity
            self.size = size


    def __str__(self):
        return '🍪' * self.size


    def deposit(self, n):
        self.size += n
        return self.size


    def withdraw(self, n):
        self.size -= n
        return self.size

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError

    # Getter for size
    @property
    def size(self):
        return self._size

    #Setter for size
    @size.setter
    def size(self, size):
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError


def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()

