# !!! PART 2 !!!
# ----1
a = None
l = []

while not a == "e":
    a = input("Enter the number you want to add to the list > ")
    if a.isdigit():
        l.append(int(a))
    elif a == "e":
        break
    else:
        print("Please enter a number.")

print(f"Largest of them is {max(l)}")
print(f"Average of these is approximately {sum(l)//len(l)}")

# ----2
a = None
l = []


while not a == "e":
    a = input("Enter the number you want to add to the list > ")
    if a.isdigit():
        l.append(a)
    elif a == "e":
        break
    else:
        print("Please enter a number.")

n = input("What number do you want to look for? > ")
s = ''.join(l)
print(f"There are {s.count(n)} {n}'s in the list.")

# ----3

