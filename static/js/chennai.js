var myChartChennai;

function plotChennaiChartSeries(dict_Chennai) {

    var myChartChennai = document.getElementById("ChartChennai").getContext("2d");
    myChartChennai = new Chart(myChartChennai, {
        type: 'line',
        data: {
            labels: dict_Chennai['date'],
            datasets: [{
                    label: 'Total',
                    data: dict_Chennai['confirmedCases'],
                    backgroundColor: "#d1971b",
                    steppedLine: false,
                    borderColor: "#d1971b",
                    fill: false,
                }, {
                    label: 'Hospitalized',
                    data: dict_Chennai['hospitalized'],
                    backgroundColor: "#cf6d38",
                    steppedLine: false,
                    borderColor: "#cf6d38",
                    fill: false,
                },
                {
                    label: 'Recovered',
                    data: dict_Chennai['recovered'],
                    backgroundColor: "#228734",
                    steppedLine: false,
                    borderColor: "#228734",
                    fill: false,
                }, {
                    label: 'Deceased',
                    data: dict_Chennai['deceased'],
                    backgroundColor: "#e61515",
                    steppedLine: false,
                    borderColor: "#e61515",
                    fill: false,
                }

            ]
        },

        options: {
            legend: {
                display: true,
                labels: {
                    fontColor: 'rgb(2, 37, 41)'
                },

            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                    gridLines: {
                        display: false
                    }
                }],
                xAxes: [{
                    //  barPercentage: 0.4,
                    barThickness: 25,
                    maxBarThickness: 40,
                    minBarLength: 20,
                    gridLines: {
                        display: false
                    }
                }]
            },
            title: {
                display: true,
                text: 'Chennai Last 20 days'
            },
            elements: {
                point: {
                    // pointStyle: 'star'
                }
            }
        }
    });

}