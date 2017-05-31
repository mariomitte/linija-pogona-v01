function led() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=led", true);
  xhttp.send();
}

function fwd() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=fwd", true);
  xhttp.send();
}

function left() {
  document.getElementById("signali-gore").style.backgroundColor = '#5cb85c';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=left", true);
  xhttp.send();
}

function pause() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=pause", true);
  xhttp.send();
}

function right() {
  document.getElementById("signali-dolje").style.backgroundColor = '#5cb85c';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=right", true);
  xhttp.send();
}

function bwd() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=bwd", true);
  xhttp.send();
}

function speed_up() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=up", true);
  xhttp.send();
}

function speed_down() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=down", true);
  xhttp.send();
}

function stop_linija() {
  document.getElementById("signali-gore").style.backgroundColor = '#ef2929';
  document.getElementById("signali-dolje").style.backgroundColor = '#ef2929';
  document.getElementById("signali-stol").style.backgroundColor = '#ef2929';
  document.getElementById("signali-obrada").style.backgroundColor = '#ef2929';
  document.getElementById("signali-ciklus").style.backgroundColor = '#ef2929';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=stop", true);
  xhttp.send();
}

function record() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=record", true);
  xhttp.send();
}

function stop_record() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=stop-record", true);
  xhttp.send();
}

function take_photo() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=take-photo", true);
  xhttp.send();
}

function clear() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=clear", true);
  xhttp.send();
}

function motor_stol() {
  document.getElementById("signali-stol").style.backgroundColor = '#5cb85c';
  document.getElementById("signali-goredolje").style.backgroundColor = '#ffffff';
  document.getElementById("signali-obrada").style.backgroundColor = '#ffffff';
  document.getElementById("signali-stol").style.backgroundColor = '#5cb85c';
  document.getElementById('rucno_motor').innerHTML = 'Motor - Stol';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=motor-stol", true);
  xhttp.send();
}

function motor_goredolje() {
  document.getElementById("signali-stol").style.backgroundColor = '#ffffff';
  document.getElementById("signali-goredolje").style.backgroundColor = '#5cb85c';
  document.getElementById("signali-obrada").style.backgroundColor = '#ffffff';
  document.getElementById("signali-gore").style.backgroundColor = '#e9b96e';
  document.getElementById("signali-dolje").style.backgroundColor = '#e9b96e';
  document.getElementById('rucno_motor').innerHTML = 'Motor - Gore/Dolje';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=motor-goredolje", true);
  xhttp.send();
}

function motor_obrada() {
  document.getElementById("signali-stol").style.backgroundColor = '#ffffff';
  document.getElementById("signali-goredolje").style.backgroundColor = '#ffffff';
  document.getElementById("signali-obrada").style.backgroundColor = '#5cb85c';
  document.getElementById("signali-obrada").style.backgroundColor = '#5cb85c';
  document.getElementById('rucno_motor').innerHTML = 'Motor - Obrada';
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=motor-obrada", true);
  xhttp.send();
}

function send_mail() {
}
