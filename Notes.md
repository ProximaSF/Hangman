[hangman_info()]

1. Store the size of the `word` string: `word_num_size`
    • Used to create a list (`sorted_word_letter_list`) of letters formed by `word` 
    • Also used to determine the number of `attempts` 

2. Return `word_num_size`, `word`, `attempts`, `sorted_word_letter_list`

-------------------------------------------------------------------------------------------------

[print_empty_start()]

1. Create an empty hangman word chart (`word_letters`) with the correct number of underscores for each letter in `word` using a loop. 

-------------------------------------------------------------------------------------------------

[check_input()]

1. Takes in 4 parameters: `word_num_size`, `word`, `attempts`, `sorted_word_letter_list`

2. Ask for `user_input` and determine if `user_input` matches one of the statements
    • A while loop keeps asking for input unless the user types `stop`, runs out of `attempts`, or guesses correctly.
    
    • If a letter is guessed correctly, store that letter in `used_letters` and count the number of the same characters and add those character(s) in `sorted_word_letter_list`
        ► `sorted_word_letter_list` will be used to determine if the user manages to guess the word before the attempt limit. 

    • Also create a dictionary (`final_list`) that stores all the positions of the same letter based on `word`
        ► Will loop through all the different characters. Ex: 
        `Word` = 'PINEAPPLE'
        {'P': [0, 5, 6], 'I': [1], 'N': [2], 'E': [3, 8], 'A': [4], 'L': [7]}
    
    • Call `change()`
    
    • If the user guesses all characters for the `word`, end the `while` loop.

-------------------------------------------------------------------------------------------------

[check()]

2. Takes in 3 parameters.

3. Runs the first `for loop` only once with the use of global variable `isTrue` to `False` after the loop is done. 

4. The global variable `word_letters` is set to an empty string at first. After the first loop, it creates an empty _ scores based on the size of the word. 
    • It is than converted into a `list` so it can be used to added letter if the user gussed the correct letter (`new_word_letters`)
        ► After that, this loop no longer work, same for the list conversion.

5. Second loop loop through the `user_input` letter position(s) and change the `new_word_letters` list accordingly based on the size of the word `word_num_size`. 
    • If letter not in position, it keeps the underscore until the iteration end. 
    • It is than converted into a `string` to update `word_letters`, which will be used again, when the user guess the correct letter again.
    • Finally, it print the result. 

-------------------------------------------------------------------------------------------------

[draw_hangman()]

1. Called in `elif not user_input in word:`

2. Each time is called, `total_body_parts` is decreased by one, and print the part of the body. 
    • If `total_body_parts` reaches 1, the game end.

-------------------------------------------------------------------------------------------------

[Hangman_2.0.py]

1. This version adds spaces between each letter using the `insert()` function for the list. The only def function changes is `change()`