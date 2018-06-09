#dictionary{"key":value}  pairs

#information of profile
information={"name":"csk","age":56,"city":"bangalore","area":"btm"}
print(information)
#accessing the value of dictionary

print(information["name"])
print(information["age"])
print(information["city"])
print(information["area"])

#assignment:['clear','keys','pop','popitem','copy','fromkeys]
print(information.items())
print(information.keys())
print(information.values())
for value,key in information.items():
    print(value,key)
