meaningDictionary = {}
sizeDictionary = {}

meaningDictionary["apple"] = "A fruit"
sizeDictionary["apple"] = 5

meaningDictionary["cabbage"] = "A vegetable"
sizeDictionary["cabbage"] = 10

meaningDictionary["tomato"] = "Widely contested"
sizeDictionary["tomato"] = 5

print(meaningDictionary["apple"])

print(meaningDictionary)

print("What would you like to look up?")
query = input()
print("The size of " + query + " is "+ str(sizeDictionary[query]))