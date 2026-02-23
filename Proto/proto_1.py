import subprocess  

WAKE_WORD = "shogun"    
COMMANDS = {
    "open terminal": ["terminator"],    
    "open brave": ["brave-browser"],
    "open btop": ["terminator", "-e" , "btop --utf-force"]}

def parse_command(text):
    text = text.lower()  
    if WAKE_WORD not in text:
        return None
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
if __name__ == "__main__":
    print(f"myShogun Prototype Online. Wake word: '{WAKE_WORD}'")

    while True:
        user_input = input("You: ")
        command = parse_command(user_input)

        if command:
            execute_command(command)
