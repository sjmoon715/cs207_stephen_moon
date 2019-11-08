class AutoDiffToy():
    def __init__(self, a, der=1):
        self.a = float(a)
        self.val = a
        self.der = der
    def __add__(self, other):
        # Checks whether other has a val attribute
        try:
            new_toy = AutoDiffToy(self.val + other.val, self.der + other.der)
            return new_toy
        # If other is not an object, perform the addition    
        except AttributeError:
            try:
                new_val = self.val + other
                new_toy = AutoDiffToy(new_val, self.der)
                return new_toy
            except TypeError:
                raise TypeError ("Invalid Type")
    def __radd__(self, other):
        # Checks whether other has a val attribute
        try:
            new_toy = AutoDiffToy(self.val + other.val, self.der + other.der)
            return new_toy
        # If other is not an object, perform the addition
        except AttributeError:
            try:
                new_val = self.val + other
                new_toy = AutoDiffToy(new_val, self.der)
                return new_toy
            except TypeError:
                raise TypeError("Invalid Type")
    def __mul__(self, other):
        # Checks whether other has a val attribute
        try:
            new_val = self.val * other.val
            new_toy = AutoDiffToy(new_val, self.val*other.der + self.der*other.val)
            return new_toy
        # If other is not an object, perform the multiplication    
        except AttributeError:
            try:
                new_val = self.val * other
                new_toy = AutoDiffToy(new_val, other)
                return new_toy
            except TypeError:
                raise TypeError("Invalid Type")
    def __rmul__(self, other):
        # Checks whether other has a val attribute
        try:
            new_val = self.val * other.val
            new_toy = AutoDiffToy(new_val, self.val*other.der + self.der*other.val)
            return new_toy
        # If other is not an object, perform the multiplication
        except AttributeError:
            try:
                new_val = self.val * other
                new_toy = AutoDiffToy(new_val, other)
                return new_toy
            except TypeError:
                raise TypeError("Invalid Type")

# Test 1
a = 2.0
x = AutoDiffToy(a)
alpha = 3.0
beta = 2.0
f = alpha * x + beta
print (f.val, f.der)

# Test 2
a = 2.0
x = AutoDiffToy(a)
alpha = 3.0
beta = 2.0
f = x * alpha + beta
print (f.val, f.der)

# Test 3
a = 2.0
x = AutoDiffToy(a)
alpha = 3.0
beta = 2.0
f = beta + alpha * x
print (f.val, f.der)

# Test 4
a = 2.0
x = AutoDiffToy(a)
alpha = 3.0
beta = 2.0
f = beta + x * alpha
print (f.val, f.der)

# Test 5 - two objects multiplied by each other
a = 2.0
alpha = 3.0
beta = 2.0
x = AutoDiffToy(a)
y = AutoDiffToy(a)
f = x*y
print(f.val,f.der)