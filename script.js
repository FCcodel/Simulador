const svg = d3.select("#wave-chart"),
      width = +svg.attr("width"),
      height = +svg.attr("height");

let amplitudE = 1,
    frecuenciaE = 1,
    amplitudB = 1,
    frecuenciaB = 1,
    showE = true,
    showB = true,
    animRunning = false,
    interval;

// Generación de datos
const x = d3.range(0, 4 * Math.PI, (4 * Math.PI) / 1000);
let yE = x.map(d => amplitudE * Math.sin(frecuenciaE * d));
let zB = x.map(d => amplitudB * Math.sin(frecuenciaB * d));

const yScale = d3.scaleLinear().domain([-2, 2]).range([height, 0]);
const xScale = d3.scaleLinear().domain([0, 4 * Math.PI]).range([0, width]);

const lineE = d3.line()
                .x((d, i) => xScale(x[i]))
                .y(d => yScale(d))
                .curve(d3.curveLinear);

const lineB = d3.line()
                .x((d, i) => xScale(x[i]))
                .y(d => yScale(d))
                .curve(d3.curveLinear);

// Definir gradiente de color para las ondas
const gradientE = svg.append("defs")
    .append("linearGradient")
    .attr("id", "gradientE")
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "0%");
gradientE.append("stop")
    .attr("offset", "0%")
    .attr("stop-color", "blue");
gradientE.append("stop")
    .attr("offset", "100%")
    .attr("stop-color", "lightblue");

const gradientB = svg.append("defs")
    .append("linearGradient")
    .attr("id", "gradientB")
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "0%");
gradientB.append("stop")
    .attr("offset", "0%")
    .attr("stop-color", "red");
gradientB.append("stop")
    .attr("offset", "100%")
    .attr("stop-color", "pink");

const pathE = svg.append("path")
                 .datum(yE)
                 .attr("class", "lineE")
                 .attr("d", lineE)
                 .style("stroke", "url(#gradientE)")
                 .style("fill", "none")
                 .style("stroke-width", 2);

const pathB = svg.append("path")
                 .datum(zB)
                 .attr("class", "lineB")
                 .attr("d", lineB)
                 .style("stroke", "url(#gradientB)")
                 .style("fill", "none")
                 .style("stroke-width", 2);

// Añadir eje de propagación
svg.append("line")
    .attr("x1", 0)
    .attr("y1", height / 2)
    .attr("x2", width)
    .attr("y2", height / 2)
    .attr("stroke", "black")
    .attr("stroke-dasharray", "5,5")
    .attr("stroke-width", 1)
    .attr("marker-end", "url(#arrow)");

svg.append("defs").append("marker")
    .attr("id", "arrow")
    .attr("viewBox", "0 0 10 10")
    .attr("refX", 10)
    .attr("refY", 5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto-start-reverse")
  .append("path")
    .attr("d", "M0,0 L10,5 L0,10 Z")
    .attr("fill", "black");

function updateWave() {
    yE = x.map(d => amplitudE * Math.sin(frecuenciaE * d));
    zB = x.map(d => amplitudB * Math.sin(frecuenciaB * d));
    
    pathE.datum(yE).attr("d", lineE);
    pathB.datum(zB).attr("d", lineB);

    d3.select("#a-value").text(amplitudE);
    d3.select("#w-value").text(frecuenciaE);
    d3.select("#p-value").text(amplitudB);
    d3.select("#m-value").text(frecuenciaB);
}

d3.select("#a-slider").on("input", function() {
    amplitudE = +this.value;
    updateWave();
});

d3.select("#w-slider").on("input", function() {
    frecuenciaE = +this.value;
    updateWave();
});

d3.select("#p-slider").on("input", function() {
    amplitudB = +this.value;
    updateWave();
});

d3.select("#m-slider").on("input", function() {
    frecuenciaB = +this.value;
    updateWave();
});

d3.select("#toggleE").on("change", function() {
    showE = this.checked;
    pathE.style("display", showE ? null : "none");
});

d3.select("#toggleB").on("change", function() {
    showB = this.checked;
    pathB.style("display", showB ? null : "none");
});

function animate() {
    let i = 0;
    interval = setInterval(() => {
        yE = x.map(d => amplitudE * Math.sin(frecuenciaE * d + i / 10.0));
        zB = x.map(d => amplitudB * Math.sin(frecuenciaB * d + i / 10.0));
        
        pathE.datum(yE).attr("d", lineE);
        pathB.datum(zB).attr("d", lineB);
        i++;
    },
    
    //[_{{{CITATION{{{_1{](https://github.com/Genesissdh/Estructuras-Control/tree/0c75aa66757613b7a4668d3cc243ca27a8780030/Ejercicio1.php)[_{{{CITATION{{{_2{](https://github.com/medialab/personal-air-timeline/tree/b20dab5f50c9d8c6830912c832ae93aabe38c6d5/app%2Fapp.js)[_{{{CITATION{{{_3{](https://github.com/callumwebb/cwebby/tree/fd5c2416446bbb94bd22834a5ed4d8b2f970432e/static%2Fjs%2Froc%2Fconfusion-matrix.js)[_{{{CITATION{{{_4{](https://github.com/jsIsrael/d3-epidemiology-timeline/tree/f4bd356ee06af34a6389fbabe6852e96b231420f/src%2FGraph%2FsecondIterationD3.ts)[_{{{CITATION{{{_5{](https://github.com/tinpotnick/packetpeek/tree/6039dc33889552bf2051b7ccb22ebf6d49a516c4/pcap.js)[_{{{CITATION{{{_6{](https://github.com/ntropy-esa/biochar-systems-dev/tree/ecf241fe53d1a7c91e5b3e0bb26f4e6388a8fdf1/static%2Fbw2widgets%2Fwidget_plot_types.js)