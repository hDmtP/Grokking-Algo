voted = {}

# value = voted.get("tom")
# print(value)

def check_voter(name):
    if voted.get(name):
        print("Kick him/her out")
    else:
        voted[name] = True
        print("Let him/her vote")

check_voter("tom")
check_voter("Javed")
check_voter("tom")
print(voted)