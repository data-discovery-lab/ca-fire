function WordStreamViewer() {

    // this.wordCloud = new WordCloud('adminBoard');

}

WordStreamViewer.prototype = {
    constructor: WordStreamViewer,

    create_graph: function (canvasElementId) {

       // completely arbitrary data
      var sampleData = {
         labels: ['2018_11_08', '2018_11_09', '2018_11_10', '2018_11_11', '2018_11_12', '2018_11_13', '2018_11_14', '2018_11_15', '2018_11_16', '2018_11_17', '2018_11_18', '2018_11_19', '2018_11_20', '2018_11_21'],
        datasets: [
{label: "trump", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0] },
{label: "camp", data: [0, 0, 0, 0, 21, 0, 0, 0, 0, 20, 25, 0, 28, 0] },
{label: "photo", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 0] },
{label: "evacuation", data: [0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0] },
{label: "homes", data: [0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "sunday", data: [0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0] },
{label: "wildfire", data: [0, 0, 0, 29, 0, 0, 0, 21, 0, 0, 20, 0, 0, 0] },
{label: "fire", data: [61, 50, 33, 73, 80, 59, 48, 49, 39, 78, 67, 29, 54, 25] },
{label: "ojai", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0] },
{label: "calif", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0] },
{label: "wildfires", data: [0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0] },
{label: "file", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0] },
{label: "nov", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0] },
{label: "california", data: [0, 22, 0, 87, 38, 0, 21, 38, 26, 25, 45, 0, 28, 24] },
{label: "rain", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24] },
{label: "search", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 0, 0, 0] },
{label: "northern", data: [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0] },
{label: "wednesday", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20] },
{label: "southern", data: [0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "paradise", data: [22, 0, 0, 27, 31, 0, 0, 0, 0, 23, 36, 0, 0, 0] },
{label: "fires", data: [0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "remains", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0] },

        ]
      };

      var context = document.getElementById(canvasElementId).getContext('2d');

    var maxHeightChart = new Chart(context)
        .Streamgraph(sampleData, {
          responsive: true,
            colorAssignmentMethod: 'verticalPosition',
          labelPlacementMethod: 'maxHeight',
            colors: [
                '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94',
                '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf'
            ],
            labelFontColor: 'black',
            labelMinimumSize: 9,
            stroke: false        });

    }




};

function init() {
    var concern = new WordStreamViewer();
    concern.create_graph('concern_flow');
}

window.onload = init;
