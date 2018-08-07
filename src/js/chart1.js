$.getJSON( "data/chartdata/chart1.json", function( data ) {
    var JSONseries = JSON.stringify(data[0])
    var jsseries = JSON.parse(JSONseries)
    var JSONdrilldown = JSON.stringify(data[1])
    var jsdrillseries = JSON.parse(JSONdrilldown)
    Highcharts.chart('container1', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Percentage of Food Groups'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    },

    "series": jsseries,
    "drilldown": {
        "series": jsdrillseries
    }
    });
});