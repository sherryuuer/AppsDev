# TODO: Create a letter using starting_letter.txt 
with open("MailMergeProject/Input/Letters/starting_letter.txt") as f:
    contents = f.read()


# for each name in invited_names.txt
with open("MailMergeProject/Input/Names/invited_names.txt") as f:
    names = f.readlines()

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for name in names:
    name = name.strip()
    letter = contents.replace("[name]", name)
    with open(f"MailMergeProject/Output/ReadyToSend/send_to_{name}.txt", mode="w") as file:
        file.write(letter)
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
