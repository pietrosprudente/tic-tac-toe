const wsUri = "ws://localhost:8000/";
const websocket = new WebSocket(wsUri);

var username = "Player" + RandomRange(1000, 9999);

function Start(){
    Load();
}

function CreateGame() {
    const message = {
        id: 0,
        username: username
    }
    websocket.send(JSON.stringify(message));
}

function JoinGame(code) {
    const message = {
        id: 1,
        code: code
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