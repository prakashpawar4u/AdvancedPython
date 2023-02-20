import yaml

#with open(r'fruits.yaml') as file:
with open(r'categories.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(fruits_list)
    for key, val in fruits_list.items():
        print(key, ":",  val)
#{'apples': 20, 'mangoes': 2, 'bananas': 3, 'grapes': 100, 'pineapples': 1}
#{'sports': ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis'], 'countries': ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}


import yaml

with open(r'categories.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)

#write file:

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(r'store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)