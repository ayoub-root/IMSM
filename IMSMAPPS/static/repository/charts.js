function chart(type, data){
alert(data[1])
var dps = []; // dataPoints
	var dataa=[];
var chart = new CanvasJS.Chart("chartContainer", {
	title :{
		text: "Dynamic Data"
	},
	axisY: {
		includeZero: false
	},
	data: dps
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
			x: 33,//data[0],
			y: 334//data[1]+Math.round(5 + Math.random() *(-5-5))
		});

	}



	chart.render();
};

updateChart(dataLength);
setInterval(function(){updateChart(20)}, updateInterval);

}