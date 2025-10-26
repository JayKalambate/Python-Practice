# Creating a Dictionary
Student = {"name": "Jay",
           "age": 22,
           "Course":"Data_Science"}
print(Student)

# Accessing Dictionary elements
print(Student["name"])
print(Student["age"])

# Adding & Updating elements
Student["grade"] = "A"
Student["age"] = 23
print(Student)

# Removing elements
Student.pop("grade")
print(Student)