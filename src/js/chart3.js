
$.getJSON( "data/chartdata/chart3.json", function( data ) {
    var JSONseries = JSON.stringify(data[0])
    var jsseries = JSON.parse(JSONseries)
    var JSONcateg = JSON.stringify(data[1])
    var jscateg = JSON.parse(JSONcateg)
    Highcharts.chart('container3', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Proximates per Major Food Groups'
        },
        xAxis: {
            categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
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
        series: [{
            name: 'John',
            data: [5, 3, 4, 7, 2]
        }, {
            name: 'Jane',
            data: [2, 2, 3, 2, 1]
        }, {
            name: 'Joe',
            data: [3, 4, 4, 2, 5]
        }]
    });