with open("./english_alphabet_freq.txt", "r") as file:
    lines = file.readlines()

freq = {}
mods = {}
for line in lines:
    pieces = line.split()
    freq[pieces[0]] = pieces[1]
    mods[pieces[0]] = pieces[2]

reverse_mods = {v: k for k, v in mods.items()}


def sort_desc(dct):
    return dict(sorted(dct.items(), reverse=True, key=lambda item: item[1]))

sorted_freq = sort_desc(freq)

def print_freq(freq):
    for k, v in freq.items():
        print(f'{k}: {v}')

def get_freq_pcts(encoded):
    counts = {}
    for char in encoded:
        if char != ' ' and char != '\n':
            counts[char] = counts.setdefault(char, 0) + 1

    total_chars = sum(counts.values())

    cipher_freqs = {}
    for k, v in counts.items():
        cipher_freqs[k] = round((v / total_chars), 4)

    return sort_desc(cipher_freqs)

def decode(freq, message_file):
    with open(message_file, "r") as file:
        encoded = file.read()

    get_freq_pcs(encoded)

    # for k, v in sorted_cipher_freqs.items():
    #     print(f'{k}: {v}')

    sorted_english_keys = list(sorted_freq.keys())
    sorted_cipher_keys = list(sorted_cipher_freqs.keys())
    subs = {}
    for i in range(len(sorted_cipher_keys)):
        subs[sorted_cipher_keys[i]] = sorted_english_keys[i]

    subs_manual = {
        'r': 'E', 'b': 'T', 'm': 'A', 'k': 'N', 'j': 'O',
        'w': 'I', 'i': 'S', 'p': 'H', 'u': 'R', 'd': 'D',
        'h': 'L', 'v': 'C', 'x': 'F', 'y': 'M', 'n': 'U',
        's': 'P', 't': 'Y', 'l': 'B', 'q': 'K', 'o': 'G',
        'e': 'V', 'a': 'X', 'c': 'W', 'f': 'Q', 'g': 'Z'
    }

    decoded = ''
    for char in encoded:
        if char != ' ' and char != '\n':
            # decoded += subs[char]
            decoded += subs_manual[char]
        else:
            decoded += char
    # print("Sorted English:")
    # print(sorted_freq.keys())
    # print(subs)
    print(decoded)

decode(freq, "encoded_msg.txt")
