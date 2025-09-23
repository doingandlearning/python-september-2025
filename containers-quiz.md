# Python Lists and Dictionaries Quiz

## Question 1: List Creation
What is the correct way to create an empty list in Python?

A) `empty_list = ()`  
B) `empty_list = []`  
C) `empty_list = {}`  
D) `empty_list = list()`  

**Answer: B and D** - Both `[]` and `list()` create empty lists.

---

## Question 2: List Indexing
Given the list `beatles = ["John", "Paul", "George", "Ringo"]`, what does `beatles[1]` return?

A) "John"  
B) "Paul"  
C) "George"  
D) "Ringo"  

**Answer: B** - List indexing starts at 0, so index 1 is "Paul".

---

## Question 3: List Methods
Which method adds a single element to the end of a list?

A) `extend()`  
B) `append()`  
C) `insert()`  
D) `add()`  

**Answer: B** - `append()` adds one element to the end of the list.

---

## Question 4: List vs Extend
What's the difference between `append()` and `extend()`?

A) They do the same thing  
B) `append()` adds one element, `extend()` adds multiple elements  
C) `extend()` adds one element, `append()` adds multiple elements  
D) `append()` only works with strings  

**Answer: B** - `append()` adds a single element, `extend()` adds multiple elements from an iterable.

---

## Question 5: List Removal
Which method safely removes all occurrences of a value from a list?

A) `remove()` in a while loop  
B) `delete()`  
C) `clear()`  
D) `pop()`  

**Answer: A** - Using `remove()` in a while loop safely removes all occurrences.

---

## Question 6: List Operations
What does `pop()` return and do to the list?

A) Returns the first element and removes it  
B) Returns the last element and removes it  
C) Returns the last element but keeps it in the list  
D) Returns the list length  

**Answer: B** - `pop()` returns and removes the last element (LIFO - Last In, First Out).

---

## Question 7: Dictionary Creation
What is the correct way to create an empty dictionary?

A) `empty_dict = []`  
B) `empty_dict = ()`  
C) `empty_dict = {}`  
D) `empty_dict = dict()`  

**Answer: C and D** - Both `{}` and `dict()` create empty dictionaries.

---

## Question 8: Dictionary Access
Given `user_dict = {"name": "Jemima", "team": "Infosec"}`, how do you access the value "Jemima"?

A) `user_dict[0]`  
B) `user_dict["name"]`  
C) `user_dict.name`  
D) `user_dict.get("name")`  

**Answer: B and D** - Both `user_dict["name"]` and `user_dict.get("name")` access the value, but `get()` is safer.

---

## Question 9: Dictionary Membership
What does `"London" in user_dict` check?

A) If "London" is a key in the dictionary  
B) If "London" is a value in the dictionary  
C) If "London" is both a key and value  
D) If the dictionary contains the string "London" anywhere  

**Answer: A** - The `in` operator checks keys, not values, in dictionaries.

---

## Question 10: Dictionary Methods
Which method returns a list of tuples containing (key, value) pairs?

A) `keys()`  
B) `values()`  
C) `items()`  
D) `pairs()`  

**Answer: C** - `items()` returns a list of tuples with (key, value) pairs.

---

## Question 11: Dictionary Modification
How do you add a new key-value pair to a dictionary?

A) `dict.add(key, value)`  
B) `dict[key] = value`  
C) `dict.insert(key, value)`  
D) `dict.append(key, value)`  

**Answer: B** - Use `dict[key] = value` to add or update key-value pairs.

---

## Question 12: Dictionary Deletion
How do you remove a key-value pair from a dictionary?

A) `dict.remove(key)`  
B) `del dict[key]`  
C) `dict.delete(key)`  
D) `dict.pop(key)`  

**Answer: B and D** - Both `del dict[key]` and `dict.pop(key)` remove key-value pairs.

---

## Question 13: Nested Data Structures
Given `bands = {"Queen": {"singer": "Freddie Mercury"}}`, how do you access "Freddie Mercury"?

A) `bands["Queen"][0]`  
B) `bands["Queen"]["singer"]`  
C) `bands[0]["singer"]`  
D) `bands.Queen.singer`  

**Answer: B** - Use chained square brackets to access nested dictionary values.

---

## Question 14: List Copying
What's the difference between `list1 = list2` and `list1 = list2.copy()`?

A) No difference  
B) First creates a reference, second creates a copy  
C) First creates a copy, second creates a reference  
D) Both create copies  

**Answer: B** - Assignment creates a reference (both variables point to same list), `copy()` creates a separate list.

---

## Question 15: Data Type Identification
What data type do these brackets represent: `()`, `[]`, `{}`?

A) Tuple, List, Dictionary  
B) List, Tuple, Dictionary  
C) Dictionary, List, Tuple  
D) Tuple, Dictionary, List  

**Answer: A** - `()` for tuples, `[]` for lists, `{}` for dictionaries.

---

## Bonus Question: Complex Nesting
Given `ditto["abilities"][0]["ability"]["name"]`, what data structure is `ditto`?

A) A list of dictionaries  
B) A dictionary containing a list of dictionaries  
C) A tuple of lists  
D) A dictionary of tuples  

**Answer: B** - `ditto` is a dictionary with an "abilities" key containing a list of dictionaries.
