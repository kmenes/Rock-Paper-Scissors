print "Hi, I'm Kristian Menes' computer.  Let's play Rock-Paper-Scissors!"
def function(s, computer, you):
	from random import choice 
	x = choice("rps")
	if move == "r" and x == "r":
		print "Ok, my move is rock."
		print "Haha we tied, wow!"
		return computer + 1, you + 1
	elif move == "r" and x == "s":
		print "Ok, my move is scissors."
		print "Oh, no! You won!"
		return computer, you + 1
	elif move == "r" and x == "p":
		print "Ok, my move is paper."
		print "Yay! I won!"
		return computer + 1, you
	elif move == "s" and x == "r":
		print "Ok, my move is rock."
		print "Yay! I won!"
		return computer + 1, you
	elif move == "s" and x == "s":
		print "Ok, my move is scissors."
		print "Haha we tied, wow!"
		return computer + 1, you + 1
	elif move == "s" and x == "p":
		print "Ok, my move is paper."
		print "Oh, no! You won!"
		return computer, you + 1
	elif move == "p" and x == "r":
		print "Ok, my move is rock."
		print "Oh, no! You won!"
		return computer, you + 1
	elif move == "p" and x == "s":
		print "Ok, my move is scissors"
		print "Yay! I won!"
		return computer + 1, you
	elif move == "p" and x == "p":
		print "Ok, my move is paper."
		print "Haha we tied, wow!"
		return computer + 1, you + 1
	elif move == "q":
		return "Ok, see you later!" 
	else:
		print "I don't understand that. Sorry :/"
		return computer, you

x = 0
y = 0

move = raw_input("Make your move (r, p, s) or q to quit")
while move != "q":
	x, y = function(move, x, y)
	print (x, y)
	move = raw_input("Make your move (r, p, s) or q to quit: ")

if x > y:
	print "YAY, I beat you, I guess computers are better!"
if x == y:
	print "WOW, we tied the whole game, that's weird"
if x < y:
	print "Oh no, how did you beat me!"

print "Game over, it was nice playing you!"
print "Final Score is Me: %d, You: %d" % (x, y)
