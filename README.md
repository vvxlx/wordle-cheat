# 🟩 Wordle Guesser

A lightweight Python-based Wordle solver that analyzes your guesses, understands **green, yellow, and gray letters**, handles duplicate letters correctly, and filters thousands of possible words to find the best matches.

Built to make Wordle solving faster, smarter, and a little more satisfying. 🎯

---

# ✨ Features

✅ Automatic Wordle word filtering  
✅ Correct green-letter position checking  
✅ Yellow-letter position tracking  
✅ Gray-letter elimination  
✅ Duplicate-letter support  
✅ Works with large custom word lists  
✅ Words can be in any order  
✅ Displays remaining possible answers  
✅ Suggests useful next guesses  
✅ Shows detected constraints after every guess  
✅ Fully configurable word list  
✅ No external API required  

---

# 🧠 How It Works

The solver uses the feedback from each Wordle attempt to eliminate impossible words.

For example:

```text
Guess:    SNIPE
Feedback: ....G
```

The solver understands:

```text
S N I P _
        ↓
        E must be here
```

So only words matching:

```text
____E
```

remain possible.

If a letter is yellow:

```text
Guess:    SNIPE
Feedback: .Y..G
```

the solver knows:

```text
N exists in the answer
N is NOT in position 2
E MUST be in position 5
```

It then removes every word that violates those rules.

---

# 🔍 Duplicate Letter Handling

Unlike basic Wordle filters, this solver properly handles repeated letters.

For example:

```text
Answer:   SHEEP
Guess:    SPEED
```

The program doesn't simply search for letters. It recreates Wordle's actual feedback system so that duplicate letters are handled correctly.

This prevents false suggestions caused by words containing too many copies of a letter.

---

# 📸 Example

After entering a guess, the solver displays the information it has learned:

```text
==================================================
              WORDLE GUESSER
==================================================

Possible answers: 2,347

BEST SUGGESTIONS:
 1. ARISE
 2. STARE
 3. CRATE
 4. SLATE
 5. IRATE

Enter your guess: SNIPE
Enter feedback (G/Y/.): ....G

KNOWN INFORMATION
-----------------
GREEN: position 5 = E
```

The word list is immediately filtered using that information.

---

# 📁 Word List

The solver uses a simple `words.txt` file.

Example:

```text
horse
stare
train
crane
house
arise
slate
apple
sheep
green
```

The words **do not need to be sorted**.

You can mix them however you want:

```text
horse
train
apple
crane
stare
house
green
```

The program will still process every word correctly.

---

# ⚙️ Installation

## 1. Install Python

Python **3.10+** is recommended.

Download Python from:

https://www.python.org/downloads/

Make sure Python is added to your system PATH during installation.

---

## 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/wordle-guesser.git
```

Enter the project directory:

```bash
cd wordle-guesser
```

---

## 3. Add your word list

Place your five-letter word list in:

```text
words.txt
```

The project should look like:

```text
wordle-guesser/
│
├── main.py
├── words.txt
└── README.md
```

---

# ▶️ Running

Start the solver with:

```bash
python main.py
```

You'll be asked for your Wordle guess:

```text
Enter your guess: SNIPE
```

Then enter the colors Wordle gave you:

```text
Enter feedback (G/Y/.): ....G
```

Where:

```text
G = Green
Y = Yellow
. = Gray
```

---

# 🎨 Feedback System

| Symbol | Meaning |
|--------|---------|
| 🟩 `G` | Correct letter + correct position |
| 🟨 `Y` | Correct letter + wrong position |
| ⬜ `.` | Letter is not used |

Example:

```text
S N I P E
. Y . . G
```

Means:

```text
S → not in the answer
N → exists, but not position 2
I → not in the answer
P → not in the answer
E → position 5
```

---

# 🎯 Suggestions

After every round, the solver ranks possible guesses based on letter frequency.

Example:

```text
BEST SUGGESTIONS:

 1. ARISE
 2. STARE
 3. CRATE
 4. SLATE
 5. IRATE
```

The suggestions are selected from the available word pool to prioritize letters that can reveal useful information.

---

# 🛠️ Configuration

The main settings are located at the top of `main.py`.

```python
WORD_FILE = "words.txt"
```

You can replace this with another word-list file:

```python
WORD_FILE = "my_words.txt"
```

As long as the file contains five-letter words, the solver can use it.

---

# 📦 Requirements

The project intentionally has **no third-party dependencies**.

It only uses Python's built-in modules:

```text
collections
```

So there is no need to run:

```bash
pip install ...
```

Just install Python and run the program.

---

# 🧪 Tested Cases

The checker is designed to correctly handle:

```text
✓ Green letters
✓ Yellow letters
✓ Gray letters
✓ Multiple green letters
✓ Multiple yellow letters
✓ Duplicate letters
✓ Mixed word lists
✓ Large word lists
✓ Impossible combinations
```

For example, if the only known information is:

```text
____E
```

then words such as:

```text
HORSE
RINSE
CRANE
SLATE
```

can remain possible, while words that don't end in `E` are eliminated.

---

# 🚀 Future Improvements

Possible additions:

- 🧠 Entropy-based guess selection
- 📊 Information-gain scoring
- 🎯 Automatic optimal starting word
- 🖥️ Graphical interface
- 🌐 Browser-based version
- ⌨️ Keyboard visualization
- 📚 Built-in English word database
- 🔄 Automatic Wordle board input
- 📈 Guess statistics
- 🏆 Average guesses tracker
- 🌙 Dark-mode GUI
- ⚡ Faster filtering for huge dictionaries

---

# 🗂️ Project Structure

```text
wordle-guesser/
│
├── main.py          # Main solver
├── words.txt        # Five-letter word database
└── README.md        # Documentation
```

---

# ⚠️ Notes

- Use a word list containing five-letter words.
- The solver does not require the words to be sorted.
- Make sure the feedback is entered exactly as Wordle displays it.
- `G`, `Y`, and `.` are case-insensitive for the guess, but feedback is normalized automatically.
- Incorrect feedback can eliminate the real answer, so double-check your colors.

---

# 💡 Why This Project?

Most simple Wordle scripts only check whether letters exist somewhere in a word.

This project goes further by treating Wordle feedback as a set of constraints:

```text
GREEN  → exact position
YELLOW → required letter + forbidden position
GRAY   → excluded letter
```

That makes the solver much more reliable when dealing with real Wordle games and duplicate letters.

---

# 📜 License

MIT License

Copyright VVXLX (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
