## 🧺 Lists in Python

A **list** is a built-in Python data structure used to store a collection of items. Think of it like a hippo’s lunchbox 🦛—it might contain apples, carrots, and sweet potatoes all in one tidy container.

### ✅ Why Lists Matter

- Store multiple related values in a single variable
- Access, modify, or remove individual items
- Iterate over them using loops
- Useful for nutrition data, e.g. daily intakes, meal components

---

### 🛠️ Creating and Accessing Lists

```python
# A list of daily calcium intakes (mg) for different hippos
calcium_intakes = [1200, 1150, 1250]

# Accessing elements (index starts at 0)
print(calcium_intakes[0])   # First element
print(calcium_intakes[-1])  # Last element
```

---

### 🧮 List Operations

```python
# Built-in operations
print(len(calcium_intakes))       # Number of items
print(sum(calcium_intakes))       # Total calcium intake
print(max(calcium_intakes))       # Highest value

# Add and update
calcium_intakes.append(1180)      # Add new intake to the end
calcium_intakes[1] = 1190         # Update second value

# Remove
calcium_intakes.remove(1250)      # Remove specific value
```

---

<details>
<summary>💡 Advanced Tip: Lists Can Store Anything</summary>

Lists can hold different types of values—even other lists!

```python
mixed_list = ['apple', 3.5, True, [1, 2, 3]]
```

</details>

---

## 🧪 Exercise: List Practice

Create a list of iron intakes for three hippos (e.g. `8.2`, `7.9`, `8.5`). Then:

- Print the full list
- Access the second value and print it
- Add one more value to the list
- Calculate and print the average

💬 *Add comments to explain what each line does.*

```python
# Your code here
```

✏️ Want help with the average? Try:  
```python
average = sum(your_list) / len(your_list)
```
