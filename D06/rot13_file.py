# Create a script called rot13_file.py that given a file on the command line it will replace the content with the rot13 of it of it.

user_input = input('Please enter a text to ROT13: ')
Input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
Output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

user_output = []

for letter in user_input:
    if letter in Input:
       index = Input.find(letter)
       user_output.append(Output[index])
    else:
        user_output.append(letter) 

print("Original:", user_input)
print("ROT13:   ", ''.join(user_output))

