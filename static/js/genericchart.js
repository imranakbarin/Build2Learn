var arr = [];
var activecasesli = [];
var deceasedcasesli = [];
var recoveredcasesli = [];

function assignvalues() {
    arr = [];
    activecasesli = [];
    deceasedcasesli = [];
    recoveredcasesli = [];

    for (var key in test) {
        arr.push(test[key]['date']);
        activecasesli.push(test[key]['hospitalized']);
        deceasedcasesli.push(test[key]['deceased']);
        recoveredcasesli.push(test[key]['recovered']);
    }
    // console.log(arr);
    // console.log(activecasesli);
}

var myChart5;

function plotChartSeries() {


    var mychartsFive = document.getElementById("LineChartSeries").getContext("2d");
    myChart5 = new Chart(mychartsFive, {
        type: 'line',
        data: {
            labels: arr,
            datasets: [{
                    label: 'Active',
                    data: activecasesli,
                    backgroundColor: "#0a8af2",
                    steppedLine: false,
                    borderColor: "#0a8af2",
                    fill: false,
                },
                {
                    label: 'Recovered',
                    data: recoveredcasesli,
                    backgroundColor: "#228734",
                    steppedLine: false,
                    borderColor: "#228734",
                    fill: false,
                }, {
                    label: 'Deceased',
                    data: deceasedcasesli,
                    backgroundColor: "#ff1226",
                    steppedLine: false,
                    borderColor: "#ff1226",
                    fill: false,
                }
            ]
        },

        options: {
            responsive: true,
            legend: {
                display: true,
                labels: {
                    fontColor: '#221d24'
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
                text: ZoneSelected + ' Cases'
            },
            elements: {
                point: {
                    pointStyle: 'star'
                }
            }
        }
    });

}

function UpdateChart(zonename) {
    assignvalues();
    myChart5.config.data.datasets[0].data = activecasesli;
    myChart5.config.data.datasets[1].data = recoveredcasesli;
    myChart5.config.data.datasets[2].data = deceasedcasesli;
    // myChart.config.data.datasets[0].label = case_type + " cases"
    myChart5.config.options.title.text = zonename + " Cases"
    myChart5.update();
};