# Hangman Game
import random
import turtle
import math
import time

# Dictionsary of Words
wordList = ['Python', 'Ambivalent', 'Equivocal', 'Urge', \
            'Complacent', 'Reprisal', 'Eviscerate', 'Melodramatic', \
            'Afford', 'Allude', 'Ambiguous', 'Assertion', \
            'Contend', 'Cultivate', 'Diminish', 'Facilitate', \
            'Malleable', 'Lucrative', 'Paramount', 'Sentiment', \
            'Surmount', 'Tentative', 'Ubiquitous', 'Viability']

secretWord = random.choice(wordList)
wrongLetters = []
correctLetters = []
print(f"The secret word is {secretWord}")

wrongGuesses = 0
MAX_GUESSES = 11
screenWord = ""

# Screen Set up
screen = turtle.getscreen()
turtle.colormode(255)
sWidth = 1200
sHeight = 600
screen.setup(sWidth, sHeight)
screen.bgcolor('#b3711b')

# Making the First Turtle
t = turtle.getturtle()
t.hideturtle()
t.color('#ffffff')
t.width(5)
t.speed(0)
t.penup()

# Making a Top Screen Turtle
topScreenTurtle = turtle.Turtle()
topScreenTurtle.hideturtle()
topScreenTurtle.color('#ffffff')
topScreenTurtle.width(5)
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-1 * int(sWidth / 2) + int(sWidth * 0.12),  -1 *int(sWidth * 0.2))
topScreenTurtle.setheading(0)

# Making a Bottom Screen Turtle
bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.hideturtle()
bottomScreenTurtle.color('#ffffff')
bottomScreenTurtle.width(5)
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-1 * int(sWidth / 2) + int(sWidth * 0.12), -1 * int(sHeight / 2) + int(sWidth * 0.125))
bottomScreenTurtle.setheading(0)

# Locations:
rightFootLoc = (0, 0)
leftFootLoc = (0, 0)
wordsLoc = (0, 0)


# Drawings
def drawGallows():
    t.forward(int(sWidth * 0.125))
    t.right(90)
    t.forward(int(sHeight * 0.25))
    t.left(90)
    t.pendown()
    t.forward(int(sWidth * 0.25))
    t.backward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.65))
    t.left(90)
    t.forward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * .1))
def drawHead():
    t.right(90)
    t.circle(int(sHeight * 0.055))
def drawHat():
    t.forward(int(sWidth * .05))
    t.backward(int(sWidth * .025))
    t.right(90)
    t.forward(int(sHeight * .07))
    t.right(90)
    t.forward(int(sWidth * .05))
    t.right(90)
    t.forward(int(sHeight * .07))
    t.left(90)
    t.forward(int(sWidth * .025))
    t.left(180)
    t.forward(int(sWidth * .05))
def drawBody():
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.055) * 2)
    t.pendown()
    t.forward(int(sHeight * 0.15))
    t.penup()
def drawLegLeft():
    global leftFootLoc
    t.right(20)
    t.pendown()
    t.forward(int(sHeight * .15))
    leftFootLoc = t.position()
    t.penup()
    t.backward(int(sHeight * .15))
def drawLegRight():
    global rightFootLoc
    t.left(40)
    t.pendown()
    t.forward(int(sHeight * .15))
    rightFootLoc = t.position()
    t.penup()
    t.backward(int(sHeight * .15))
    t.right(20)
def drawRArm():
    t.backward(int(sHeight * .075))
    t.pendown()
    t.right(90)
    t.forward(int(sHeight * .075))
def drawLArm():
    t.right(180)
    t.forward(int(sHeight * .150))
    t.left(180)
    t.forward(int(sHeight * .075))
    t.right(90)
    t.penup()
def drawEyes():
    t.forward(int(sHeight * .135))
    t.right(90)
    t.forward(int(sHeight * .015))
    t.pendown()
    t.forward(int(sHeight * .001))
    t.penup()
    t.left(180)
    t.forward(int(sHeight * .035))
    t.pendown()
    t.forward(int(sHeight * .001))
    t.penup()
def drawMouth():
    t.backward(int(sHeight * .025))
    t.left(90)
    t.forward(int(sHeight * .025))
    t.pendown()
    t.left(90)
    t.forward(int(sHeight * .015))
    t.left(180)
    t.forward(int(sHeight * .030))
    t.right(180)
    t.right(90)
    t.penup()
    t.forward(int(sHeight * .15))
def drawRFoot():
    t.penup()
    t.goto(rightFootLoc)
    t.left(90)
    t.pendown()
    t.forward(int(sHeight * .015))
    t.circle(10)
    t.penup()
def drawLFoot():
    t.penup()
    t.goto(leftFootLoc)
    t.left(90)
    t.pendown()
    t.forward(int(sHeight * .015))
    t.circle(10)

# Word Guessing
def updateDrawing():
    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawHat()
    if wrongGuesses == 3:
        drawBody()
    if wrongGuesses == 4:
        drawLegLeft()
    if wrongGuesses == 5:
        drawLegRight()
    if wrongGuesses == 6:
        drawRArm()
    if wrongGuesses == 7:
        drawLArm()
    if wrongGuesses == 8:
        drawEyes()
    if wrongGuesses == 9:
        drawMouth()
    if wrongGuesses == 10:
        drawRFoot()
    if wrongGuesses == 11:
        drawLFoot()
def drawWord():
    global screenWord
    bottomScreenTurtle.clear()
    bottomScreenTurtle.penup()
    bottomScreenTurtle.goto(-1 * int(sWidth / 2) + int(sWidth * 0.12), -1 * int(sHeight / 2) + int(sWidth * 0.125))
    bottomScreenTurtle.setheading(0)
    screenWord = " "

    for letter in secretWord.lower():
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottomScreenTurtle.write(screenWord, move=False, align='left', font=('Arial', 64, 'normal'))
def drawWrongLetters():
    topScreenTurtle.clear()
    lettersString = "Wrong Letters: "
    for l in wrongLetters:
        lettersString += l + ", "
        lettersString = lettersString[: -1]
    topScreenTurtle.write(lettersString, move=False, align='left', font=('Arial', 64, 'normal'))
def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ","

    boxTitle = 'Letters Used:' + badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess
def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align='left', font=('Arial', 24, 'normal'))
    time.sleep(2)
    topScreenTurtle.clear()
def printWinOrLose(win):
    topScreenTurtle.clear()
    if win:
        topScreenTurtle.write("You Win!!", move=False, align='left', font=('Arial', 64, 'normal'))
    else:
        topScreenTurtle.write("I'm sorry, you lost...", move=False, align='left', font=('Arial', 64, 'normal'))
def getWordGuess():
    playerWordGuess = screen.textinput("Guess it", "Enter your guess of the word:")
    print(playerWordGuess)
    print(secretWord)
    if playerWordGuess.lower() == secretWord.lower():
        printWinOrLose(True)
        return False
    else:
        printWinOrLose(False)
        time.sleep(1)
        writeErrorMessage("The secret word was " + secretWord)
        return False


# Playing the Game
gameOn = True
updateDrawing()
while gameOn:
    drawWord()
    guess = getGuess()

    if guess == "$$":
        gameOn = getWordGuess()
    elif len(guess)!= 1:
        writeErrorMessage("Sorry, you can only guess one letter... Guess again:")
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("Sorry, you can only guess letters... Guess again:")
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guessed " + guess + ", please guess again")
        drawWrongLetters()
    else:
        if guess.lower() in secretWord.lower():
            print(guess + " is in " + secretWord)
            correctLetters.append(guess.lower())
            drawWord()
        else:
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updateDrawing()
        if (wrongGuesses >= MAX_GUESSES):
            writeErrorMessage("Sorry, that's game over.")
            gameOn = False
            writeErrorMessage("The secret word was " + secretWord)
        if "_" not in screenWord:
            writeErrorMessage("Excelent!! YOU WIN!!")
            gameOn = False

topScreenTurtle.hideturtle()
bottomScreenTurtle.hideturtle()
t.hideturtle()
turtle.mainloop()