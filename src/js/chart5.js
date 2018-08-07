$.getJSON( "data/chartdata/chart5.json", function( data ) {
    var JSONcateg = JSON.stringify(data[0])
    var jscateg = JSON.parse(JSONcateg)
    var JSONseries = JSON.stringify(data[1])
    var jsseries = JSON.parse(JSONseries)
    Highcharts.chart('container5', {
        chart: {
            type: 'areaspline'
        },
        title: {
            text: 'Average of cholesterol, fatty acid, and fiber of 3 Food Groups'
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 340,
            y: 50,
            floating: true,
            borderWidth: 1,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        xAxis: {
            categories: jscateg
        },
        yAxis: {
            title: {
                text: 'Weight (g)'
            }
        },
        tooltip: {
            shared: true,
            valueSuffix: ' grams'
        },
        credits: {
            enabled: false
        },
        plotOptions: {
            areaspline: {
                fillOpacity: 0.5
            }
        },
        series: jsseries
    });
});
    