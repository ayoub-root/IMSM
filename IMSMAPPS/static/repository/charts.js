function chart(type,parameters, data){

var dps = []; // dataPoints
	var dataa=[];
var chart = new CanvasJS.Chart("chartContainer", {
	title :{
		text: "Dynamic Data"
	},
	axisY: {
		includeZero: false
	},
	data: dataa
});

var xVal = 0;
var yVal = 100;
var updateInterval = 1000;
var dataLength = 20; // number of dataPoints visible at any point

var updateChart = function (count) {

	count = count || 1;

	for (var j = 0; j < count; j++) {
		//yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
		dps.push({
			x: data[0],
			y: data[1]
		});

	}

	if (dps.length > dataLength) {
	//	dps.shift();
	}

	chart.render();
};

updateChart(dataLength);
setInterval(function(){updateChart(20)}, updateInterval);

}