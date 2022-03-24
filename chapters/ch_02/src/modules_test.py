# %%
# How to import a Module
# This and the module fibo should be in the same directory
import fibo 

fibo.fib(3)

# %%
# DO NOT DO THIS!! EVER!!!
from fibo import *

fib(3)

# %%
# Import only what youneed from the module
from fibo import fib, fib2

fib(3)

# %%
# You could alias the method to avoid colissions
from fibo import fib as fibonacci
fibonacci(3)

# %%
# In case you have another module with the same function name you 
# could import both and alias one of them
from fibo import fibonacci
from david import fib

fibonacci(3)
fib(3)

# %%
# You could also import only the module and this will also disambiguate
import fibo
import david

david.fib(3)
fibo.fib(3)