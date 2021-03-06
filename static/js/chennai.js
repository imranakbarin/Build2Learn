var myChartChennai;

function plotChennaiChartSeries(dict_Chennai) {

    var myChartChennai = document.getElementById("ChartChennai").getContext("2d");
    myChartChennai = new Chart(myChartChennai, {
        type: 'line',
        data: {
            labels: dict_Chennai['date'],
            datasets: [
                /*{
                                    label: 'Total',
                                    data: dict_Chennai['confirmedCases'],
                                    backgroundColor: "#d1971b",
                                    steppedLine: false,
                                    borderColor: "#d1971b",
                                    fill: false,
                                },*/
                {
                    label: 'Hospitalized',
                    data: dict_Chennai['hospitalized'],
                    backgroundColor: "#0a8af2",
                    steppedLine: false,
                    borderColor: "#0a8af2",
                    fill: false,
                    borderWidth: 1,
                    pointHitRadius: 30,
                },
                {
                    label: 'Recovered',
                    data: dict_Chennai['recovered'],
                    backgroundColor: "#228734",
                    steppedLine: false,
                    borderColor: "#228734",
                    fill: false,
                    pointHitRadius: 30,
                    borderWidth: 1,

                }, {
                    label: 'Deceased',
                    data: dict_Chennai['deceased'],
                    backgroundColor: "#e61515",
                    steppedLine: false,
                    borderColor: "#e61515",
                    fill: false,
                    pointHitRadius: 30,
                    borderWidth: 1
                },


            ]
        },

        options: {
            responsive: true,
            legend: {
                display: true,
                labels: {
                    fontColor: 'rgb(2, 37, 41)'
                },

            },
            scales: {
                yAxes: [{
                    ticks: {
                        fontSize: 9,
                        fontFamily: "'Roboto', sans-serif",
                        fontColor: '#000',
                        fontStyle: '500'
                    },

                    gridLines: {
                        display: false
                    },
                    // scaleLabel: {
                    //     display: true,
                    //     labelString: 'Count'
                    // }
                }],
                xAxes: [{
                    //  barPercentage: 0.4,

                    ticks: {
                        fontSize: 9,
                        fontFamily: "'Roboto', sans-serif",
                        fontColor: '#000',
                        fontStyle: '500'
                    },
                    gridLines: {
                        display: false
                    },
                    // scaleLabel: {
                    //     display: true,
                    //     labelString: 'Date'
                    // }
                }]
            },
            title: {
                display: true,
                text: 'Chennai Last 30 days'
            },
            elements: {
                point: {
                    pointStyle: 'cross'
                }
            }
        }
    });

}