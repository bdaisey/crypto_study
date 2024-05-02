with open("./english_alphabet_freq.txt", "r") as file:
    lines = file.readlines()

freq = {}
for line in lines:
    letter_pct = line.split()
    freq[letter_pct[0]] = letter_pct[1]

sorted_freq = dict(sorted(freq.items(), reverse=True, key=lambda item: item[1]))

def print_freq(freq):
    for k,v in freq.items():
        print(f'{k}: {v}')



