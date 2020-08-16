var myindiaChart;

function plotIndiaChart() {
    var colours = ['#605B56', '#F2FBE0', '#C71585', '#ACC18A', '#F0E68C', '#CD5C5C', '#FFA07A', '#FFC0CB', '#6495ED', '#87CEEB', '#00CED1', '#7cadca', '#F4A460', '#8fc1d1', '#FF6347', '#FF1493', '#8B0000', '#9966CC', '#008080', '#EEE8AA', '#FFE4C4', '#1E90FF', '#FFA07A', '#008B8B', '#B0E0E6', '#ADD8E6', '#6495ED', '#fd9291', '#90EE90', '#f4777f', '#5F9EA0', '#e75d6f', '#e05067', '#B22222', '#cf3759', '#6B8E23', '#ba1d4b', '#778899', '#a1043f', '#2E8B57']

    var myIndiachart = document.getElementById("indiaChart").getContext("2d");
    myindiaChart = new Chart(myIndiachart, {
        type: 'doughnut',
        data: {
            labels: indiastate_list,
            datasets: [{
                    label: 'No. of Active cases',
                    data: india_activelist,
                    backgroundColor: colours

                }

            ]
        },

        options: {

            legend: {
                display: false,
                position: 'bottom',
                labels: {
                    fontColor: 'rgb(0,0,51)'
                },

            },
            title: {
                display: true,
                text: 'India State-wise Active cases'
            },
            responsive: true,

        }
    });

}

function chartChange(flag) {
    //		var zero = Math.random() < 0.2 ? true : false;
    var datasetA;

    if (flag == 'active') {
        //  block of code to be executed if condition1 is true
        datasetA = india_activelist

    } else if (flag == 'recovered') {
        //  block of code to be executed if the condition1 is false and condition2 is true
        datasetA = india_recoveredlist

    } else if (flag == 'confirm') {
        datasetA = india_confirmedlist

    } else {
        datasetA = india_deceasedlist

    }
    var case_type = flag.charAt(0).toUpperCase() + flag.slice(1)
    myindiaChart.config.data.datasets[0].data = datasetA;
    myindiaChart.config.data.datasets[0].label = case_type + " cases"
    myindiaChart.config.options.title.text = "India State-wise " + case_type
    myindiaChart.update();
};