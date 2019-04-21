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
{label: "thank", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 24] },
{label: "retweet4good", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 123] },
{label: "paradise", data: [82, 105, 0, 58, 49, 49, 47, 36, 33, 36, 33, 23, 17, 0] },
{label: "people", data: [0, 89, 96, 51, 49, 38, 34, 0, 32, 34, 0, 14, 0, 0] },
{label: "home", data: [0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "started", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0] },
{label: "san", data: [0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0] },
{label: "prayer", data: [37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "rain", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39] },
{label: "death", data: [0, 0, 0, 0, 58, 32, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "airquality", data: [0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0] },
{label: "god", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0] },
{label: "help", data: [0, 83, 92, 114, 155, 61, 49, 35, 50, 43, 29, 16, 14, 45] },
{label: "forest", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0] },
{label: "history", data: [0, 0, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "evacuation", data: [39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "paradisefire", data: [0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "relief", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22] },
{label: "firefighter", data: [0, 0, 0, 71, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0] },
{label: "animal", data: [0, 0, 0, 0, 0, 30, 50, 0, 0, 0, 0, 0, 0, 0] },
{label: "state", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0] },
{label: "hillfire", data: [0, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "air", data: [0, 0, 0, 0, 0, 0, 0, 46, 56, 0, 22, 0, 0, 0] },
{label: "smoke", data: [60, 129, 112, 43, 0, 0, 38, 70, 48, 28, 0, 18, 25, 0] },
{label: "fire", data: [79, 148, 247, 105, 104, 72, 65, 62, 44, 40, 59, 41, 18, 23] },
{label: "democrat", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0] },
{label: "story", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0] },
{label: "affected", data: [0, 0, 69, 0, 113, 0, 57, 0, 0, 0, 0, 0, 0, 0] },
{label: "please", data: [35, 62, 80, 76, 0, 44, 0, 0, 38, 28, 0, 0, 0, 0] },
{label: "quality", data: [0, 0, 0, 0, 0, 0, 0, 31, 33, 0, 0, 0, 0, 0] },
{label: "safe", data: [0, 72, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
{label: "missing", data: [0, 0, 0, 44, 0, 0, 29, 28, 49, 0, 0, 0, 0, 0] },
{label: "victim", data: [0, 0, 0, 44, 0, 0, 0, 35, 0, 30, 0, 20, 17, 27] },
{label: "president", data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 0, 0, 0, 0] },
{label: "deadliest", data: [0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 16, 0, 0] },

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
