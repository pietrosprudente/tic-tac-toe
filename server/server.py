import asyncio
import threading
import websockets

async def handler(connection):
    print("Client connected")
    while True:
        try:
            message = await connection.recv()
            print("Received from client:", message)
        except:
            break;
    print("Client disconnected")

async def server():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()  # Run forever

serverThread = threading.Thread(target=asyncio.run, args=(server(),));

def start():
    if serverThread.is_alive():
        print("Server is already running.")
        return
    serverThread.start()

def shutdown():
    if not  serverThread.is_alive():
        print("Server is not running.")
        return
    isRunning = False
    serverThread.join()
    for task in asyncio.all_tasks():
        task.cancel()