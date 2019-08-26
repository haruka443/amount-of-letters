wording = 'ala ma kota'
dict = {}

for letter in wording:
    if letter not in dict:
        dict[letter] = 0
    dict[letter] += 1
for letter, amount in dict.items():
    print(f'The character {letter} occured {amount} times')
