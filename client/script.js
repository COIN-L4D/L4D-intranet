var nbDialogs;
var pages;
var ENDPOINT = "http://l4d.dbarth.eu";


function onEnterPrompt(event) {
	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		interpretCommand(parseCommand($('#prompt').val()));
	}
}

function refreshPages() {
	$.get( ENDPOINT + "/api/menu", function(data) {
		pages = data.initial.concat(data.reveal);
		console.log(pages);
	});
}

function getPathFromPageName(pageName) {
	for(var i = 0 ; i < pages.length ; i++) {
		if(pages[i].name.toLowerCase() === pageName) {
			return pages[i].path;
		}
	}
	return undefined;
}

function parseCommand(input) {
	if(input.trim() === "") {
		println("h4kers@cia.confidential $ " + input);
		return {"name": "", "parameters": ""};
	}
	
	var regex = new RegExp("(\\w+)([\\s\\S]*)", "g");
	var match = regex.exec(input);
	if(match.length < 3) {
		match.push("");
	}
	println("h4kers@cia.confidential $ " + input);
	return {"name": match[1], "parameters": match[2].trim().toLowerCase()};
}

function interpretCommand(command) {
	var commands = {};
	commands["help"] = commandHelp;
	commands["open"] = commandOpen;
	commands["menu"] = commandMenu;
	
	if(commands[command.name]) {
		commands[command.name](command.parameters);
	} else {
		commandHelp();
	}
	
	$('#prompt').val('');
	
	//scroll down the page
	window.scrollTo(0,document.body.scrollHeight);
}

function commandMenu() {
	println("Liste des menus accessibles : ");
	for(var i = 0 ; i < pages.length ; i++) {
		println("* - " + pages[i].name);
	}
}

function commandHelp() {
	println("Voici la liste des commandes disponibles : ");
	println(' - Tapez "menu" pour afficher la liste des pages disponible.');
	println(' - Tapez "open" puis le nom de la page pour ouvrir une nouvelle fenêtre.');
}

function commandOpen(pageName) {
	// adding html dialog
	var idDialog = "dialog" + nbDialogs;
	var pagePath = getPathFromPageName(pageName);
	if(pagePath) {
		$("#dialogs").append('<div id="' + idDialog + '" title="'+pageName+'">'
		+ '<iframe frameBorder="0" src="'+ENDPOINT + pagePath+'"></iframe>'
		+ '</div>');
		$( "#" + idDialog ).dialog();
		nbDialogs++;
		setFocusPrompt();
	} else {
		println("Aucune page de ce nom à afficher.");
	}
}

function println(line) {
	$('#content').append(line + "<br />");
}

function setFocusPrompt() {
	$('#prompt').focus();
}

$(document).ready(function() {
	
	var nbDialogs = 0;
	
	refreshPages();
	
	$('#prompt').keypress(onEnterPrompt);
	$(window).click(setFocusPrompt);
	
});



