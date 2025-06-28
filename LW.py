# !!! LABORATORY WORK !!!
# ----1
stripper = input("Enter any string --> ")
d = 0
l = 0

for i in stripper:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1

print(f"There are {d} digits and {l} letters in the string.")

# ----2
akayupik = input("Enter any string --> ")
s = input("What symbol do you want to count? > ")

count = akayupik.count(s)
print(f"There are {count} {s}'s in the string.")

# ----3 (я зробив зручним для мене способом)
stripper = input("Enter any string > ")
print(''.join(reversed(stripper)))

# ----4
stripper = input("Enter any string > ")
w = input("Word you want to look for? > ")

print(f"The word {w} repeats {stripper.count(w)}")

# ----5
stripper = input("Enter any string > ")
w = input("Word you want to look for? > ")
r = input("What do you want to replace with it? > ")

stripper = stripper.replace(w, r)
print(stripper)

# ----6
s = input("Enter any string > ")
longestword = None

print(f"The longest word here is {max(s.split(), key=len)}")
