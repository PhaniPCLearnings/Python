dict_1={
    "name_1":"Phani",
    "name_2":"Cherry"
}

print(dict_1)

print(dict_1["name_1"])


#print(dict_1[name_1]) -- This will give us the name error

#print(dict_1["name_3"]) -- This will give us the key error

#empty Dictionary
dict_2={}

dict_2[1]="Phani"
dict_2["Location"]="Ongole"

print(dict_2)
print(dict_2[1])

#we can use the empty dictionary to wipe off the data

dict_nest={
    'Name':"Phani",
    'Places':["Ongole","Hyderabad","Guntur"]
}

print(dict_nest)
print(dict_nest['Places'][2])

dict_nested={
    'place':'Ongole',
    'Area':[["MM Road","Gandhi Road"],["Pernametta","Bhagya Nagar"]]
}

print(dict_nested)

print(dict_nested['Area'][0][1])


travel_log={
    "Ongole":{
        "Places_Visited":["MM Road","Gandhi Road"],
        "total_Visits":11
    },
    "Guntur":{
        "Places_Visited":"Gorantla",
        "total_Visits":12
    }
}

print(travel_log["Ongole"]["Places_Visited"][0])


dict_ke={
    "a":1,
    "b":2,
    "c":3
}

for key in dict_ke:
    dict_ke[key]+=1

print(dict_ke)