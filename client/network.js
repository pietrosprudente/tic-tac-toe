const wsUri = "ws://localhost:8000/"
const websocket = new WebSocket(wsUri)
websocket.onmessage = function (event) {
    const message = JSON.parse(event.data)
    console.log("Received from server:", message)
    switch (message.id) {
        case serverToClientMessageIds.GAME_CREATED:
            console.log("Game created with code:", message.code)
            window.location.href = "game.html"
            break;
        case serverToClientMessageIds.GAME_JOINED:
            console.log("Joined game with code:", message.code)
            window.location.href = "game.html"
            break;
        case serverToClientMessageIds.ERROR:
            console.error("Error from server:", message.error)
            window.location.href = "index.html"
            break;
    }
}
const clientToServerMessageIds = {
    CREATE_GAME: 0,
    JOIN_GAME: 1,
    PLACE_MARK: 2,
}
const serverToClientMessageIds = {
    ERROR: -1,
    GAME_CREATED: 0,
    GAME_JOINED: 1,
    UPDATE_BOARD: 2,
}