import subprocess  #it help to run the linux comands
          # subprocess.Popen(["terminator"])    it open the terminal form the python 


# ======================
# CONFIG
# ======================
WAKE_WORD = "shogun"    #  raiden is whatching 

COMMANDS = {
    "open terminal": ["terminator"],    #left what usr say      spoken command : system command
    "open brave": ["brave-browser"],
    "open btop": ["terminator", "-e" , "btop --utf-force"]
}

# ======================
# CORE LOGIC
# ======================
def parse_command(text):
    text = text.lower()   #lower

    if WAKE_WORD not in text:
        return None

    # Remove wake word
    text = text.replace(WAKE_WORD, "").strip()

    return text


def execute_command(command):
    if command in COMMANDS:
        try:
            subprocess.Popen(COMMANDS[command])
            print(f"[Shogun]: Executed '{command}'")
        except FileNotFoundError:
            print("[Shogun]: Application not found.")
    else:
        print(f"[Shogun]: Command not recognized.'{command}'")


# ======================
# MAIN LOOP (TEXT MODE)
# ======================
if __name__ == "__main__":
    print(f"myShogun Prototype Online. Wake word: '{WAKE_WORD}'")

    while True:
        user_input = input("You: ")
        command = parse_command(user_input)

        if command:
            execute_command(command)
