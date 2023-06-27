# PyGrid

A simple library to quickly create tables with Python.

## Examples

Basic example using the built in theme.

```python
from PyGrid import makeGird

users = [
    ("Username", "Display Name")
    ("Melissa-537", "Melissa S. G.")
    ("Greg5", "gregFIVE")
    ("PopSoda50", "Popsoda")
]

print("Output:")
print(makeGird(users))

# Output:
# Username    | Display Name
# ---------------------------
# Melissa-537 | Melissa S. G.
# Greg5       | gregFIVE
# PopSoda50   | Popsoda
```
