"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import json

Jill={"name":"Jill",
      "age":26,
      "Job":"Biologist",
      "Relation":{"Zalika":"friend", "John":"partner"}
      }

Zalika={"name":"Zalika",
        "age":28,
        "Job":"artist",
        "Relation":{"Jill":"friend", "Nash":"renter"}
        }

John={"name":"John",
      "age":27,
      "Job":"writer",
      "Relation":{"Jill":"partner","Nash":"uncle"}
      }

Nash={"name":"Nash",
      "age":34,
      "Job":"chef",
      "Relation":{"John":"cousin","Zalika":"landlord"}
      }


def forget(person1,person2):
    del person1['Relation'][person2['name']]
    del person2['Relation'][person1['name']]


def add_person(name,age,job,relations):
    person = {"name":name, "age":age, "Job":job,"Relation":relations}
    return person


def average_age(group):
    total_age=0
    total_person=0
    for i in group:
        total_age += i['age']
        total_person +=1
    
    return total_age / total_person



my_group =[]
my_group.append(Jill)
my_group.append(Zalika)
my_group.append(John)
my_group.append(Nash)

#forget(Jill,Zalika)
#print(Jill)
#print(Zalika)

Dokolo = add_person("Dokolo", 24, "student", {})
my_group.append(Dokolo)
#print(Dokolo)

#print(average_age(my_group))

def max_age(group_list):
    max_age=0
    for i in group_list:
        if i["age"] >= max_age:
            max_age = i["age"]
    
    return max_age
#print(max_age(my_group))

def mean_relation(group_list):
    total_relation=0
    total_person=0
    for i in group_list:
        total_relation += len(i['Relation'])
        total_person +=1
    
    return total_relation / total_person
#print(mean_relation(my_group))

def max_age_relation(group_list):
    max_age=0
    max_name=""
    for i in group_list:
        if len(i["Relation"]) >= 1:
            if i["age"] >= max_age:
                max_age = i["age"]
                max_name = i["name"]
    return (max_age, max_name)
#print(max_age_relation(my_group))

def max_age_name(group_list):
    max_age=0
    max_name=""
    for i in group_list:
        #print(i["Relation"])
        if "friend" in i["Relation"].values():
            if i["age"] >= max_age:
                max_age = i["age"]
                max_name = i["name"]
    return (max_age, max_name)
#print(max_age_name(my_group))


######################################################################################################

#week4 exercise1
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


#write
with open("group.json", "w") as group_file:
    json.dump(group, group_file)

#read
read_group = {}
with open("group.json", "r") as group_file:
    read_group = json.load(group_file)



