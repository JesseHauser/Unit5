'''
############
Do Now 5.01
############

In your Console
---------------
Type the following code:

my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what was printed out. What type is my_dictionary?
it uses a key and uses the key to give the information behind it 
Add a line of code that will print the definition of 'chair', then run the code again.

Write down what happens if you use my_dictionary['kittens']? What do you think that error means?
give a error because it not part of the dictornary 
'''

my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary['chair'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)