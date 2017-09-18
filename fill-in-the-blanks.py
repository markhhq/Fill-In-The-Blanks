# Set up dictionary for all the phrases, question and answers that will be used in the program

data = {
	'easy': {
'phrase':
['Easy', '__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__'],
		
'question':
'''Speaking in public is a form of an art as its other forms like
singing, writing or acting are. The speaker is requiredto be careful or rather
more __1__ because one of its most important requirement is to appear __2__ to
the audience. In ancient times, the great speakers used to prepare their
speeches before a __3__ of their known persons and noticed their own
__4__ and __5__ of the spectators. Their audence __6__ their trusted
friends, critics and mentors. They repeated their speech a number of times
in order to make a good command over their words, speech and way of
speaking. This made their speaking perfect and __7__. This is the reason that
we still study the speeches of great men to gain experience and perfection in
our acts of speaking in public more __8__ and flawlessly.''',
	
'answers':
 ['careful', 'spontaneous', 'gathering', 'shortcoming', 'reaction', 'included', 'immaculate', 
'efficiently']

},

'medium': {

'phrase': ['Medium', '__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__'],
		
'question':
'''It is a well-established __1__ that some people have mathematical
mind while others do not. __2__, the myth is __3__ to mathematics; you never hear
, for example, that someone with a historical mind. It is a general belief __4__ 
us that if we do not learn something it is because we cannot.  In fact mathematical
ideas that are difficult at an early age are much easier to __5__ a few years later,
if we give them another try.\n Another handicap by the math anxious seems to be a
distrust of their own __6__. An immediate right formula or give up the problem is
the real action on the part of a mathematician. Mathematicians trust their intuition
in solving problems and they would not be able to function without it. Another __7__
distinction between the mathematics anxious and people who are not good at figures is
a difference in attitude. So the persons with guessing and estimating __8__ and having
intuitive thinking should be encouraged and rewarded in the class. This helps in learning
word problems, coping with equations and confronting theorems and thereby overpowering the
mythical __9__ of mathematics.''',
  
'answers':
['myth', 'Interestingly', 'restricted', 'amongst', 'comprehend', 'intuition', 'tangible', 'attitude',
'fright']

},

'hard': {
'phrase':
['Hard', '__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__', '__10__'],

'question':
'''Nanotechnology is the __1__ of miniature. It is the engineering of working
__2__ at the molecular level. Due to advancement in technology area, nanotechnology
is the __3__ field that interests many people. From the clothes and sunglasses we wear
to computer drives and even cleaning products, nanotechnology which is __4__ by natural
world, plays a big part in manufacturing many familiar products of our daily use. It
enhances our sunscreen __5__ to reflect harmful ultra violet radiation, armours our
designer shades against unwanted scratches. It increases the capacity of our computer
gadgets for storage of data and photos for our use. Nanotechnology, very broad in its
size, __6__ in itself diverse fields of sciences like surface science, organic chemistry,
molecular biology and semiconductor science etc. Similarly the research and applications
associated to it are also equally __7__. Realising its commercial viability, the scientific
institutions in India have started carrying out research and development work in this filed.
It is now fast becoming a powerful technology that aids the development of products with __8__
performance. The two major categories of nanotechnology are nano-scale technology and molecular
manufacturing. The former covers small structures and can be used for introducing stronger,
better medicines and faster computers and so on. Molecular __9__ is an attempt at building 
mechanical and __10__ manufacturing systems that join molecules together.''',

'answers':
['science', 'systems', 'upcoming', 'inspired', 'ability', 'imbibes', 'diverse', 'futuristic',
'manufacturing', 'chemical']
	}
}

# the play_game function asks for user to choose the level of difficulty, if user enter a invalid value, ask again

def play_game():

	choice = raw_input('Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard:\n')

	while choice.lower() not in data:
		print "That's not an option!"
		choice = raw_input('Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard:\n')
	
	return choice.lower()

# display error messages if the user entered the wrong answer, if user only had 1 guess left, display different message

def wrong_answer(chance, question):

	if chance == 1:

		print "That isn't the correct answer! Let's try again; you only have " + str(chance) + " left!  Make it count!\n\n"
		print question + "\n\n"

	elif chance > 1:

		print "That isn't the correct answer! Let's try again; you have " + str(chance) + " left!\n\n"
		print question + "\n\n"

	return chance

# replace the blanks with correct answers if user guessed correctly

def correct_answer(difficulties, blank_index, user_answer, original_question):

	updated_question = original_question.replace(data[difficulties]['phrase'][blank_index], data[difficulties]['answers'][user_answer])

	print "\nCorrect!\n\n"
	print updated_question + '\n\n'

	return updated_question 


# the fill_in_the_blan prompt user to enter their guesses for each blank of the selected question

def fill_in_the_blank(level):
	
	phrase = data[level]['phrase']
	paragraph = data[level]['question']
	answer_index = 0
	phrase_index = 1
	guesses = 4

	while answer_index < len(data[level]['answers']) and guesses >= 0:

		user_answer = raw_input('What should be substituted for ' + data[level]['phrase'][phrase_index] + ' ?')

		if user_answer == data[level]['answers'][answer_index]:

			paragraph = correct_answer(level, phrase_index, answer_index, paragraph) 

			answer_index += 1
			phrase_index += 1
			guesses = 4

		elif user_answer != data[level]['answers'][answer_index] and guesses >= 0:

			counter = wrong_answer(guesses, paragraph)
			guesses -= 1

			if counter == 0:

				return "You've failed too many straight guesses! Game over!"

	return "You won!"

# set main method

def main():

	selection = play_game()
	
	print "You've chosen " + data[selection]['phrase'][0] + "!\nYou will get 5 guesses per problem\n"
	print data[selection]['question'] + "\n"

	print fill_in_the_blank(selection)


# run main

main()
