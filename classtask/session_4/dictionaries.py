# dictionaries

# are key value stores
# 

# dictionaries = {1: "key", 2: "value", 2: "key2", 4: "value2"}
# print(dictionaries[1])

# keys must be unique
# 

# create a dictionary of students key is the 1 ... 100



students = {
1 : {"name": "George", "last_name": "Tugs", "date_of_birth": "10-01-2000" },
2 : {"name": "David", "last_name": "Tugs", "date_of_birth": "10-02-2013" },
3 : {"name": "Bold", "last_name": "Ona", "date_of_birth":" 10-02-2014" }
}


for key, value, date in students.items():
    print(f"hello Iam {value['name']} {value['last_name']}. I was born in {value['date_of_birth']}")
    print(f"Hello I ")
    
    print(value)
    print(f"Hello my name is {key['name']} {key['last_name']}; "I was born" {key['date_of_birth']})