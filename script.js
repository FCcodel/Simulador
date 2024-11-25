const svg = d3.select("#wave-chart"),
      width = +svg.attr("width"),
      height = +svg.attr("height");

let amplitudE = 1,
    frecuenciaE = 1,
    amplitudB = 1,
    frecuenciaB = 1,
    showPlanes = true;

const x = d3.range(0, 4 * Math.PI, (4 * Math.PI) / 1000);
const yE = x.map(d => amplitudE * Math.sin(frecuenciaE * d));
const zB = x.map(d => amplitudB * Math.sin(frecuenciaB * d));

const yScale = d3.scaleLinear().domain([-2, 2]).range([height, 0]);
const xScale = d3.scaleLinear().domain([0, 4 * Math.PI]).range([0, width]);

const lineE = d3.line()
                .x((d, i) => xScale(x[i]))
                .y(d => yScale(d));

const lineB = d3.line()
                .x((d, i) => xScale(x[i]))
                .y(d => yScale(d));

svg.append("path")
   .datum(yE)
   .attr("class", "lineE")
   .attr("d", lineE)
   .style("stroke", "blue");

svg.append("path")
   .datum(zB)
   .attr("class", "lineB")
   .attr("d", lineB)
   .style("stroke", "red");

function updateWave() {
    const yE = x.map(d => amplitudE * Math.sin(frecuenciaE * d));
    const zB = x.map(d => amplitudB * Math.sin(frecuenciaB * d));
    
    svg.select(".lineE")
       .datum(yE)
       .attr("d", lineE);
       
    svg.select(".lineB")
       .datum(zB)
       .attr("d", lineB);
}

document.getElementById("amplitudE").addEventListener("input", function() {
    amplitudE = +this.value;
    updateWave();
});

document.getElementById("frecuenciaE").addEventListener("input", function() {
    frecuenciaE = +this.value;
    updateWave();
});

document.getElementById("amplitudB").addEventListener("input", function() {
    amplitudB = +this.value;
    updateWave();
});

document.getElementById("frecuenciaB").addEventListener("input", function() {
    frecuenciaB = +this.value;
    updateWave();
});

document.getElementById("togglePlanes").addEventListener("click", function() {
    showPlanes = !showPlanes;
    if (showPlanes) {
        svg.select(".lineE").style("stroke-dasharray", "none");
        svg.select(".lineB").style("stroke-dasharray", "none");
    } else {
        svg.select(".lineE").style("stroke-dasharray", "4,4");
        svg.select(".lineB").style("stroke-dasharray", "4,4");
    }
});

