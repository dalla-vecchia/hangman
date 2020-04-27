board = ['''

 +---+
 |   |
     |
     |
     |
     |
========= ''', '''

 +---+
 |   |
 O   |
     |
     |
     |
========= ''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
========= ''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
========= ''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
========= ''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
========= ''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========= ''', '''

 +---+
 |   |
     |
 O   |
/|\  |
/ \  |
========= ''', '''

 +---+
 |   |
     |
     |
 O   |
/|\  |
========= ''', ''' 

 +---+
 |   |
     |
     |
 O   |
========= ''']


def playGame(cat, word):

    wordGuess = "".join(word)
    print(f"\n{len(wordGuess)} letters - Category: {cat}\n")
    
    wordGuessList = list(wordGuess)
    listOutPut = wordGuessList.copy()
    for index, character in enumerate(listOutPut):
        if not character == "  _  ":
            listOutPut[index] = "  _  "

    count = 0
    charExists = False
    while count < 11:
        
        print("\n")
        if wordGuess == str("".join(listOutPut)) and count <10:
            print(f"You Win - {wordGuess}\n")
            break

        usrInput = input("Enter one valid letter or '@' to exit: ")        
            
        if not usrInput.isalpha():
            if usrInput == "@":
                print("Bye, bye!!!\n")
            else:
                print("Invalid character!!!\n")
            break

        for indice, character in enumerate(wordGuessList):
            if character == usrInput:
                charExists = True
                listOutPut[indice] = usrInput
            elif character == usrInput.capitalize():
                print("Capital letter")
        if not charExists:
            count += 1
        
        charExists = False
                       
        print(board[count], end="")
        for i in range(len(listOutPut)):
            print(listOutPut[i] + " ", end="")

        if count == 9:
            print("\n")
            print(f"\nYou loose!!! - {wordGuess}\n")
            break