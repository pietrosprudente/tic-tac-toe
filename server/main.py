print("tic-tac-toe server terminal has opened !!");

from server import start, shutdown

while True:
    _input = input("Next, type HELP to see the list of commands: ");
    match _input.lower():
        case "start":
            print("Server is starting...");
            start();
        case "help":
            print("List of commands:");
            print("");
        case "kill":
            print("Server is shutting down...");
            shutdown();
            break;