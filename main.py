import pandas as pd
import random
from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMG_PATH = "images/card_front.png"
CARD_BACK_IMG_PATH = "images/card_back.png"
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"
SAMPLE_WORDS_PATH = "data/french_words.csv"

# Global variable to store the scheduled flip ID
scheduled_flip_id = None
to_learn = []
new_card = {}


def load_data():
    """Load words from CSV or fallback to sample data."""
    try:
        return pd.read_csv(WORDS_TO_LEARN_PATH).to_dict(orient="records")
    except (pd.errors.EmptyDataError, FileNotFoundError):
        return pd.read_csv(SAMPLE_WORDS_PATH).to_dict(orient="records")


def next_card():
    """Selects and displays the next flashcard from the list of words to learn.

    This function cancels any previously scheduled card flip and randomly selects a new card from the `to_learn` list. It updates the UI to show the French word on the front of the card and schedules a flip to display the English translation after a set duration.

    Args:
        None

    Returns:
        None
    """

    global scheduled_flip_id, to_learn, new_card
    if scheduled_flip_id is not None:
        window.after_cancel(scheduled_flip_id)

    if not to_learn:
        return None

    new_card = random.choice(to_learn)
    new_word = new_card.get("French", "")
    translation = new_card.get("English", "")

    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card_title, fill='black', text="French")
    canvas.itemconfig(card_word, fill='black', text=new_word)

    scheduled_flip_id = window.after(3000, lambda: flip_card(translation))


def update_words(viewed_card):
    """Update the words to learn after a correct answer."""
    global to_learn
    if viewed_card in to_learn:
        to_learn.remove(viewed_card)
        pd.DataFrame(to_learn).to_csv(WORDS_TO_LEARN_PATH, index=False)
    else:
        print(f"Card not found in to_learn: {viewed_card}")


def correct_button_action():
    update_words(new_card)
    next_card()


def flip_card(translation):
    """Displays the back of the flashcard with the English translation.

    This function updates the UI to show the English translation of the word on the back of the flashcard. It changes the card's image and text color to indicate that the card has been flipped.

    Args:
        translation (str): The English translation of the French word to be displayed.

    Returns:
        None
    """
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, fill='white', text="English")
    canvas.itemconfig(card_word, fill='white', text=translation)


# Load data
to_learn = load_data()

# UI Setup
window = Tk()
window.title("Remembrall")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT_IMG_PATH)
card_back_img = PhotoImage(file=CARD_BACK_IMG_PATH)
card = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(
    400, 150, text='title', font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text='word', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_mark = PhotoImage(file="images/right.png")
button_correct_ans = Button(
    image=check_mark, highlightthickness=0, command=correct_button_action)
button_correct_ans.grid(row=1, column=0)

cross_mark = PhotoImage(file="images/wrong.png")
button_wrong_ans = Button(
    image=cross_mark, highlightthickness=0, command=next_card)
button_wrong_ans.grid(row=1, column=1)

next_card()
window.mainloop()
