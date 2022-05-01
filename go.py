from bearlibterminal import terminal as term
# reads a single char beside specified prompt, which is shown at specified position
# default position is bottom row of current term display
# TODO: don't require [enter] after single-char input
def single_input(prompt, colPos=-1, rowPos=-1):
    if colPos == -1:
        colPos = 1
    if rowPos  == -1:
        rowPos = term.state(term.TK_HEIGHT) - 1
    term.printf(colPos, rowPos, prompt)
    inlineKey = ''
    key = term.read_str(len(prompt) + colPos + 1, rowPos, inlineKey, 1)
    return key[1]
term.open()
term.printf(1, 1, 'Hello, world! Use q to quit.')
key = single_input('your choice: ')
term.printf(1, 2, 'You entered: ' + key)
if key != 'q': 
    single_input('hit any key to exit')
term.close()