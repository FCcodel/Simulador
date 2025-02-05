function calculateLaplace() {
    const select = document.getElementById('equation-select');
    const selectedEquation = select.value;

    fetch(`/calculate?equation=${selectedEquation}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `$$${data.result}$$`;
            MathJax.typesetPromise();
        });
}