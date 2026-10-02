import asyncio
import websockets
import json
import uuid

from network import ClientToServerMessageIds, ServerToClientMessageIds
from room import Room
from player import Player
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
                    room.addPlayer(Player(connection, message["username"], 1))
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_CREATED,
                        "code": room.code
                    }))
                case ClientToServerMessageIds.JOIN_GAME:
                    print("Client requested to join a game with username:", message["username"], "with code:", message["code"])
                    code = message["code"]
                    if code not in rooms:
                        await connection.send(json.dumps({
                            "id": ServerToClientMessageIds.ERROR,
                            "message": "Room not found"
                        }))
                        pass
                    rooms[code].addPlayer(Player(connection, message["username"], 2))
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_JOINED,
                        "otherPlayer": rooms[code].players[0].username,
                        "code": code
                    }))
        except Exception as e:
            print(e)
            # await connection.send(json.dumps({
            #                             "id": ServerToClientMessageIds.ERROR,
            #                             "message": "Room not found"
            #                         }))
            await connection.close()
            break;
    print("Client disconnected", connection.remote_address)

async def startAsync():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()

def start():
    asyncio.run(startAsync())


def  CreateRoom(status):
    code = str(uuid.uuid4())[:6]
    if code not in rooms:
        room = Room(code, status)
        rooms[code] = room
        return room
    else:
        return CreateRoom(status)


start();