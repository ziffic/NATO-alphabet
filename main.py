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

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha = {row.letter:row.code for (index, row) in data.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
print(nato_alpha)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Input a word to get the code for: ")
# word_list = list(word)
code_word = [letter for letter in word]
new_list = []
for letter in code_word:
    new_list.append(nato_alpha[letter.upper()])


print(new_list)
