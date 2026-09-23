# Using enumerate() to list
courses = ['Java', 'Python', 'Pandas', 'Sparks']
new_list = enumerate(courses)
print(list(new_list))       # Converting enumerator object into list

# Using enumerate() and for loop
for index, value in enumerate(courses):
    print(f'Index:{index}, Value:{value}')
