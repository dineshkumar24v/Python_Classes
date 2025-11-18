
'''DECORATORS :  we generally use decorators to add some more functionalities to an existing function '''

def example_decorator(func):
    def wrapper():
       print("check cartridge and A4 sheets")
       func()
       print("System is going to sleep mode")

    return wrapper

@example_decorator
def printer():
  print("Hi, Printing in progress")
  print("Completed, Bye")


printer()


### Explanation:
# 1. **Decorator Function (`example_decorator`)**:
#    - This is a higher-order function that takes a function (`func`) as an argument.
#    - The `wrapper` function inside it adds extra behavior before and after calling the original function (`func`).

# 2. **Applying the Decorator**:
#    - The `@example_decorator` syntax applies the decorator to the `printer` function.
#    - The `printer` function is effectively replaced by the `wrapper` function, which adds the additional print statements.

# 3. **Function Call (`printer()`)**:
#    - When you call `printer()`, it executes the `wrapper` function.
#    - The output includes the preparatory step ("check cartridge and A4 sheets"), the original function's behavior (printing in progress and completion), and the concluding step ("System is going to sleep mode").

# This pattern is super useful when you want to add reusable functionality—like logging, authentication checks, or setup tasks—without modifying the original function's code. 



# Let's dive deeper into decorators with more practical examples! Decorators can be especially useful in scenarios where you want to add functionality without altering the original function. Here are a few examples:

# ### 1. **Logging Decorator**
# This decorator logs the execution of a function:


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Siddu")

# **Output:**

# Calling function: greet
# Hello, Siddu!
# Function greet executed successfully




### 2. **Authentication Check**
# Imagine you're building a web app and need to verify a user before running certain functions.

def auth_decorator(func):
    def wrapper(user_role):
        if user_role == "admin":
            func(user_role)
        else:
            print("Access Denied: Insufficient Permissions")
    return wrapper

@auth_decorator
def access_admin_panel(user_role):
    print(f"Welcome to Admin Panel, {user_role}.")

access_admin_panel("admin")
access_admin_panel("guest")

# **Output:**

# Welcome to Admin Panel, admin.
# Access Denied: Insufficient Permissions




### 3. **Performance Timer**
# Measure the time taken by a function to execute:

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def heavy_computation():
    for _ in range(10**6):
        pass

heavy_computation()

# **Output:**

# Execution Time: X.XX seconds

