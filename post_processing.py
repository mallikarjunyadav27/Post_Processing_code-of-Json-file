import json
with open(r'C:\Users\Lenovo\Downloads\input format1.json') as f:
    data = json.load(f)
output =[]
for i in data:
    j = list(i.values())[0]
    new_dict ={}
    for k in j:
        if k["entity_name"] in new_dict:
            new_dict[k["entity_name"]] = new_dict[k["entity_name"]]+ [k["text"]]
        else:
            new_dict[k["entity_name"]] = [k["text"]]
    output.append({list(i.keys())[0]:new_dict})
print(output)











