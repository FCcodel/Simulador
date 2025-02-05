document.addEventListener("DOMContentLoaded", function() {
    updateEquation();
});

function updateEquation() {
    const select = document.getElementById('equation-select');
    const selectedEquation = select.value;
    let equationText = '';

    if (selectedEquation === 'eq1') {
        equationText = '$$f(t) = u(t) - u(t-2)$$';
    } else if (selectedEquation === 'eq2') {
        equationText = '$$f(t) = e^{-a t} \cdot u(t)$$';
    } else if (selectedEquation === 'eq3') {
        equationText = '$$f(t) = 3e^{-2t} \cdot u(t) + e^{-t} \cos(3t) \cdot u(t)$$';
    }

    document.getElementById('equation').innerHTML = `Ecuación: ${equationText}`;
    MathJax.typesetPromise();
}

function calculateLaplace() {
    const select = document.getElementById('equation-select');
    const selectedEquation = select.value;

    fetch(`/calculate?equation=${selectedEquation}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `Resultado: $$${data.result}$$`;
            MathJax.typesetPromise();
        });
}