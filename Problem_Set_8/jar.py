class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be a negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = ""
        for i in range(self._size):
            cookies += "🍪"
        return cookies

    def deposit(self, cookies_deposited):
        new_size = cookies_deposited + self._size
        if new_size > self._capacity:
            raise ValueError("Not enough space")
        self._size = new_size
        return self._size
    
    def withdraw(self, cookies_withdrawed):
        if cookies_withdrawed > self._size:
            raise ValueError("Not enough cookies inside")
        self._size -= cookies_withdrawed
        return self._size

    @property
    def capacity(self):
        print("Jar's capacity is:")
        return self._capacity
    @capacity.setter
    def capacity(self, cap):
        if cap < 0:
            raise ValueError("Capacity can't be a negative number")
        print("The value of the capacity is set.")
        self._capacity = cap

    @property
    def size(self):
        print("Jar's capacity is:")
        return self._size
    @size.setter
    def size(self, size):
        print("The value of the size is set.")
        self._capacity = size


