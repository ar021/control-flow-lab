# exercise-01 Vowel or Consonant

letter = input('Please enter a letter from the alphabet (a-z or A-Z):')
print(f'You have entered a {letter}')
if letter.lower() in 'aeiou':
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')
    