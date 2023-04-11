import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Input a word to get the code for: ").upper()
    try:
        code_word = [nato_alpha[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        generate_phonetic()
    else:
        print(code_word)


generate_phonetic()
