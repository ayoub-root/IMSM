function chart(type, data){
//alert(data[1])
var dps = []; // dataPoints

var chart = new CanvasJS.Chart("chartContainer", {
	title :{
		text: "Dynamic Data"
	},
	axisY: {
		includeZero: false
	},
	data: [{type: type, dataPoints:dps}]
});

var xVal = 0;
var yVal = 100;
var updateInterval = 1000;
var dataLength = 200; // number of dataPoints visible at any point

var updateChart = function (count) {

	count = count || 1;

	for (var j = 0; j < count; j++) {
		//yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
		dps.push({
			x: data[0]+Math.round(5 + Math.random() *(-5-5)),
			y: data[1]+Math.round(5 + Math.random() *(-5-5))
		});

	}



	chart.render();
};

updateChart(dataLength);
setInterval(function(){updateChart(200)}, updateInterval);

}