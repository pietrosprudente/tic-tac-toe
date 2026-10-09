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
                    print("Client requested to create a game:", message["cookie"])
                    room = CreateRoom("waiting")
                    room.hostPlayer =  Player(connection, message["cookie"], 1)
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_CREATED,
                        "code": room.code
                    }))
                case ClientToServerMessageIds.JOIN_GAME:
                    print("Client requested to join a game:", message["cookie"], "with code:", message["code"])
                    code = message["code"]
                    if code not in rooms:
                        await connection.send(json.dumps({
                            "id": ServerToClientMessageIds.ERROR,
                            "message": "Room not found"
                        }))
                        pass
                    rooms[code].guestPlayer = Player(connection, message["cookie"], 2)
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_JOINED,
                        "otherPlayer": rooms[code].players[0].username,
                        "code": code
                    }))
                case ClientToServerMessageIds.PLACE_MARK:
                        myRoom = getRoomFromPlayer(connection)
                        myPlayer = myRoom.getPlayer(connection);
                        if myRoom.game.canPlay(myPlayer):
                            myRoom.game.placeMark(myPlayer);

                        sendUpdateBoard(connection);

                        
        except Exception as e:
            print(e)
            # await connection.send(json.dumps({
            #                             "id": ServerToClientMessageIds.ERROR,
            #                             "message": "Room not found"
            #                         }))
            await connection.close()
            break;
    print("Client disconnected", connection.remote_address)

def getRoomFromPlayer(connection):
    myRoom = Room()
    for x in len(rooms.items):
        if rooms[x].hostPlayer == connection or rooms[x].guestPlayer == connection:
            return Room(rooms[x]);


async def startAsync():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()

async def sendUpdateBoard(room, connection):
    dump = json.dumps({
        "id": ServerToClientMessageIds.UPDATE_BOARD,
        "board": room.game.board,
        "turn": room.game.turn
    })
    await room.hostPlayer.connection.send(dump);
    await room.guestPlayer.connection.send(dump);

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