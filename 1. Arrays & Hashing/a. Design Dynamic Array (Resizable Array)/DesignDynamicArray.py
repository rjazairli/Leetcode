class DynamicArray:

    # Initialize the DynamicArray with the given capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0                   # Initialize the current size (number of elements) to 0
        self.arr = [0] * capacity       # Create a list to store the elements

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set n at i-th index
    def insert(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        # Insert n at next empty position
        self.arr[self.size] = n        # Add the element at the current size
        self.size += 1                 # Increment the size by 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1             # soft delete the last element
        return self.arr[self.size]     # return the popped element

    # Double the capacity of the array when it's full
    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity  # Create a new list with the new capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]   # Copy elements to the new list
        self.arr = new_arr             # Update the data to the new list

    # Return the current number of elements in the array
    def getsize(self) -> int:
        return self.size

    # Return the current capacity of the array
    def getcapacity(self) -> int:
        return self.capacity

# Example usage:
arr = DynamicArray(1)
output = []
output.append(None)
output.append(arr.getsize())
output.append(arr.getcapacity())
print(output)

output = []
output.append(None)
arr.pushback(1)
output.append(arr.getcapacity())
arr.pushback(2)
output.append(arr.getcapacity())
print(output)

output = []
output.append(None)
output.append(arr.getsize())
output.append(arr.getcapacity())
arr.pushback(1)
output.append(arr.getsize())
output.append(arr.getcapacity())
arr.pushback(2)
output.append(arr.getsize())
output.append(arr.getcapacity())
output.append(arr.get(1))
arr.insert(1, 3)
output.append(arr.get(1))
output.append(arr.popback())
output.append(arr.getsize())
output.append(arr.getcapacity())
print(output)
