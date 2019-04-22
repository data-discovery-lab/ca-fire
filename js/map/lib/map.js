//Initialize a map inside a div called map
var map = L.map('map', {
  zoomControl: false,
  scrollWheelZoom: false,
  dragging: false,
  attributionControl: false
}).setView([33.784916499999994,-116.9794525], 5.8); //Input the center location [lat, lon], 10.5 is the zoom level

//merge the two data sets
//dist_num is the region_number, counts means the need level in this region_number
//if you add counts in geojson file, you don't need to do this
for (let i = 0; i < districts.features.length; i++) {
  for (j = 0; j < region_concern.features.length; j++) {
    if (districts.features[i].properties.cartodb_id == region_concern.features[j].region) {
      districts.features[i].properties.count = region_concern.features[j].count;
    }
  }
};

var geojson;
var style_override = {};
var style_target = function (f) {
  return f.properties.count
};

function merge_styles(base, new_styles) {
  for (var attrname in new_styles) {
    base[attrname] = new_styles[attrname];
  }
  return base;
}

//set color palatte
function getColor(d) {
  return d > 90 ? '#67000d' :
    d > 80 ? '#800000' :
    d > 70 ? '#B31B1B' :
    d > 60 ? '#cb181d' :
    d > 50 ? '#FF5700' :
    d > 40 ? '#FF7B00' :
    d > 30 ? '#FF8C00' :
    d > 20 ? '#FFC100' :
    d > 10 ? '#FFE400' :
    d > 0 ? '#F7FF00' : '#ffffff'
};

//attach color palatte to category
function style(feature, color) {
  var target = style_target(feature);
  var fillColor = (!color) ? getColor(target) : color;
  var default_style = {
    fillColor: fillColor,
    weight: 1,
    opacity: 1,
    color: 'grey',
    fillOpacity: 1
  };
  return merge_styles(default_style, style_override);
};

L.geoJson(districts, {
  style: {
    weight: 2,
    fillColor: 'white',
    color: 'black',
  }
}).addTo(map);


function highlightFeature(e) {
  var concerns = [];
  var layer = e.target;
  var needs = []
  //on hover change color from what was defined in function style(feature)
  style_override = {
    weight: 0,
    fillOpacity: 0.8
  };
  geojson.resetStyle(e.target);

  if (!L.Browser.ie && !L.Browser.opera) {
    layer.bringToFront();
  }
  // concerns = (layer.feature.properties.concern.toString().split(','));
}

//reset highlight when hovering out
function resetHighlight(e) {
  style_override = {};
  var layer = e.target;
  geojson.resetStyle(layer);
}

function onEachFeature(feature, layer) {
  layer.on({
    mouseover: highlightFeature,
    mouseout: resetHighlight,
  });
}

var geojson = L.geoJson(districts, {
  style: style,
  onEachFeature: onEachFeature
}).addTo(map);

//create an legend
var legend = L.control({
  position: 'topleft'
});
legend.onAdd = function (map) {
  var div = L.DomUtil.create('div', 'info legend'),
    grades = ['100', '90', '80','70', '60', '50', '40', '30', '20', '10', '0'],
    labels = [];

  // loop through categories and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
    div.innerHTML +=
      '<i style="background:' + getColor(grades[i]) + '"></i> ' +
      grades[i] + '<br>';
  }
  return div;
};
legend.addTo(map);
