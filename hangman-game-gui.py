from random_words import RandomWords
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase

words = RandomWords()

root = Tk()

root.title("Hangman")

photos = [
    PhotoImage(file="images\hang5.png"),
    PhotoImage(file="images\hang6.png"),
    PhotoImage(file="images\hang7.png"),
    PhotoImage(file="images\hang8.png"),
    PhotoImage(file="images\hang9.png"),
    PhotoImage(file="images\hang10.png"),
    PhotoImage(file="images\hang11.png"),
]


# def reSet():
#     global nosOfGuesses
#     global word
#     global wordwithspaces

#     nosOfGuesses = 0
#     wordwithspaces = ""
#     word = ""

#     newGame()


def newGame():
    global wordwithspaces
    global nosOfGuesses

    nosOfGuesses = 0
    imgLabel.config(image=photos[0])
    word = words.random_word().upper()
    wordwithspaces = " ".join(word)
    lblWord.set(" ".join("_" * len(word)))
    print(word)


def guess(letter):
    global nosOfGuesses
    if nosOfGuesses < 6:
        txt = list(wordwithspaces)
        gussed = list(lblWord.get())
        if wordwithspaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    gussed[c] = letter
                lblWord.set("".join(gussed))

                if lblWord.get() == wordwithspaces:
                    messagebox.showinfo("Hangman", "You Gussed it")
                    newGame()

        else:
            nosOfGuesses += 1
            imgLabel.config(image=photos[nosOfGuesses])
            if nosOfGuesses == 6:
                lblWord.set(wordwithspaces)
                messagebox.showinfo("Hangman", "Game Over")
                newGame()


imgLabel = Label(root)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(root, textvariable=lblWord, font=("Consolas 24 bold")).grid(
    row=0, columnspan=15, padx=150
)

n = 0

for c in ascii_uppercase:
    Button(
        root,
        text=c,
        command=lambda c=c: guess(c),
        font=("Helvetica 10"),
        width=4,
        fg="orange",
        bg="black",
    ).grid(row=1 + n // 9, column=n % 9)
    n += 1


newGame()

root.mainloop()