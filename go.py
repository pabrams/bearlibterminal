from bearlibterminal import terminal as term

def single_input(prompt='', colPos=1, rowPos=-1):
    """
        Reads a single char beside specified prompt, which is shown at the specified position.
        Default prompt is empty.
        Default position is bottom row of current term display, first column.
    """
    if rowPos  == -1:
        rowPos = term.state(term.TK_HEIGHT) - 1
    term.printf(colPos, rowPos, prompt)
    term.refresh()
    key = term.read()
    if key == term.TK_CLOSE:
        exit
    return chr(term.state(term.TK_WCHAR))

term.open()
term.refresh()
term.printf(1, 1, 'Hello, world! Use q to quit.')
key = single_input('your choice: ')
if key != 'q': 
    term.printf(1, 2, 'You entered: ' + key)
    single_input('enter to exit')
term.close()