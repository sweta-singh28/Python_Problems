info = {
    "name" : "sweta",
    "age" : 19,
    "cgpa" : 8.3,
    "state" : "odisha",
    "lang" : ["python", "c", "cpp", "javascript"],
    "topic" : ("typle", "sets", "dict"),
    34 : 45
}
print(info)
print(info.keys())   #returns all keys 
print(info.values())  #returns all teh values in the dict
print(info.items())    #returns all the keys and values in the dict
info.update({"city" : "odisha"})
print(info)

print(info.get("name"))  #retuns the value of the key