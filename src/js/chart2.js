$.getJSON( "data/chartdata/chart2.json", function( data ) {
    var JSONstr = JSON.stringify(data)
    var jsdata = JSON.parse(JSONstr)
    Highcharts.chart('container2', {
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: 'Map of Energy and Protein per 100 g'
            // warna nunjukin food category
        },
        xAxis: {
            title: {
                enabled: true,
                text: 'Protein (g)'
            },
            startOnTick: true,
            endOnTick: true,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: 'Energy (kcal)'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 260,
            y: 50,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
            borderWidth: 1
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    pointFormat: '{point.x} g, {point.y} kcal'
                }
            }
        },
        series: jsdata
    });
});