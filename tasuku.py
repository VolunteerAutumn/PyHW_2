# PART I
# ----1
text = input("Enter the text > ")
sentence_count = text.count('.') + text.count('?') + text.count('!')
print(f"Number of sentences: {sentence_count}")

# ----2
s = input("Enter the string > ")
sc = ""

for char in s:
	if char != " ":
		sc += char
srev = ''.join(reversed(sc))
if sc.lower() == srev.lower():
	print("The string is a palindrome!")
else:
	print("The string is NOT a palindrome!")

# ----3
rw = ["apple", "steampunk", "miku", "python", "i", "love", "pokemon", "they", "are", "adorable"]

t = input("Enter the text > ")
ts = t.lower().split()

for i in range(len(ts)):
    if ts[i] in rw:
        ts[i] = ts[i].upper()

print(' '.join(ts))


# ----4
s_tr = input("Enter the string > ")
s1, s2 = input("Enter the symbols SEPARATELY > ").split()

s_tr_p = s_tr.replace(s_tr[s_tr.index(s1):s_tr.index(s2)+1], "")
print(s_tr_p)

# ----5
text = input("Enter the text > ")
symbols = input("Please enter the symbols that the words you want to delete contain > ").split()
lotw = text.split()
textres = []

for word in lotw:
	for symbol in symbols:
		if symbol not in word:
			textres.append(word)

print(' '.join(textres))

# ----6
text = input("Enter a text > ").split()
txet = []

for word in reversed(text):
	txet.append(word)

print(' '.join(txet))

# PART II (!!! IMPORTANT - I did everything as it was easier for me (I'm lazy af))
# ----1
nl = map(int, input("Enter the numbers separated with spaces (\" \") > ").split())
en = 0
on = 0

for i in nl:
	if i % 2 == 0:
		en += 1
	elif i % 2 != 0:
		on += 1

print(f"There are {en} even numbers and {on} odd numbers")

# ----2
nl = list(map(int, input("Enter the numbers separated with spaces (\" \") > ").split()))
print(f"The biggest one is {max(nl)} and the smallest one is {min(nl)}")

# ----3
import random as r
nl = []
min_pos = 100
max_neg = -100
zeros = 0
for i in range(0, r.randint(8, 15)):
	nl.append(r.randint(-100, 100))
print(f"We have a list: {nl}")
for number in nl:
	if number < 0:
		if number > max_neg:
			max_neg = number
	elif number > 0:
		if number < min_pos:
			min_pos = number
	elif number == 0:
		zeros += 1
print(f"In this list, {min_pos} is the smallest positive number, {max_neg} is the largest negative number.")
print(f"The list has {zeros} zeros.")

# ----4
nums = list(map(int, input("Enter all the numbers of the list you want to create > ").split()))
c = int(input("Enter a coefficient > "))
filtered_nums = []
for i in nums:
    if i >= c:
        filtered_nums.append(i)
print(f"The result is: {' '.join(map(str, filtered_nums))}")

# ----5
kkk = input("Enter the equation (ex. 23+12) > ")
print(f"Result of {kkk} is {int(eval(kkk))}")

# ----6
starting_list = list(map(int, input("Enter the numbers of the list (separate with ' ') > ").split()))
filler_list = []
result = []
filler_number_index = 0

for i in starting_list:
	if i >= 0:
		filler_list.append(i)

filler_list.sort()

for num in starting_list:
	if num < 0:
		result.append(num)
	else:
		result.append(filler_list[filler_number_index])
		filler_number_index += 1
print(f"Result: {', '.join(map(str, result))}")

