from server import start, shutdown
print("tic-tac-toe server terminal has opened !!");


while True:
    _input = input("Next, type HELP to see the list of commands: ");
    match _input.lower():
        case "help":
            print("List of commands:");
            print("start - starts a server on port 8000");
            print("shutdown - shuts down the server");
            print("kill - shuts down the server and the program");
        case "start":
            print("Server is starting...");
            start();
        case "shutdown":
            print("Server is shutting down...");
            shutdown();
        case "kill":
            print("Server and Program is shutting down...");
            shutdown();
            break;