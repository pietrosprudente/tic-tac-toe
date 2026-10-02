var username = "Player" + RandomRange(1000, 9999);

function Start(){
    Load();
}

function CreateGame() {
    const message = {
        id: clientToServerMessageIds.CREATE_GAME,
        username: username
    }
    websocket.send(JSON.stringify(message));
}

function GetGameCode(){
    return document.getElementById("gameCode").value;
}

function JoinGame() {
    const message = {
        id: clientToServerMessageIds.JOIN_GAME,
        username: username,
        code: GetGameCode(),
    }
    websocket.send(JSON.stringify(message));
}

function Save() {
    username = document.getElementById("username").value;
}
function Load(){
    document.getElementById("username").value = username;
}

function RandomRange(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}