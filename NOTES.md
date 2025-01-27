# `Table of contents`

## `Circular Indexing / Iteration`
Given an array `[1, 2, 3, 4, 5, 6]`

To get the next index for circular indexing:

```py
n = len(arr)
index = 0

next_index = (index + 0) % n
```

Another Example
```py
n = len(arr)
index = 3

for i in range(n):
    res.append(A[index])
    index = (index + 1) % n
```

---

## `D E F A U L T S`

### `1. Default Values`
### 1.1. `get()`
```py
data = {'Name': 'Zinga', 'Location': 'Migombani', 'Age': 33}
hobby = data.get('Hobbies', 'Coding')
print(hobby) # Coding
```
> **PROBLEM** - Sets default value for all missing keys


### 1.2. `setdefault()`
```py
data = {'Name': 'Zinga', 'Location': 'Migombani', 'Age': 33}
data.setdefault('Hobbies', None)

print(data['Hobbies']) # None
```
> **PROBLEM** - We need to know the key for which we want to create a default value beforehand


### 1.3. Custom default value
```py
from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla')

ice_cream['Cobih'] = 'Chunky Monkey'
ice_cream['Santa'] = 'Butter Pecan'

print(ice_cream['Cobih']) # Chunky Monkey
print(ice_cream['Chiwawa']) # Vanilla
```

### `2. Default Integers`
### 2.1. Without defaultdict
```py
names = [
    'Mchicha', 'Dingo', 'Evan', 'Mbenda', 'Sukari', 'Mchicha', 'Dingo', 'Mchicha'
]

freqs = {}

for name in names:
    # freqs[name] = freqs.get(name, 0) + 1

    if name in freqs:
        freqs[name] += 1
    else:
        freqs[name] = 1

print(freqs)
# {'Mchicha': 3, 'Dingo': 2, 'Evan': 1, 'Mbenda': 1, 'Sukari': 1}
```
### 2.2. With defaultdict
```py
from collections import defaultdict
names = ['Nik', 'Kate', 'Evan', 'Kyra', 'John', 'Nik', 'Kate', 'Nik']

counts = defaultdict(int)
for name in names:
    counts[name] += 1

print(counts)
# defaultdict(<class 'int'>, {'Nik': 3, 'Kate': 2, 'Evan': 1, 'Kyra': 1, 'John': 1})
```

### `3. Default Lists`
```py
# Resource: https://realpython.com/python-defaultdict/

dep = [
    ('Sales', 'John Fitina'),
    ('Sales', 'Martin Dungicha'),
    ('Accounting', 'Jane Kololeni'),
    ('Marketing', 'Elizabeth Mambo'),
    ('Marketing', 'Adam Wema')
]

from collections import defaultdict

mapping = defaultdict(list)
for department, employee in dep:
    mapping[department].append(employee)

    # [Code without default dict]
    # if department not in mapping:
    #     mapping[department] = []
    # mapping[department].append(employee)

# output
{
    'Sales': ['John Fitina', 'Martin Dungicha'],
    'Accounting' : ['Jane Kololeni'],
    'Marketing': ['Elizabeth Mambo', 'Adam Wema']
}
```
---
## `Flatten an Array`

```py
def transpose(strs):
    grid = [list(str) for str in strs]
    return list(map(list, zip(*grid)))
```

### 1. Basic iterative function
```py
def flatten(matrix):
    new_list = []
    for row in matrix:
        for num in row:
            new_list.append(num)
    return new_list
```

### 2. Using array functions
```py
def flatten(matrix):
    new_list = []
    for row in matrix:
        new_list.extend(row)
    return new_list
```
### 3. Flatten List of Lists Using sum
`sum` has an optional argument: sum(iterable [, start]), so you can do:
```py
regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = sum(regular_list, []) # [] + [1, 2, 3, 4] + [5, 6, 7] + [8, 9]

flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
---
## `Find i,j in a flattened 2d matrix`
Given a 2 matrix, 
```py
[[1, 2, 3],
 [3, 4, 5],
 [6, 7, 8]]
```
Flattened to [1, 2, 3, 4, 5, 6, 7, 8, 9].

**Challenge**: 
How do you find the position of an element in the matrix given index i in the flattened list?

```py
# Trick
rows, cols = len(matrix), len(matrix[0])
left, right = 0, rows * cols

item_idx = idx
i, j = idx // cols, idx % cols  # divmod(idx, cols)

# Example - index 7
i, j = divmod(7, cols) # (2, 1) -> i.e row: 2, col: 1

print(matrix[2][1]) # 7
```
---
## `Reverse Iterables`
### 1. By `reverse()`
It reverses an iterable in-place
```py
systems = ['Windows', 'macOS', 'Linux']
systems.reverse()

print(systems) # ['Linux', 'macOS', 'Windows']
```

### 2. By Slicing -> `[::-1]`
```py
systems = ['Windows', 'macOS', 'Linux']
reversed_list = systems[::-1]
print(systems) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
n = len(systems)
for i in range(n-1, -1, -1):
    print(systems[i])
```

### 3. By `reversed()`
```py
systems = ['Windows', 'macOS', 'Linux']
reversed_systems = reversed(systems)
print(list(reversed_systems)) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
for system in reversed(systems):
    print(system)
```

## `Sort Iterables`
### 1. By `sort()`
Sorts an iterable in place

```py
prime = [11, 3, 7, 5, 2]
prime.sort()
print(prime) # [2, 3, 5, 7, 11]
```

### 2. By `sorted()`
```py
prime = [11, 3, 7, 5, 2]
new_prime = sorted(prime)
print(new_prime) # [2, 3, 5, 7, 11]
```

### Syntax: Pameters
`sort()` and `sorted()` hav two optional parameters:<br>
1. `reverse` - If True, the sorted list is descending order<br> 
2. `key` - function that serves as a key for the sort comparison

### Sort the list in Descending order
```py
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print(vowels) # ['u', 'o', 'i', 'e', 'a']
```

### Sort with custom key function
```py
# Sort by lenth of strings in a list
list.sort(key=len)
sorted(list, key=len)

e.g.
words = ['pinapples', 'grape', 'apples', 'mangoes']
sorted(words, key=len) # ['grape', 'apples', 'mangoes', 'pinapples']
```

### Sort a list of list by sum
```py
nums = [[7, 9], [2, 4], [8, 1], [5, 6]]
sorted(nums, key=sum) # [[2, 4], [8, 1], [5, 6], [7, 9]]
```

---
### Sort dictionary
```py
sorted_dict = sorted(d.items(), key=lambda x: x[1])
sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_dict)
```
### Sorting by the first index is the default sorting mechanism
```py
nums = [[7, 9], [2, 4], [8, 1], [5, 6]]
sorted_nums = sorted(nums, key=lambda x: x[0])
sorted_list = sorted(nums)

assert sorted_nums == sorted_list # TRUE

# Alternatively
sorted(d, key=d.get, reverse=True):

# Examples
employees = [
    {'Name': 'Sifu', 'age': 25, 'salary': 10000},
    {'Name': 'Chepe', 'age': 30, 'salary': 81000},
    {'Name': 'Ericko', 'age': 18, 'salary': 110000},
]

employees.sort(key=lambda x: x.get('Name'))
employees.sort(key=lambda x: x.get('salary'), reverse=True)
```
---
## `Heaps`
### Time Complexites
`heapq.heapify()` -> `O(n)` </br>
> Transform list x into a heap, in-place, in linear time. </br>

`heapq.heappush()` -> `O(logn)` </br>
`heapq.heappop()` ->  `O(logn)` </br> </br>


### `minHeap`
```py
>>> import heapq
>>> heapq.heapify(lst)
```
<br/>

### `maxHeap`
1. Solution: `heapq._heapify_max(lst)`

```py
>>> lst = [5, 1, 3, 7, 2]

>>> heapq._heapify_max(lst)
>>> pop_max = heapq._heappop_max(lst)
```
2. Solution: **Use Negatives**

```py
>>> array = [1, 4, 6, 2, 5, 3, 9, 8, 7]
>>> maxHeap = []
>>> for num in array:
        heapq.heappush(maxHeap, -num)

>>> print('maxHeap:', maxHeap)
# maxHeap: [-9, -8, -6, -7, -2, -3, -4, -1, -5]
```

### Multiple Items Heap
```py
>>> lst = [
    (5, 'write code'),
    (7, 'release product'), 
    (1, 'write spec'),
    (3, 'create tests')
]
>>> heap = []
>>> for num in array:
        heappush(heap, num)

>>> heappop(heap)
# (1, 'write spec')
```
---
## `Traversals`
### Depth First Searh
> Implemented using a STACK
<br/>

### Breadth First Search
> Implemented using a QUEUE

---

## `Infinity`
### 1. Using `float('inf')` and `float('-inf)`
```py
positive_infinity = float('inf') # inf
negative_infinity = float('-inf') # -inf
```

### 2. Using Python’s math module
```py
import math
 
positive_infinity = float('inf') # inf
negative_infinity = float('-inf') # -inf
```

### 3. Integer `maxsize`
```py
import sys

maxSize = sys.maxsize # 9223372036854775807
minSize = -sys.maxsize # -9223372036854775807
```

### 4. Using Python’s decimal module
```py
from decimal import Decimal
 
positive_infinity = Decimal('Infinity') # Infinity
negative_infinity = Decimal('-Infinity') # -Infinity
```

---

## `Algorithms' Summary`
### **1. Brute Force**
This approach finds all the possible solutions and selects desired solution per given the constraints.

### **2. Dynamic Programming** 
It uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.

### **3. Backtracking** 
It uses Brute Force approach but to find ALL the solutions.
  - Solutions to the Backtracking problems can be represented as **State-Space Tree**.
  - The constrained applied to find the solution is called Bounding function.
  - Backtracking follows **Depth-First Search method**.
  - Branch and Bound is also a Brute Force approach, which uses Breadth-First Search method.
  
---

## `STR TO INT: INT TO STR`
### `ord()`
Returns an integer representing the Unicode character for your input string.
```py
>>> [ord(str(i)) for i in range(0, 10)]
# [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

>>> import string
>>> [ord(i) for i in string.ascii_uppercase]
# [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

>>> [ord(i) for i in string.ascii_lowercase]
# [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
```

#### Getting a corresponding integer from an integer character
```py
>>> ch = '5'
>>> ord(ch) - ord('0') # 5
```

### `chr()`
Returns a character (a string) from an integer (represents unicode code point of the character)

```py
>>> val = 5 
# it's corresponding unicode is 53 = 48 + 5: ord('0') + 5

>>> val_repr = ord('0') + val
>>> char_rep = chr(val_repr) # 5
```
---

## Random
`random.randint(a, b)` -> a: inclusive, b: inclusive </br>
> coverage a <= n <= b </br>

`random.randrange(a, b)` -> a: inclusive, b: exclusive
> coverage a <= n < b </br>

---
## Sorting Algorithms(Major)

### Time Complexities
| Algorithm	     | Time Complexity	 | Space Complexity |
|----------------|-------------------|------------------| 
| Selection Sort | O(n^2)            | O(1)             |
| Bubble Sort    | O(n^2)            | O(1)             |
| Insertion Sort | O(n^2)            | O(1)             |
| Quick Sort     | O(n^2)            | O(log(n))        |
| Heap Sort      | O(n log(n))	     | O(1)             |
| Merge Sort     | O(n log(n))	     | O(n)             |
| Heap Sort      | O(n log(n))	     | O(1)             |