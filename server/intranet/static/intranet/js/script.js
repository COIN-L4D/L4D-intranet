(function(){
	var nbDialogs = 0;
	var pages = [];
	var ENDPOINT = "";


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
		commands["password"] = commandPassword;

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
		println("Liste des pages dévérouillées");
		for(var i = 0 ; i < pages.length ; i++) {
			println("* - " + pages[i].name);
		}
	}

	function commandHelp() {
		println("Voici la liste des commandes disponibles : ");
		println(' - Tapez "menu" pour afficher la liste des pages dévérouillées.');
		println(" - Tapez \"open\" suivi du nom d'une page pour y accéder.");
		println(" - Tapez \"passsword\" suivi d'un mot de passe pour tenter de hacker une page.");
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
			println("ERROR: PERMISSION DENIED");
		}
	}

	function commandPassword(password){
		var xhr = new XMLHttpRequest();

		if (typeof password == "undefined" || password.length == 0){
			println("ERROR: PASSWORD REQUIRED")
			return ;
		}

		xhr.onload = function(e){
			if (xhr.readyState == xhr.DONE && xhr.status == 200){
				var response = JSON.parse(xhr.responseText);
				if (response.granted == true){
					println("ACCESS GRANTED: " + response.page.name)
					println('Tapez "open ' + response.page.name + '" pour ouvrir cette nouvelle page')
				}
				else {
					println("ERROR: ACCESS DENIED")
				}
			}
		}

		xhr.open("GET", "/api/try?password="+password);
		xhr.send(null);
	}

	function println(line) {
		$('#content').append(line + "<br />");
	}

	function setFocusPrompt() {
		$('#prompt').focus();
	}

	$(document).ready(function() {

		nbDialogs = 0;

		refreshPages();
		setInterval(refreshPages, 5000);

		$('#prompt').keypress(onEnterPrompt);
		$(window).click(setFocusPrompt);

	});
})()
