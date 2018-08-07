$.getJSON( "data/chartdata/chart4.json", function( data ) {
    var JSONseries = JSON.stringify(data[0])
    var jsseries = JSON.parse(JSONseries)
    var JSONdrilldown = JSON.stringify(data[1])
    var jsdrillseries = JSON.parse(JSONdrilldown)
    Highcharts.chart('container4', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Highest Water Content Food per Food Group'
        },
        xAxis: {
            type: 'Food groups'
        },
        yAxis: {
            title: {
                text: 'Rate of mass of water (g)'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}g'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}g</b> mean<br/>'
        },

        "series": jsseries,
        "drilldown": {
            "series": jsdrillseries
        }
    });
});