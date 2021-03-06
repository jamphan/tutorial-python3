# Lesson 07: Checkpoint

<!-- TOC depthFrom:2 orderedList:true -->

1. [Terminal](#terminal)
2. [Built-in Functions](#built-in-functions)
3. [Data-Types](#data-types)
    1. [Integers](#integers)
    2. [Strings](#strings)
        1. [String Methods](#string-methods)
    3. [Booleans](#booleans)
4. [Data Structures](#data-structures)
    1. [Arrays](#arrays)
        1. [Indexing Arrays](#indexing-arrays)
        2. [Array Methods](#array-methods)
5. [Control-Flow](#control-flow)
    1. [`if` to branch out](#if-to-branch-out)
    2. [`for` to iterate](#for-to-iterate)
    3. [`continue` and `break`](#continue-and-break)

<!-- /TOC -->

## Terminal

|Command|Description|Example|
|---|---|---|
|`pwd`|Print working directory|
|`cd`|Change directory|`cd ~/Desktop`
|`cd ..`|Go up on directory|
|`ls`|List directory contents|

## Built-in Functions

|Function|Description|Example|
|---|---|---|
|[`input()`](https://docs.python.org/3/library/functions.html#input)|Polls the user for input, and returns the entered string up-to and excluding the newline|`age = input("Enter your age> ")`
|[`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)|Provides a counter as you iterate through a sequence|`for idx, ele in enumerate(["a", "b", "c"]):`
|[`len()`](https://docs.python.org/3/library/functions.html#len)|Determins the number of elements in some iterable|`len("Hello") == 5`
|[`range()`](https://docs.python.org/3/library/functions.html#func-range)|Provides a range of integers|`for ii in range(0, 10):`
|[`zip()`](https://docs.python.org/3/library/functions.html#zip)|Allows you to iterate multiple objects at once|`for aa, bb in zip(listA, listB):`

## Data-Types

### Integers

- Only whole numbers
- Cast to an integer with `int("1") == 1`

### Strings

#### String Methods

|Method|Description|Example
|---|---|---
|[`.isnumeric()`](https://docs.python.org/3/library/stdtypes.html#str.strip)|Checks that a string can be converted into a numeric type|`"123".isnumeric() == True`
|[`.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip)|Removes leading and trailing white space|`"  ab   c   ".strip() == "ab   c"`
|[`.split()`](https://docs.python.org/3/library/stdtypes.html#str.split)|Splits a string based on some separator, default is space|`"a,b,c".split(',') == ["a", "b", "c"]`

### Booleans

**Inequalities**

|Symbols|Description|Example
|---|---|---
|`>`, `>=`|Checks for greater than (or equal to)|`(5 > 10) == False`
|`<`, `<=`|Checks for less than (or equal to)|`(10 < 5) == False`
|`!=`|Not equal to|`(10 != 5) == True`
|`==`|Equal to|`("A" == "a") == False`

**Operators**

- `and`: Both must be `True` for the result to be `True`
- `or`: At least one must be `True` for the result to be `True`
- `not`: Inverse result

**Truth Table**

|A|B|`and`|`or`|
|---|---|---|---
|`True`|`True`|`a and b == True`|`a or b == True`|
|`True`|`False`|`a and b == False`|`a or b == True`|
|`False`|`True`|`a and b == False`|`a or b == True`|
|`False`|`False`|`a and b == False`|`a or b == False`|

## Data Structures

### Arrays

``` py
example_list = [1, 2, 3, 4]
```

#### Indexing Arrays

- `some_list[1]`: Returns the single element at index = 1 (the 2nd element)
- `some_list[1:]`: Returns all elements starting and including index = 1 (every element but the 1st)
- `some_list[:2]`: Returns all elements up-to and **exclusding** index = 2

#### Array Methods

|Method|Description|Example
|---|---|---
|[`.append()`](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)|Adds an element to the end of the list|`[1,2,3].append(4) == [1,2,3,4]`
|[`.extend()`](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)|Extends a list by adding another list to the end of it|`[1,2,3].extend([4,5,6]) == [1,2,3,4,5,6]`
|[`.index()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)|Returns the index of an element in the list|`['a', 'b', 'c'].index('b') == 1`

## Control-Flow

### `if` to branch out
``` py
if (condition):
    #
    # Do this block
    #

elif (some_other_condition):
    #
    # Do this block instead
    #

else:
    #
    # Catch-all block
    #

```

### `for` to iterate

- Iterating a list: `for ele in ["this", "is", "a", "list"]:`
- Iterating a string: `for char in "Hello World":`
- Iterating a range: `for ii in range(0, 10):`
- Iterating a range with larger step sizes: `for ii in range(0, 10, 2):`
- Iterating two lists at once: `for aa, bb in zip(listA, listB):`
- Iterating with a counter: `for idx, ele in enumerate(["a", "b", "c"]):`


### `continue` and `break`

``` py
print("The Windows Versions:")
for ii in range(7,200):

    if (ii == 9):
        continue

    if (ii > 10):
        break

    print(f"\tWindows {ii}")
```