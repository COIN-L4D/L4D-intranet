/*
fonctionnement de l'api :
 getList() qui renvoie un "tableau" t t.listInitial qui renvoie la liste initial des pages de bases et t.listReveal la liste des pages révélés en plus des pages de bases.
 tryPassword(string le mot de passe, fonction x à utiliser) 
 la fonciton x doit prendre en premier paramètre le boolean qui dit si le mot de passe est correct
 et en deuxièeme paramètre un tableau de ce type : {"path": "/page/secret-1", "name": "Secret 1"}
*/
var apiAjax = {};

apiAjax.serveur = "http://l4d.dbarth.eu";

apiAjax.listInitial = [];
apiAjax.listeReveal = [];

apiAjax.setupListeners = function(){
	apiAjax.retrieveList();
}
window.addEventListener("load", apiAjax.setupListeners);

apiAjax.getList =  function(){
	return {listInitial : apiAjax.listInitial, listeReveal : apiAjax.listeReveal};	
}

apiAjax.retrieveList = function (){

	setInterval(function(){
		var requ = new XMLHttpRequest();
		requ.open("GET",apiAjax.serveur+"/api/menu",true);
		requ.addEventListener("load", apiAjax.updateList);
		requ.addEventListener("error", apiAjax.error);
		requ.send(null);
	}, 5000);

}

apiAjax.updateList = function(){
	var res = JSON.parse(this.responseText);
	if (res.error == true){
		console.log(res.error_info);
	}
	else{
		apiAjax.listInitial = res.initial;
		apiAjax.listeReveal = res.reveal;
	}
}

apiAjax.error = function() {
	console.log("erreur d'accèss au serveur");
}

apiAjax.tryPassword = function(password, callback){
	var requ = new XMLHttpRequest();
	requ.open("GET", apiAjax.serveur+"/api/try"+"?password="+password,true);
	requ.addEventListener("load", function(){
		var res = JSON.parse(this.responseText);
		if (res.error == true){
			console.log(res.error_info);
		}
		callback(res.granted, res.page);
	});
	requ.addEventListener("error", apiAjax.error);
	requ.send("password="+ password);
}




