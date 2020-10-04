import json

configFile = open("config.json", "r")
config = json.load(configFile)

print(config["food"])
print(config["drink"])
print(config["health"])
print(config["energy"])

configFile.close




#config["food"] = 0

#configFile =  open("config.json", "w")
#json.dump(config, configFile)

#print(config["food"])
#configFile.close()

