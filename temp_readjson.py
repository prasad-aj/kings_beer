import json
  
# Opening JSON file
f = open('price_data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(type(data["hot_drinks"]["Blenders_Pride"][0]))
  
# Closing file
f.close()