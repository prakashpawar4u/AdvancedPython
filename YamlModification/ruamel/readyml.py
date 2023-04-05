#from ruamel.yaml.main import round_trip_load as yaml_load

import ruamel.yaml
import ruamel.yaml.util
# emp_dict= yaml_load("""
# emp:
#   - name: Prakash
#     job title: CEO
#   - name: Nisha
#     job title: CTO
# """)

# print(emp_dict)
# print(f"Type: {type(emp_dict)}")
# print("Done")

yaml = ruamel.yaml.YAML()
file_to_parse = "/Users/prax/AutomationActivities/AdvancedPython/YamlModification/ruamel/values.yaml"
with open(file_to_parse) as fp:
    yaml.preserve_quotes = True
    data = yaml.load(fp)
fp.close()

#print("data",data)
print("\nIMAGE",data['DU']['image']['repository'])
print("\nkeys",data.values())