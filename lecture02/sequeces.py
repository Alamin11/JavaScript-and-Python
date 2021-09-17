from typing import OrderedDict, Sequence


# Mutable and Ordered
# Mutable means can be changed the Sequence
# Orderd means can not be changed the sequence because order matters
#string = oredered
name = "Farjana"
print(name[0])
print(name[6])
print(name)
#Lists=mutable and ordered
listName = ["Farjana", "Toma", "Nuntu", "Tuntun pakhi", "Jhunjhun pakhi"]
print(listName)
print(listName[0])
print(listName[1])
print(listName[2])
print(listName[3])
print(listName[4])

# Add a new name to the list:
listName.append("Ami")
print(listName[5])

# Delete a name from the list
listName.remove(listName[5])
print(listName)

# Sort the list
listName.sort()
print(listName)
