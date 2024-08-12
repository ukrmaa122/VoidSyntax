import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():
    print("V͡oi͈ͥd̅͊ͦS̲̻̭y̆ͬ͆n͋̽ͧt̳̚ả͕x̾", flush=True)
    time.sleep(2)
    clear_screen()
    print("Welcome to VoidSyntax!")
    print("""
    ▂▃▄▅▆▇█▓▒░Menu░▒▓█▇▆▅▄▃▂
    1 - Check datebases for Chromium (ip required)
    2 - Check datebases for discord token (discord name required)
    3 - Check datebases for Roblox info
    4 - Check databases for Tdata (Phone number required) ░X░ not working fixing bugs
    -------- 
    Some password or tokens can be false so if you find an issue, go to my github: https://github.com/ukrmaa122/VoidSyntax_EXE/issues
    """)

def check_chromium_database(ip):
    valid_ips = {
        "192.168.0.1": "Chromium Data for IP 192.168.0.1",
        "127.0.0.1": "Test Chromium Data for localhost"
    }
    if ip in valid_ips:
        print(valid_ips[ip])
    else:
        print("Invalid IP. Restarting...")
        return False
    return True

def main():
    while True:
        clear_screen()
        display_intro()
        choice = input("Please select an option: ")
        if choice == '1':
            ip = input("IP? : ")
            if not check_chromium_database(ip):
                continue
            input("Press Enter to restart...")
        elif choice == '3':
            name = input("Name? : ")
            if name in valid_names:
                print(valid_names[name])
            else:
                print("Invalid Name. Restarting...")
                continue
            input("Press Enter to restart...")
        else:
            print("Option not implemented yet or invalid choice. Restarting...")
            time.sleep(2)

if __name__ == "__main__":
    main()