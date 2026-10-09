var profile = 0;
var username = "cookie";
var pfp = Object.keys(pfps)[5];
let params = new URLSearchParams(document.location.search);

function Start() {
    Object.keys(pfps).forEach(key => {
        var option = document.createElement("option");
        option.text = key;
        document.getElementById("pfp").add(option);
    });
    
    Load();
    if (params.has("code")) {
        JoinGame(params.get("code"))
    }
}

function CreateGame() {
    const message = {
        id: clientToServerMessageIds.CREATE_GAME,
        cookie: document.cookie
    }
    websocket.send(JSON.stringify(message));
}

function GetGameCode() {
    return document.getElementById("gamecode").value;
}

function JoinGame() {
    JoinGameWithCode(GetGameCode())
}

function JoinGameWithCode(code) {
    const message = {
        id: clientToServerMessageIds.JOIN_GAME,
        cookie: document.cookie,
        code: code,
    }
    websocket.send(JSON.stringify(message));
}

function Save() {
    var temp1 = String(document.getElementById("username").value);
    if (temp1.length < 3 && temp1.length > 16) {
        console.error("invalid name");
        alert("invalid name")
        return;
    }
    pfp = document.getElementById("pfp").value;
    username = temp1;
    document.cookie = JSON.stringify({ username: username, pfp: pfp })
    alert("saved")
    UpdateHTML(true);
}

function Load() {
    if(document.cookie.length < 1) {
        UpdateHTML(true);
        Save();
        return;
    }
    json = JSON.parse(document.cookie);
    username = json["username"]
    pfp = json["pfp"]
    UpdateHTML(true);
}

function UpdateHTML(updateCrucial = false){
    if(updateCrucial){
        document.getElementById("username").value = username;
        document.getElementById("pfp").value = pfp;
    }
    document.getElementById("mepfp").src = pfps[pfp];
    document.getElementById("me").innerText = username;
}

function RandomRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}