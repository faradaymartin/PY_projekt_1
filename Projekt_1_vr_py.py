"""
projekt_1.ipynb: první projekt do Engeto Online Python Akademie

author: Martin Faraday
email: faradaymartin@gmail.com
discord: martinfaraday_19641
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatel = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

login = input("Vlož Tvůj login:")
password = input("Vlož heslo:")

if login in uzivatel and password == uzivatel[login]:
    print(f'username: {login}\npassword: {password}')
    print("-" * 43)
    print(f'Welcome to the app, {login}\nWe have 3 texts to be analyzed.')
    print("-" * 43)
else:
    print("unregistered user, terminating the program..")



def analyze_text(text):
    words = text.split()
    word_count = len(words)
    capitalized_words = sum(1 for word in words if word[0].isupper())
    uppercase_words = sum(1 for word in words if word.isupper())
    lowercase_words = sum(1 for word in words if word.islower())
    numbers = [int(word) for word in words if word.isdigit()]
    number_count = len(numbers)
    number_sum = sum(numbers)
    
    word_lengths = [len(word) for word in words]
    length_freq = {length: word_lengths.count(length) for length in set(word_lengths)}
    
    return {
        "There are words in the selected text": word_count,
        "There are titlecase words": capitalized_words,
        "There are uppercase words": uppercase_words,
        "There are lowercase words": lowercase_words,
        "There are numeric strings": number_count,
        "The sum of all the numbers is": number_sum,
        "Word length frequencies": length_freq
    }

vyber = int(input("Enter a number between 1 and 3 to select:"))
print("-" * 43)

if vyber in range(1, 4):
    vybrany_text = TEXTS[vyber - 1]
    analysis = analyze_text(vybrany_text)
    for key, value in analysis.items():
        if key == "Word length frequencies":
            print("-" * 43)
            print("LEN | OCCURRENCES      | NR.")
            print("-" * 43)
            max_freq = max(value.values())
            for length, freq in sorted(value.items()):
                print(f'{length:3} | {"*" * freq:<{max_freq}} | {freq}')
        else:
            print(f'{key}: {value}')
else:
    print("Invalid choice, choose a number between 1 and 3")

print("-" * 43)
