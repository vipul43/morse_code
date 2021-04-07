# Morse Code
Cryptographic Communication Interface.

# Setting up
Cloning the repository
```
git clone git@github.com:vipul43/morse_code.git
#Or if using https(you are outdated!)
git clone https://github.com/vipul43/morse_code.git
```
Downloading requirements for running the learner environment
```
#navigate to the cloned directory and enter
pip install -r requirements.txt
```
Running the learner environment
```
python morse_code_learner.py
```

# Getting around the learner Interface
`main display`: ASCII characters(just some subset of it, not all😅) are displayed here.<br>
`input text area`: Try to guess the morse string of the displayed character. The text box only accepts morse characters.<br>
`morse characters`: Morse characters are `'.'` and `'-'`. <br> 
`submit button`: Submits the entered morse string corresponding to the displayed character. If no string is entered then message dialog box is displayed. If wrong morse string is entered, same character is redisplayed again(just not changing the letter thats it😂). If correct morse string is entered then, displayed character is changed.
`next button`: Generated another ASCII character.