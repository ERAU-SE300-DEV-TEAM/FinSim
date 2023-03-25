from configparser import ConfigParser


config = ConfigParser()

config["Player Info"] = {
    "Current Amount": 0
}

with open("testfile.toml", "w") as f:
    config.write(f)


def openfile():
    t = open("testfile.toml")
    read = t.read()
    print(read)
    t.close()


openfile()

player = input('what is your name?')

money = int(input("Select the amount of starting money:\n1: 1,000 USD \n2: 1,500 USD \n3: 2,000 USD\n"))

print(money)
amount = 0
if money == 1:
    amount = 1000
elif money == 2:
    amount = 1500
elif money == 3:
    amount = 2000
else:
    print("error")

config = ConfigParser()

config["Player", player, "Info"] = {
    "Current Amount": amount
}

with open("testfile.toml", "w") as f:
    config.write(f)

openfile()