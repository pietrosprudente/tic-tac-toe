import asyncio
import threading
import websockets


async def handler(connection):
    print("Client connected")
    try:
        message = await connection.recv()
        print("Received from client:", message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def server():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()  # Run forever

serverThread = threading.Thread(target=asyncio.run, args=(server(),));

def start():
    serverThread.start()

def shutdown():
    serverThread.join()
    for task in asyncio.all_tasks():
        task.cancel()