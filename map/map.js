//initialisation de mapbox
L.mapbox.accessToken = 'pk.eyJ1IjoiYWx0b3IiLCJhIjoiY2llemxlMGU1MDBvanN1bTQxamszcHE5cSJ9.l021dXTkSGn9z-xUXDdreQ';
var map = L.mapbox.map('map', 'mapbox.dark', {attributionControl: false})
    .setView([50.609283, 3.142132], 16);

//initialisation des events
var xhr = new XMLHttpRequest();

xhr.onload = function(e){
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
	var response = JSON.parse(xhr.responseText);
	var geojson = response.map(function(data, i, tab){
	    return data_to_geomarker(data);
	});
	map.featureLayer.setGeoJSON(geojson);
    }
};

//rafraichissement de la map
setInterval(function (){
    xhr.open('GET', 'http://l4d.dbarth.eu/map/events', true);
    xhr.send(null);
}, 5000);


function type_to_desc(type){
    if(type == "mutagene")
	return {
	    size: 'large',
	    color: '#10C200',
	    symbol: 'chemist'
	};
    else if(type == "arme")
	return {
	    size: 'large',
            color: '#DE0F04',
            symbol: 'logging'
	};
    else if(type == "pc")
	return {
	    size: 'large',
            color: '#7A726E',
            symbol: 'embassy'
	};
    else if(type == "potion")
	return {
	    size: 'large',
            color: '#f1f075',
            symbol: 'hospital'
	};
    else if(type == "info")
	return {
	    size: 'large',
            color: '#1087bf',
            symbol: 'post'
	};
    
}

function data_to_geomarker(data){

    var desc = type_to_desc(data.type)

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
            'marker-size': desc.size,
            'marker-color': desc.color,
            'marker-symbol': desc.symbol
	}
    };
}
