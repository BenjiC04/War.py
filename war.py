#imports
import turtle as trtl
import random
import keyboard

#setup
drawer = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
wn = trtl.Screen()



#welcome screen
#background setup
drawer.hideturtle()
wn.setup(width=0.5, height=0.5)
bg = "card_table.GIF"
wn.addshape(bg)
wn.bgpic(bg)

#welcome page
trtl.textinput("Welcome!", "This is the card game 'War', a game of chance. Type 'Okay' to continue")


#setup cards
drawer.showturtle()
drawer.penup()
back_card = "back_card.gif"
wn.addshape(back_card)
drawer.shape(back_card)
drawer.goto(-250, -120)
drawer2.penup()
drawer2.shape(back_card)
drawer2.goto(250, 120)

two_spades = "2_of_spades.gif"
wn.addshape(two_spades)

three_spades = "3_of_spades.gif"
wn.addshape(three_spades)

four_spades = "4_of_spades.gif"
wn.addshape(four_spades)

five_spades = "5_of_spades.gif"
wn.addshape(five_spades)

six_spades = "6_of_spades.gif"
wn.addshape(six_spades)

seven_spades = "7_of_spades.gif"
wn.addshape(seven_spades)

eight_spades = "8_of_spades.gif"
wn.addshape(eight_spades)

nine_spades = "9_of_spades.gif"
wn.addshape(nine_spades)

ten_spades = "10_of_spades.gif"
wn.addshape(ten_spades)

jack_spades = "jack_of_spades2.gif"
wn.addshape(jack_spades)

queen_spades = "queen_of_spades2.gif"
wn.addshape(queen_spades)

king_spades = "king_of_spades2.gif"
wn.addshape(king_spades)

ace_spades = "ace_of_spades.gif"
wn.addshape(ace_spades)

#deal cards
ranks = [two_spades, three_spades, four_spades, five_spades]
num_cards = [2, 3, 4, 5]


 #get integers to equal card (2 = two_spades, etc.)

num_cards = ranks

#deal function
#player cards
drawer3.penup()
drawer3.goto(-100, 0)
def main():
    suite = random.choice(num_cards)
    drawer3.shape(suite)
    num_cards.remove(suite)
    print(num_cards)

drawer4.penup()
drawer4.goto(100, 0)
def main2():
    suite2 = random.choice(num_cards)
    drawer4.shape(suite2)
    num_cards.remove(suite2)
    print(num_cards)


wn.onkeypress(main, "a")
wn.listen()

#computer cards
wn.onkeypress(main2, "a")
wn.listen()

'''i = 1
while i < 2:
  main2()
  i += 1'''


#compare values
'''if ( main > main2):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")'''


wn.mainloop()
