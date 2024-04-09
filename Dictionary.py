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
print(type(info))
print(info["name"])
print(info["age"])
print(info["cgpa"])
print(info["state"])
print(info["lang"])

info["name"] = "gungun"  #cahnge the value in the dict
print(info)
info["surname"] = "singh"  #add a new value in the dict
print(info)