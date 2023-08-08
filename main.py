

def read_letter():
    with open('./Input/Letters/starting_letter.txt') as file:
        letter_content = file.read()
        return letter_content







def read_invitees():
    with open('./Input/Names/invited_names.txt') as invitees:
        invitees_list = invitees.readlines()
        invitees = []
        for invitee in invitees_list:
            invitees.append(invitee.strip())

        return invitees


def save_letter(filename, body):
    with open(f"./Output/ReadyToSend/letter_for_{filename}.txt", mode='w')as file:
        file.writelines(body)
def create_letter():

    for invitee in read_invitees():

        body = read_letter()
       # greeting = read_letter()[0]
        updated_body = body.replace('[name]', invitee)
        print(updated_body)
        save_letter(invitee, updated_body)


create_letter()



#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp