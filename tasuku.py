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

# PART II COMING TOMORROW
