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
                .curve(d3.curveLinear);  // Asegúrate de usar una línea suave

const lineB = d3.line()
                .x((d, i) => xScale(x[i]))
                .y(d => yScale(d))
                .curve(d3.curveLinear);  // Asegúrate de usar una línea suave

const pathE = svg.append("path")
                 .datum(yE)
                 .attr("class", "lineE")
                 .attr("d", lineE)
                 .style("stroke", "blue")
                 .style("fill", "none")  // Asegúrate de que no haya relleno
                 .style("stroke-width", 2);  // Asegúrate de que el ancho de la línea sea adecuado

const pathB = svg.append("path")
                 .datum(zB)
                 .attr("class", "lineB")
                 .attr("d", lineB)
                 .style("stroke", "red")
                 .style("fill", "none")  // Asegúrate de que no haya relleno
                 .style("stroke-width", 2);  // Asegúrate de que el ancho de la línea sea adecuado

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
    }, 100);
}

function stopAnimation() {
    clearInterval(interval);
}

d3.select("#play-pause").on("click", function() {
    animRunning = !animRunning;
    if (animRunning) {
        animate();
        d3.select(this).text("Pause");
    } else {
        stopAnimation();
        d3.select(this).text("Play");
    }
});

updateWave();
