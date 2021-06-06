# exercise-02 Length of Phrase

while True:
    phrase = input('Please enter a word or phrase or "quite" to Exit:')
    if phrase == 'quite':
        print('Goodbye')
        break
        
    else:
        phrase_length = len(phrase)
        print(f'What you entered is {phrase_length} characters long')