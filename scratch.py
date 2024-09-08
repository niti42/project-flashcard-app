from tkinter import *
import pandas as pd
import random

# Global variable to store the scheduled flip ID
scheduled_flip_id = None

BACKGROUND_COLOR = "#B1DDC6"
card_front_img_path = "images\card_front.png"
card_back_img_path = "images\card_back.png"


def next_card():
    global scheduled_flip_id, to_learn
    # Cancel any previously scheduled flip
    if scheduled_flip_id is not None:
        window.after_cancel(scheduled_flip_id)
    new_card = None
    try:
        new_card = random.choice(to_learn)
        new_word = new_card.get("French")
        translation = new_card.get("English")
    except (IndexError):
        new_word = ""
        translation = ""

    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card_title, fill='black')
    canvas.itemconfig(card_word, fill='black')
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=new_word)
    # Schedule the flip card function after 3 seconds
    scheduled_flip_id = window.after(3000, lambda: flip_card(translation))

    return new_card


def correct_button_action():
    global to_learn
    if viewed_card := next_card():
        to_learn.remove(viewed_card)
        to_learn_df = pd.DataFrame(to_learn)
        to_learn_df.to_csv("data/words_to_learn.csv", index=False)


def wrong_button_action():
    viewed_card = next_card()
    print("I got this wrong")
    print(viewed_card)


def flip_card(translation):
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, fill='white')
    canvas.itemconfig(card_word, fill='white')
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=translation)


    # -------------------------Load DAta -------------------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except (pd.errors.EmptyDataError, FileNotFoundError):
    data = pd.read_csv("data/sample_french_words.csv")
to_learn = data.to_dict(orient="records")


# --------------------------UI Setup-------------------------------------
window = Tk()
window.title("Remembrall")
window.configure(background=BACKGROUND_COLOR)
window.configure(padx=50, pady=50)


canvas = Canvas(width=800, height=526)


# card front
card_front_img = PhotoImage(file=card_front_img_path)
card_back_img = PhotoImage(file=card_back_img_path)
# (400,263) is the center of the image
card = canvas.create_image(400, 263, image=card_front_img)


# configure the background color here rather than when you make the object
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


# text
card_title = canvas.create_text(400, 150, text='title',
                                font=("Arial", 40, "italic"))

card_word = canvas.create_text(400, 263, text='word',
                               font=("Arial", 60, "bold"))
next_card()

canvas.grid(row=0, column=0, columnspan=2)


# right button
check_mark = PhotoImage(
    file="D:/hundred_days_of_code_reset/dat31-flash-card-project/images/right.png")
button_correct_ans = Button(image=check_mark,
                            highlightthickness=0, command=correct_button_action)
button_correct_ans.grid(row=1, column=0)

# wrong button
cross_mark = PhotoImage(
    file="D:/hundred_days_of_code_reset/dat31-flash-card-project/images/wrong.png")
button_wrong_ans = Button(
    image=cross_mark, highlightthickness=0, command=wrong_button_action)
button_wrong_ans.grid(row=1, column=1)

window.mainloop()
