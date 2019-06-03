try:
    import readline
except ImportError:
    import pyreadline as readline

CMD = ["January", "February", "March"]

def completer(text, state):
    options = [cmd for cmd in CMD if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while True:
    cmd = input("Please select one from the list above: ")
    if cmd == 'exit':
        break
    print(cmd)
