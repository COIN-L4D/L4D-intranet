(function(){

  var elts = {}
  var state;

  function initialize(){
    elts.gameState = document.getElementById("game-state")
    elts.playPauseBtn = document.getElementById("play-pause-btn")
    elts.stopBtn = document.getElementById("stop-btn")
    elts.notifsList = document.getElementById("notifs-list")
    elts.clearNotifsBtn = document.getElementById("notifs-clear-btn")


    bindEvents()
    loadCurrentState()
    setInterval(function () {
      loadCurrentState()
    }, 5000);
  }

  function bindEvents(){
    elts.playPauseBtn.onclick = function(){
      if (typeof state === 'undefined'){
        return ;
      }

      if (state == 'Run'){
        touchGameStateAPI('/api/pause')
      }
      else if (state == 'Pause' || state == 'Stop'){
        touchGameStateAPI('/api/start')
      }
    }

    elts.stopBtn.onclick = function(){
      touchGameStateAPI('/api/stop')
    }

    elts.clearNotifsBtn.onclick = function(){
      elts.notifsList.innerHTML = ""
    }
  }

  function touchGameStateAPI(url){
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
      if (xhttp.readyState == 4){
        if (xhttp.status == 200){
          var response = JSON.parse(xhttp.responseText)
          if (response.error == true){
            notify("error requesting " + url + ": " + response.error_info)
          }
          else {
            loadCurrentState()
          }
        }
        else{
          notify("request on " + url + " returns error code " + xhttp.status)
        }
      }
    }

    xhttp.open("GET", url, true)
    xhttp.send()
  }

  function loadCurrentState(){
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
      if (xhttp.readyState == 4){
        if (xhttp.status == 200){
          var response = JSON.parse(xhttp.responseText)
          if (response.error == true){
            notify("error requesting /api/status: " + response.error_info)
          }
          else {
            updateState(response.state)
          }
        }
        else{
          notify("request on /api/status returns error code " + xhttp.status)
        }
      }
    }

    xhttp.open("GET", "/api/status", true)
    xhttp.send()
  }

  function notify(notif){
    var e = document.createElement('p')
    var e_btn = document.createElement('button')
    e.textContent = notif + " | "
    e_btn.textContent = 'x'
    e_btn.onclick = function(){
      e.remove();
    }
    e.appendChild(e_btn)
    elts.notifsList.appendChild(e)
  }

  function updateState(newState){
    state = newState;
    elts.gameState.textContent = state;
    if (state == 'Run'){
      elts.playPauseBtn.textContent = 'Pause'
    }
    else if (state == 'Pause' || state == 'Stop'){
      elts.playPauseBtn.textContent = 'Play'
    }
    else {
      notify("error: unreconized game state")
    }
  }

  window.addEventListener('load', initialize)
})()
