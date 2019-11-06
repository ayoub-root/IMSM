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


	chart.render();
};

updateChart(dataLength);
setInterval(function(){updateChart(20)}, updateInterval);

}