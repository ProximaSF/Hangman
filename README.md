# Extra Credit Hangman_2.0 Problem Formulation

## Project Proposal:
The goal of this project is to create a hangman game. It will pick a random word from the **word.txt** file. The user will be able to guess a letter one at a time. If the letter is part of the word, it will print a word layout with empty `_` but the letter guessed correctly in the correct position. If guessed incorrectly, it will decrease the `attempt` int variable by 1 (total 11) and print a list of used/guessed letters. If the user uses up all `attempts`, the code will end and print out the word that was picked. The user will also have the option to stop the game by typing "stop" in the terminal to end the game. 

## Lists major subparts of the problem and how they're related logically, and what data is going in and out of each subpart
1. random_word() function:
   - This function picks a random word from the words.txt.
     - Returns the word without the newline syntax. 

2. hangman_info() Function:
   - This function returns multiple pieces of info that will handle initial logic to be used in the `check_input()` function.
     - Returns `words`, a random word picked from the txt file based on the def function `random_word()`.
     - Returns `word_num_size`, the size of the word.
     - Returns `attempts`, a number of attempts the user is allowed. 
     - Returns `sorted_word_letter_list`, a list of sorted letters based on the word `words`. 

3. print_empty_start() function:
   - This function prints the starting message after starting the game.
   - It prints an empty list of **_** based on the size of the word picked.
   - It doesn't return any value, only called once.
  
4. check_input() function:
   - This function is the main logic behind the game.
   - It uses all 4 parameters returned from the `hangman_info()` function.
   - The function takes the user's input and determines if the input is a letter. If so and the letter is part of the word, it will call another function `change()`. Else it will decrease the attempt value and call the `draw_hangman()` function.
    - It contains multiple side variables (used letters, body part, while loop boolean, etc.) that are used in the function and some are used outside of other functions. 
   - This function doesn't return any values.

5. change() function:
   - This function is called if the user entered a value that is part of the hangman word. 
     - It updates the hangman text display based on the letters guessed correctly and the missing blanks using the print statement.
   - This function takes 3 parameters from `check_input()`. 

6. draw_hangman() function:
   - This function draws the body part of the hangman when the user enters the wrong letter. 
     - It takes in two parameters from the `check_input()` function.
     - It uses a dictionary to handle the logic of what body part to draw (print the name, not an actual image) based on the `total_body_parts` counter that keeps track of what is already drawn. 
       - If the whole body is drawn, the game stops by ending the while loop.

## Lists major input/intermediate/output data:
1. Input data:
   - `word`: random word picked from the text file.
     - `word_num_size`: size of the word.
   - `attempts`: a fixed number of attempts.
   - `sorted_word_letter_list`: list of sorted letters based on the word.
   - `user_input`: grabs the user input to be read.

2. Intermediate data:
   - `isTrue2`: a boolean value that determines if the while loop stops or not.
   - `isTrue` is only used in the `change()` function once when the user guessed the word correctly for the first time.
     - It adds the number of empty **_** based on the size of the word. It is used as a placeholder (`word_letters`).
   - `used_letters`: a list that will be populated based on what letters the user has guessed.
   -  `correct_letters`: a list of correct letters the user has guessed.
   - `total_body_parts`: the number of body parts that will be drawn based on the number of keys in the `body_parts` dictionary.
   - `num_attempts`: a changeable variable that determines how many attempts the user has. 
   - `used_letters_2`: It does something, I forgot.
   - `final_list`: a dictionary that stores the index position in a list of all the letters in the word.
   - `pos_letter_dic`: Gets the position of the correct letter guessed by the user. 
   - `total_body_parts`: a changeable int variable that decreases when the user guesses incorrectly.
   - `body_parts`: a dictionary of body parts to be drawn as a reference.

3. Output data:
   - Initial print statement when the game starts
     - Empty number of **_**. 
     - Number of attempts the user has and how to stop the code.
   - If the user guesses correctly:
     - Print number of attempts (stays the same)
     - Display the letters guessed with their unsolved letters as **_**
   - If the user guesses incorrectly:
     - A message saying the letter is not part of the word
     - The number of attempts left (decreased by one)
     - The body part
   - If the user guesses a word already guessed:
     - A message saying the letter was already guessed
     - Number of attempts (unchanged)
     - A list of letters guessed and a list of correct letters guessed.
   - If the user types "stop", it will print:
     - Message saying the game has stopped.
     - The word the user needed to guess
   - If the user runs out of attempts or guesses all the letters before running out of attempts:
     - Message for one of those conditions
     - Message of the word needed to guess.

## Brief statement:
The goal of this code is to make a hangman game that can handle a number of attempts, correct and incorrect input. The code will also display a reference of the hangman so the user can see what they need to guess. It will also draw (send a text) of the hangman body part(s) when the user guesses incorrectly. The code can be manually stopped if the user wishes to.

## Example Inputs and Outputs:

Suppose the word is "Pineapple"

1. Scenario #1
   - Input:
     - "p"
   - Output: 
     - p _ _ _ _ p p _ _
     - Number of attempts: 11
  
2. Scenario #2
   - Input: 
     - "z"
   - Output: 
     - p _ _ _ _ p p _ _
     - Number of attempts: 10
     - Mouth

3. Scenario #3
   - Input:
     - stop
   - Output:
     - GAME STOPPED
     - The word was "pineapple"
  
☺☻