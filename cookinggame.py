command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Start Cooking!")
    elif command == "stop":
        print("Times Up!")
    elif command == "help":
        print("""
        start- to begin cooking
        stop- to stop cooking
        exit- quit
        """)
    elif command == "exit":
        break
    else:
        print("unknown term.")
