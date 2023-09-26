# Input function, strip delete blank space, title make upper case in first letter
name = input("What's your name? ").strip().title()
# Split function make space between names
first, last = name.split(" ")
# Function print to print parameters using F string method.
print(f"Hello, {last}!")
