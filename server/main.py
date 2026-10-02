import asyncio
import websockets
import json
import random
from network import ClientToServerMessageIds, ServerToClientMessageIds
from room import Room
rooms = {}

async def handler(connection):
    print("Client connected", connection.remote_address)
    while True:
        try:
            data = await connection.recv()
            print("Received from client:", data)
            message = json.loads(data)
            match message["id"]:
                case ClientToServerMessageIds.CREATE_GAME:
                    print("Client requested to create a game with username:", message["username"])
                    room = CreateRoom("waiting")
                    room.addPlayer(connection, message["username"], 1)
                    rooms[room.code] = room
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_CREATED,
                        "code": room.code
                    }))
                case ClientToServerMessageIds.JOIN_GAME:
                    print("Client requested to join a game with username:", message["username"], "with code:", message["code"])
                    code = message["code"]
                    if rooms[code] is None:
                        await connection.send(json.dumps({
                            "id": ServerToClientMessageIds.ERROR,
                            "message": "Room not found"
                        }))
                        pass
                    rooms[code].addPlayer(connection, message["username"], 2)
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_JOINED,
                        "otherPlayer": rooms[code].players[0].username,
                        "code": code
                    }))
        except Exception as e:
            print("Error occurred:", e, "Closing connection")
            await connection.close()
            break;
    print("Client disconnected", connection.remote_address)

async def startAsync():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()

def start():
    asyncio.run(startAsync())


def CreateRoom(status):
    code = str(random.randint(100000, 999999))
    if(rooms[code] is None):
        room = Room(code, status)
        rooms[code] = room
        return room
    else:
        return CreateRoom(status)


start();