def introduce(name, age=18, /, city="Zurich", *, job="Student", country="Switzerland"):
    print(name, age, city, job, country)

# A useful pattern to remember is:
# required → default → / → flexible → * → keyword-only


# --------------------
# VALID EXAMPLES
# --------------------

# Uses all default values except name
introduce("Alice")

# age is positional-only
introduce("Bob", 25)

# city can be positional
introduce("Charlie", 30, "Bern")

# city can also be a keyword argument
introduce("David", 35, city="Basel")

# job and country are keyword-only
introduce("Emma", 22, job="Developer", country="Germany")


# --------------------
# INVALID EXAMPLES
# --------------------

# name is before /, so it cannot be passed as a keyword
# introduce(name="Alice")
# TypeError


# age is also before /, so it cannot be passed as a keyword
# introduce("Bob", age=25)
# TypeError


# job is after *, so it cannot be passed positionally
# introduce("Charlie", 30, "Bern", "Developer")
# TypeError


# country is also keyword-only
# introduce("Emma", 22, "Bern", country="Germany", job="Developer", "France")
# SyntaxError: positional argument follows keyword argument


# name is required, so calling the function without it is invalid
# introduce()
# TypeError: missing required positional argument


# Unknown keyword argument
# introduce("Alice", hobby="Tennis")
# TypeError: unexpected keyword argument


# The same keyword cannot be given twice
# introduce("Alice", city="Bern", city="Basel")
# SyntaxError: keyword argument repeated