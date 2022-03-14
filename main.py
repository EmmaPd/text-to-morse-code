MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-', ' ': '       '}

message = input("Your message: ").upper()
split = list(message)

morse_code_ch_list = []

for letter in list(message):
    try:
        morse_code_ch_list.append(MORSE_CODE_DICT[letter])
    except KeyError:
        morse_code_ch_list.append(letter)

ciphered_message = "".join(morse_code_ch_list)

print(f"Your message in Morse Code: {ciphered_message}")