#collection of items, mutable, not indexable,works on a pair key:value

contact_into={
    "Alma":"045777347",
    "Erin":"045444343"
}
print(contact_into)

alma_info=contact_into["Alma"]
print(alma_info)

contact_into["Orkidea"]="049888678"
contact_into["Orkidea"]="0498886782"
contact_into["orkidea"]="049888678"
del contact_into["orkidea"]
print(contact_into)
keys=contact_into.keys()
print(keys)
values=contact_into.values()
print(values)
items=contact_into.items()
print(items) #print out the key-value pair as a lists








