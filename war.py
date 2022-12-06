#imports
import turtle as trtl

#setup
drawer = trtl.Turtle()
drawer2 = trtl.Turtle()
wn = trtl.Screen()

'''two_spades = "2_of_spades.gif"
wn.setup(width=1.0, height=1.0)
drawer.shapesize(0.1, 0.1, 1)
wn.addshape(two_spades)
drawer.shape(two_spades)'''

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









wn.mainloop()