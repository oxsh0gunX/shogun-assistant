
"""
Shogun Assistant - Prototype 2

Updates:
- Added logging system
- Added global and wake-word exit handling
- Added fuzzy command matching
- Fixed input space normalization
- Improved command execution flow

Author: Safvan (0xSh0gunX)
"""



import subprocess
import logging
import sys
from difflib import get_close_matches  #fuzzing 

WAKE_WORD = "shogun"

COMMANDS = {
    "open terminal": ["terminator"],
    "open brave": ["brave-browser"],
    "open btop": ["terminator", "-e", "btop --utf-force"]
}


logging.basicConfig(
    filename="shogun.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_command(text):
    text = text.lower().strip()

    if WAKE_WORD not in text:
        return None

    text = text.replace(WAKE_WORD, "", 1).strip()
    return " ".join(text.split())


def execute_command(command):

     # exit whith wake
    if command == "exit":
        print("[Shogun]: Shutting down.")
        logging.info("Assistant exited (wake word).")
        sys.exit(0)
    

    if command == "help":
     print("Available commands:")
    for cmd in COMMANDS:
        print("-", cmd)
    return


    if command in COMMANDS:
        try:   #for exact match 
            subprocess.Popen(COMMANDS[command])
            logging.info(f"Executed command: {command}")
            print(f"[Shogun]: Executed '{command}'")
        except FileNotFoundError:
            logging.error(f"Application not found: {command}")
            print("[Shogun]: Application not found.")
        return  

    # Fuzz
    matches = get_close_matches(command, COMMANDS.keys(), n=1, cutoff=0.6)

    if matches:
        best_match = matches[0]
        try:
            subprocess.Popen(COMMANDS[best_match])
            logging.info(f"Fuzzy matched '{command}' to '{best_match}'")
            print(f"[Shogun]: Did you mean '{best_match}'? Executing...")
        except FileNotFoundError:
            logging.error(f"Application not found (fuzzy): {best_match}")
            print("[Shogun]: Application not found.")
    else:
        logging.warning(f"Unknown command attempt: {command}")
        print(f"[Shogun]: Command not recognized: '{command}'")


if __name__ == "__main__":
    print(f"MyShogun Prototype Online. Wake word: '{WAKE_WORD}'")

    while True:
        user_input = input("You: ").lower().strip()

        #exit whith user_input
        if user_input in ["exit", "poweroff", "power off", "shutdown", "shut down"]:
            print("[Shogun]: Shutting down.")
            logging.info("Assistant exited (global).")
            sys.exit(0)

        command = parse_command(user_input)

        if command:
            execute_command(command)