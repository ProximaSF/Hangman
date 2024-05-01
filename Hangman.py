def hangman_info():
    sorted_word_letter_list = []
    word = "APPLE"
    word_num_size = len(word)
    attempts = 9

    for i in range(word_num_size):
        sorted_word_letter_list.append(word[i])

    sorted_word_letter_list.sort()
    print(sorted_word_letter_list)

    return word_num_size, word, attempts, sorted_word_letter_list

def print_empy_start(num_size):
    word_letters = ''
    for _ in range(num_size):
        word_letters += "_ "
    print(word_letters.strip(' '))

def check_input(word_num_size, word, attempts, sorted_word_letter_list):
    num_attempts = attempts
    used_letters = []
    correct_letters = []
    print(f"Guess the word, you have {num_attempts} attempts\n"
          "Type 'stop' to the game")

    isTrue2 = True
    while isTrue2:
        user_input = input("").upper()
        if user_input.casefold() == "stop":
            print("\nGAME STOPPED")
            print(f"The word was '{word}'")
            isTrue2 = False

        elif not user_input.isalpha() or len(user_input) > 1:
            print("Please only enter one letter!")
        
        else:
            if num_attempts == 1:
                print("You ran out of attempts")
                print(f"The word was \"{word}\"")
                isTrue2 = False

            
            elif user_input in used_letters:
                print("You already used that letter, try again")
                print(f"Number of attempts: {num_attempts}")
                print(used_letters)
                print(correct_letters)

            elif not user_input in word:
                used_letters.append(user_input)
                print(f"{user_input} is not part of the word, try again.")

                num_attempts -= 1
                print(f"Number of attempts: {num_attempts}")
                draw_hangman(word)

            elif user_input in word:
                used_letters.append(user_input)
                
                # Add the correct number of valid letters in the correct_letter list to be compare with
                count = sorted_word_letter_list.count(user_input)
                #print(count)
                for i in range(0, count):
                    correct_letters.append(user_input)
                correct_letters.sort()

                num_attempts -= 1
                print(f"Number of attempts: {num_attempts}")
                
                used_letters_2 = []
                final_list = {}
                for i in range(word_num_size):
                    pos = []
                    letter = word[i]
                    if letter in used_letters_2:
                        continue
                    else:
                        used_letters_2.append(letter)
                        for j in range(word_num_size):
                            if letter == word[j]:
                                pos.append(j)
                        final_list[letter] = pos
                print(final_list)
                pos_letter_dic = final_list[user_input]
                
                change(word_num_size, pos_letter_dic, user_input)

                if correct_letters == sorted_word_letter_list:
                    print("Good job, you solve the word!")
                    isTrue2 = False


word_letters = ''
isTrue = True
def change(word_num_size, pos_letter_dic, user_input):
    global word_letters
    global isTrue
    if isTrue:
        for _ in range(word_num_size):
            word_letters += "_"
        isTrue = False
    new_word_letters = list(word_letters)

    for i in range(word_num_size):
        if i in pos_letter_dic:
            new_word_letters[i] = user_input
    word_letters = ''.join(new_word_letters)
    print(''.join(new_word_letters))

def draw_hangman(word):
    global isTrue2
    total_body_parts = 10 - 1
    body_parts = {1: "head", 2: "body", 3: "left_leg", 4: "right_leg", 5: "left_arm", 6: "right_arm", 7: "eyes", 8: "nose", 9: "mouth"}
    if total_body_parts == 1:
        print("Oh know, you lost!")
        print(f"The word was {word}")
        isTrue2 = False
    else:
        print(body_parts[total_body_parts])


word_num_size, word, attempts, sorted_word_letter_list = hangman_info()
print_empy_start(word_num_size)
check_input(word_num_size, word, attempts, sorted_word_letter_list)