
$.getJSON( "data/chartdata/chart3.json", function( data ) {
    var JSONcateg = JSON.stringify(data[0])
    var jscateg = JSON.parse(JSONcateg)
    var JSONseries = JSON.stringify(data[1])
    var jsseries = JSON.parse(JSONseries)
    Highcharts.chart('container3', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Rate of Proximates per Major Food Group'
        },
        xAxis: {
            categories: jscateg
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Weight (g)'
            }
        },
        legend: {
            reversed: true
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        series: jsseries
    });
});