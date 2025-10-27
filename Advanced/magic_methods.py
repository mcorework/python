"""
# ✨ Magic (Dunder : Double Underscore) Methods in Python — Overview

## 📘 Introduction
**Magic methods**, also called **dunder methods** (short for *double underscore*), 
are special methods in Python that start and end with double underscores — like `__init__`, `__str__`, `__add__`, etc.

They are automatically invoked by Python in specific situations and 
allow classes to behave like built-in types (e.g., support `+`, `<`, `==`, or string representation).

---

## 🧩 Common Magic Methods

| Method | Purpose | Example Usage |
|--------|----------|----------------|
| `__init__` | Constructor — initializes an object | `obj = MyClass()` |
| `__str__` | String representation (used by `print()`) | `print(obj)` |
| `__repr__` | Developer representation | `repr(obj)` |
| `__add__` | Define addition `+` | `obj1 + obj2` |
| `__len__` | Define behavior for `len(obj)` | `len(obj)` |
| `__eq__` | Equality comparison | `obj1 == obj2` |
| `__lt__` | Less-than comparison | `obj1 < obj2` |
| `__getitem__` | Index access | `obj[key]` |
| `__setitem__` | Assign to key/index | `obj[key] = value` |
| `__delitem__` | Delete item | `del obj[key]` |
| `__call__` | Make instance callable | `obj()` |
| `__enter__`, `__exit__` | Context manager | `with obj:` |
| `__iter__`, `__next__` | Make object iterable | `for x in obj:` |

---

## 🧠 Example: Implementing Common Magic Methods
"""

"""
# ✨ Magic (Dunder) Methods in Python — Complete Reference

## 📘 Introduction
**Magic methods** (also called **dunder methods**, short for *double underscore*) are special functions
that Python automatically invokes in certain situations.  
They make classes behave like built-in types — for example, allowing custom objects to:
- Be printed (`__str__`)
- Compared (`__eq__`, `__lt__`)
- Added (`__add__`)
- Iterated (`__iter__`)
- Used in context managers (`__enter__`, `__exit__`)

These methods start and end with double underscores (e.g., `__init__`, `__str__`, etc.).

---

## 🧩 Categories of Magic Methods
1. **Initialization and Object Creation** → `__new__`, `__init__`, `__del__`
2. **String Representation** → `__str__`, `__repr__`
3. **Comparison Operators** → `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`
4. **Arithmetic Operators** → `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, etc.
5. **Unary Operators** → `__neg__`, `__pos__`, `__abs__`
6. **Container Methods** → `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
7. **Iteration** → `__iter__`, `__next__`
8. **Callable Objects** → `__call__`
9. **Context Managers** → `__enter__`, `__exit__`
10. **Attribute Access** → `__getattr__`, `__setattr__`, `__delattr__`
11. **Object Representation and Copying** → `__copy__`, `__deepcopy__`

---

Note:
    (1) Everything in Python is an object.
"""
import copy

class MagicExample:
    """Demonstrates common Python magic methods."""

    # ===============================================================
    # 🧱 1. Object Creation & Initialization
    # ===============================================================
    def __new__(cls, *args, **kwargs):
        """Called before __init__, allocates memory for a new object."""
        instance = super().__new__(cls)
        print(f"__new__ called: Creating instance of {cls.__name__}")
        return instance

    def __init__(self, name, value):
        """Initializes object attributes."""
        print("__init__ called: Initializing instance")
        self.name = name
        self.value = value

    def __del__(self):
        """Destructor — called when object is deleted."""
        print(f"__del__ called: {self.name} is being destroyed")

    # ===============================================================
    # 🧾 2. String Representation
    # ===============================================================
    def __str__(self):
        """User-friendly string representation (used by print)."""
        return f"MagicExample(name={self.name}, value={self.value})"

    def __repr__(self):
        """Developer-oriented representation."""
        return f"MagicExample('{self.name}', {self.value})"

    # ===============================================================
    # 🔢 3. Arithmetic Operators
    # ===============================================================
    def __add__(self, other):
        """Defines addition using + operator."""
        if isinstance(other, MagicExample):
            return MagicExample(self.name + "&" + other.name, self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        """Defines subtraction using - operator."""
        if isinstance(other, MagicExample):
            return MagicExample(self.name + "-" + other.name, self.value - other.value)
        return NotImplemented

    def __mul__(self, other):
        """Defines multiplication using * operator."""
        if isinstance(other, int):
            return MagicExample(self.name * other, self.value * other)
        return NotImplemented

    def __truediv__(self, other):
        """Defines division using / operator."""
        if isinstance(other, (int, float)):
            return MagicExample(self.name, self.value / other)
        return NotImplemented

    # ===============================================================
    # ⚖️ 4. Comparison Operators
    # ===============================================================
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    # ===============================================================
    # 🎯 5. Unary Operators
    # ===============================================================
    def __neg__(self):
        """Defines negation (-obj)."""
        return MagicExample(self.name, -self.value)

    def __abs__(self):
        """Defines abs(obj)."""
        return abs(self.value)

    # ===============================================================
    # 📦 6. Container Behavior
    # ===============================================================
    def __len__(self):
        """Return a 'length' based on value for demo."""
        return len(self.name)

    def __getitem__(self, index):
        """Allows index access."""
        return self.name[index]

    def __setitem__(self, index, char):
        """Allows character modification."""
        temp = list(self.name)
        temp[index] = char
        self.name = ''.join(temp)

    def __contains__(self, item):
        """Checks membership with 'in' keyword."""
        return item in self.name

    # ===============================================================
    # 🔁 7. Iteration
    # ===============================================================
    def __iter__(self):
        """Returns iterator over the name characters."""
        self._index = 0
        return self

    def __next__(self):
        """Returns next element for iteration."""
        if self._index < len(self.name):
            result = self.name[self._index]
            self._index += 1
            return result
        raise StopIteration

    # ===============================================================
    # ☎️ 8. Callable Objects
    # ===============================================================
    def __call__(self, multiplier):
        """Allows object to be called like a function."""
        print(f"__call__ invoked — multiplying {self.value} by {multiplier}")
        return self.value * multiplier

    # ===============================================================
    # 🧩 9. Context Managers
    # ===============================================================
    def __enter__(self):
        print("__enter__ called — opening resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called — closing resource")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return True  # Suppress exception

str1 = "Hello"
str2 = "World"
str3 = str1+str2
str4 = str1.__add__(str1)

# ===============================================================
# 🧪 Example Usage of All Magic Methods
# ===============================================================
if __name__ == "__main__":
    print("\n--- Object Creation ---")
    obj1 = MagicExample("Alpha", 10)
    obj2 = MagicExample("Beta", 5)

    print("\n--- String Representations ---")
    print(str(obj1))
    print(repr(obj2))

    print("\n--- Arithmetic Operations ---")
    print(obj1 + obj2)
    print(obj1 - obj2)
    print(obj1 * 2)
    print(obj1 / 2)

    print("\n--- Comparison Operators ---")
    print(obj1 == obj2)
    print(obj1 > obj2)
    print(obj1 < obj2)

    print("\n--- Unary Operators ---")
    print(-obj2)
    print(abs(obj1))

    print("\n--- Container Behavior ---")
    print(len(obj1))
    print(obj1[1])
    obj1[1] = "Z"
    print(obj1.name)
    print("Z" in obj1)

    print("\n--- Iteration ---")
    for char in obj2:
        print(char, end=" ")

    print("\n\n--- Callable Object ---")
    print(obj1(3))

    print("\n--- Context Manager ---")
    with MagicExample("Gamma", 42) as m:
        print("Inside with block:", m)

    print("\n--- Object Copy ---")
    obj3 = copy.copy(obj1)
    print("Copied object:", obj3)

    print("\n--- Deleting Object ---")
    del obj2
