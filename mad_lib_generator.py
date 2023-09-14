'''
Mad Libs Generator
-------------------------------------------------------------
'''

# Questions for the user to answer
print("Welcome to Mad Libs Generator!")


noun = input('Choose a noun: ')

p_noun = input('Choose a plural noun: ')

noun2 = input('Choose a second noun: ')

place = input('Name a place: ')

adjective = input('Choose an adjective: ')

adjective2 = input('Choose a second adjective: ')

# Print a story from the user input

print('------------------------------------------')

print('There was an Old Man with a', noun, 'and some', p_noun)

print('And his duck ate somebody\'s', noun2, '.')

print('So the duck said: "I should take this', p_noun, 'in the', place, '"')

print('Where the weather is always', adjective, '. \n')

print('You may think that this is', adjective2, ',')

print('Well it is.')

print('------------------------------------------')
