const svg = d3.select("#wave-chart"),
      margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = +svg.attr("width") - margin.left - margin.right,
      height = +svg.attr("height") - margin.top - margin.bottom;

const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

// Crear patrones rayados para el relleno
const defs = svg.append("defs");

defs.append("pattern")
    .attr("id", "stripeE")
    .attr("width", 4)
    .attr("height", 4)
    .attr("patternUnits", "userSpaceOnUse")
  .append("path")
    .attr("d", "M0,0 L4,4")
    .attr("stroke", "blue")
    .attr("stroke-width", 1);

defs.append("pattern")
    .attr("id", "stripeB")
    .attr("width", 4)
    .attr("height", 4)
    .attr("patternUnits", "userSpaceOnUse")
  .append("path")
    .attr("d", "M0,0 L4,4")
    .attr("stroke", "red")
    .attr("stroke-width", 1);

let amplitudE = 1, frecuenciaE = 1;
let amplitudB = 1, frecuenciaB = 1;
let showE = true, showB = true;
let animRunning = false, interval;

const x = d3.range(0, 4 * Math.PI, (4 * Math.PI) / 1000);
let yE = generateWave(amplitudE, frecuenciaE);
let zB = generateWave(amplitudB, frecuenciaB);

const yScale = d3.scaleLinear().domain([-2, 2]).range([height, 0]);
const xScale = d3.scaleLinear().domain([0, 4 * Math.PI]).range([0, width]);

const lineE = createLine(xScale, yScale);
const lineB = createLine(xScale, yScale);

const areaE = createArea(xScale, yScale);
const areaB = createArea(xScale, yScale);

const pathE = createPath(g, yE, lineE, "lineE", "blue");
const pathB = createPath(g, zB, lineB, "lineB", "red");

const areaPathE = createAreaPath(g, yE, areaE, "areaE", "url(#stripeE)");
const areaPathB = createAreaPath(g, zB, areaB, "areaB", "url(#stripeB)");

const xAxis = d3.axisBottom(xScale).ticks(10);
const yAxis = d3.axisLeft(yScale).ticks(10);

g.append("g")
 .attr("class", "x axis")
 .attr("transform", `translate(0,${height})`)
 .call(xAxis);

g.append("g")
 .attr("class", "y axis")
 .call(yAxis);

function generateWave(amplitud, frecuencia, phase = 0) {
  return x.map(d => amplitud * Math.sin(frecuencia * d + phase / 10.0));
}

function createLine(xScale, yScale) {
  return d3.line()
           .x((d, i) => xScale(x[i]))
           .y(d => yScale(d))
           .curve(d3.curveLinear);
}

function createArea(xScale, yScale) {
  return d3.area()
           .x((d, i) => xScale(x[i]))
           .y0(height)
           .y1(d => yScale(d))
           .curve(d3.curveLinear);
}

function createPath(svg, data, line, className, color) {
  return svg.append("path")
            .datum(data)
            .attr("class", className)
            .attr("d", line)
            .style("stroke", color)
            .style("fill", "none")
            .style("stroke-width", 2);
}

function createAreaPath(svg, data, area, className, pattern) {
  return svg.append("path")
            .datum(data)
            .attr("class", className)
            .attr("d", area)
            .style("fill", pattern);
}

function updateWave() {
  yE = generateWave(amplitudE, frecuenciaE);
  zB = generateWave(amplitudB, frecuenciaB);
  
  pathE.datum(yE).attr("d", lineE);
  pathB.datum(zB).attr("d", lineB);
  areaPathE.datum(yE).attr("d", areaE);
  areaPathB.datum(zB).attr("d", areaB);

  d3.select("#a-value").text(amplitudE);
  d3.select("#w-value").text(frecuenciaE);
  d3.select("#p-value").text(amplitudB);
  d3.select("#m-value").text(frecuenciaB);
}

d3.selectAll("#a-slider, #w-slider, #p-slider, #m-slider").on("input", function() {
  const value = +this.value;
  if (this.id === "a-slider") amplitudE = value;
  if (this.id === "w-slider") frecuenciaE = value;
  if (this.id === "p-slider") amplitudB = value;
  if (this.id === "m-slider") frecuenciaB = value;
  updateWave();
});

d3.selectAll("#toggleE, #toggleB").on("change", function() {
  if (this.id === "toggleE") showE = this.checked;
  if (this.id === "toggleB") showB = this.checked;
  pathE.style("display", showE ? null : "none");
  pathB.style("display", showB ? null : "none");
  areaPathE.style("display", showE ? null : "none");
  areaPathB.style("display", showB ? null : "none");
});

d3.select("#play-pause").on("click", function() {
  animRunning = !animRunning;
  d3.select(this).text(animRunning ? "Pause" : "Play");
  animRunning ? animate() : stopAnimation();
});

function animate() {
  let i = 0;
  interval = setInterval(() => {
    yE = generateWave(amplitudE, frecuenciaE, i);
    zB = generateWave(amplitudB, frecuenciaB, i);
    pathE.datum(yE).attr("d", lineE);
    pathB.datum(zB).attr("d", lineB);
    areaPathE.datum(yE).attr("d", areaE);
    areaPathB.datum(zB).attr("d", areaB);
    i++;
  }, 100);
}

function stopAnimation() {
  clearInterval(interval);
}

updateWave();

