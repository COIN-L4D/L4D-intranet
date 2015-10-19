//initialisation de mapbox
L.mapbox.accessToken = 'pk.eyJ1IjoiYWx0b3IiLCJhIjoiY2llemxlMGU1MDBvanN1bTQxamszcHE5cSJ9.l021dXTkSGn9z-xUXDdreQ';
var map = L.mapbox.map('map', 'mapbox.streets')
    .setView([50.609283, 3.142132], 16);

//recuperation des element du DOM
var content = document.getElementById('content');
var coordinates = document.getElementById('coord');
var form = document.getElementById('form');
var button = document.getElementById('button');





//initialisation des event
button.addEventListener('click', function(){
    var ul = form.firstElementChild;

    var result = ul_fold(ul, {}, function(elem, acc){

	
	var input = elem.firstElementChild.firstElementChild;
	acc[input.name] = input.value;
	console.log(acc);
	return acc;
    });

    var m = marker.getLatLng();
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://l4d.dbarth.eu/map/push');
    xhr.send('lat=' + m.lat + '&lng=' + m.lng + '&title=' + result.title + '&description=' + result.description + '&type=' + result.type);
    updateMarker();
}, false);

//creation du marqueur dragable
var marker = L.marker([50.609283, 3.142132], {
    icon: L.mapbox.marker.icon({
      'marker-color': '#f86767'
    }),
    draggable: true
}).addTo(map);

marker.on('dragend', ondragend);

//affichage des coordonée du marqueur
ondragend();

//boucle évenementiel
updateMarker();





function ondragend() {
    var m = marker.getLatLng();
    coordinates.innerHTML = '<ul><li>Latitude: ' + m.lat + '</li><li>Longitude: ' + m.lng + '</li><ul>';
}

function updateMarker(){
    
    var xhr = new XMLHttpRequest();
    xhr.addEventListener('readystatechange', function(){
	if (xhr.readyState === xhr.DONE && xhr.status === 200) {
	    var response = JSON.parse(xhr.responseText);
	    var geojson = response.map(function(data, i, tab){
		var ret = data_to_geomarker(data);
		return ret;
	    });
	    map.featureLayer.setGeoJSON(geojson);

	}
    }, false);

    
    xhr.open('GET', 'http://l4d.dbarth.eu/map/events');
    xhr.send();
}

function data_to_geomarker(data){
    return {
	type: 'Feature',
	geometry: {
            type: 'Point',

            coordinates: [
		data.position.lng,
		data.position.lat
            ]
	},
	properties: {
            title: data.title,
            description: data.description,
            'marker-size': 'large',
            'marker-color': '#BE9A6B',
            'marker-symbol': 'cafe'
	}
    };
}

function ul_fold(ul_node, acc_init, fun){

    function aux(elem, acc){
	var acc2 = fun(elem, acc);
	if(!elem.nextElementSibling)
	    return acc2;
	return aux(elem.nextElementSibling, acc2);
    }
    return aux(ul_node.firstElementChild, acc_init);
}


