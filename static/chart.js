const chart = document.getElementById("lineChart");
console.log(chart);

let data = [5, 10, 5, 14, 20, 15, 22, 32, 12, 1];

let lineChart = new Chart(chart, {
    type: 'line',
    data: {
        //labels: ["January", "February", "March", "Apri", "May", "June"],
        labels: [2, 3, 4, 5, 6, 7, 8],
        datasets: [{ 
            label: "EDA 2 vai ser é doido parceiro",
            data: data,
            borderWidth: 6,
            borderColor: 'rgba(75, 75, 192, 0.4)',
            backgroundColor: 'rgba(75, 75, 192, 0.4)',
            lineTension: 0,
            fill: false,
            pointStyle: "star",
            pointBorderColor: 'rgba(23, 122, 102, 0.7)',        

            }
        ]
    },
    options: {
        showLines: true,
        stacked: false,
        elementspointradius: 10,
        scales: {

            xAxes: [{
                ticks:{
                    beginAtZero: true,
                    fontColor: 'black',
                    min: 0,
                    max: 100,
                    gridLines: {
                        color: "rgba(0, 0, 0, 0)",
                    },
                }
            }],

            yAxes: [{
                ticks:{
                    beginAtZero: true,
                    min: 0,
                    max: 100,
                    fontColor: 'black',
                    gridLines: {
                        color: "rgba(0, 0, 0, 0)",
                    },
                }
            }]
        }
    } 
});

const barCtx = document.getElementById("barChart");

Chart.defaults.scale.ticks.beginAtZero = true;

let barChart = new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: [1, 2, 3, 4, 6, 7, 8],
        datasets: [{
            label: 'Vou dominar o mundo parceiro',
            data: [10, 20, 30, 45, 25],
            backgroundColor: '#00FF00',
            borderWidth: 2,
            borderColor: 'rgba(75, 75, 192, 0.4)',
        }]
    }
});