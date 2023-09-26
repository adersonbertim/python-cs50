name = input("What's your name? ").strip().title()
# Split function make space between names
first, last = name.split(" ")
# Function print to print parameters using F string method.
print(f"Hello, {last}!")
