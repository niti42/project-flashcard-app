# Flashcard App

## Overview

The Flashcard App is a simple educational tool designed to help users learn French vocabulary through interactive flashcards. Users can view French words, see their English translations, and track their progress by marking words as learned or not.

## Features

- Randomly displays French words on flashcards.
- Flips the card to show the English translation after a set duration.
- Allows users to mark words as correct or incorrect.
- Saves progress by updating the list of words to learn.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
- Pandas library

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>

   ```

2. Create a virtual environment (optional but recommended):

```
python -m venv .venv
```

3. Activate the virtual environment:

On Windows:

```
.venv\Scripts\activate
```

On macOS/Linux:

```
source .venv/bin/activate
```

Install required packages:

```
pip install pandas
```

Usage
Run the application:

```
python main.py
```

The app will display a flashcard with a French word. After 3 seconds, it will flip to show the English translation.

Use the buttons to mark the word as correct (✓) or incorrect (✗):

- Clicking the correct button will remove the word from the learning list.
- Clicking the wrong button will keep the word in the list for future review.

The app saves your progress in a CSV file, allowing you to continue learning where you left off.
