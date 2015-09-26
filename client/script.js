var nbDialogs;

function onEnterPrompt(event) {
	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		interpretCommand($('#prompt').val());
	}
}


function interpretCommand(command) {
	var commands = {};
	commands["help"] = commandHelp;
	commands["open"] = commandOpen;
	
	println("h4kers@cia.confidential $ " + command);
	if(commands[command]) {
		commands[command]();
	};
	
	$('#prompt').val('');
	
	//scroll down the page
	window.scrollTo(0,document.body.scrollHeight);
}

function commandHelp() {
	println("Voici la liste des commandes disponibles : ");
	println('tapez "Open" pour ouvrir une nouvelle fenêtre');
}

function commandOpen() {
	createIframeDialog("page2.html");
}

function createIframeDialog(url) {
	
	// adding html dialog
	var idDialog = "dialog" + nbDialogs;
	$("#dialogs").append('<div id="' + idDialog + '" title="page trop importante">'
	+ '<iframe frameBorder="0" src="page1.html"></iframe>'
	+ '</div>');
    $( "#" + idDialog ).dialog();	
	nbDialogs++;
}

function println(line) {
	$('#content').append(line + "<br />");
}

function setFocusPrompt() {
	$('#prompt').focus();
}

$(document).ready(function() {
	
	var nbDialogs = 0;
	
	$('#prompt').keypress(onEnterPrompt);
	$(window).click(setFocusPrompt);
	
});



