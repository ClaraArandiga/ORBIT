function simular() {
    const params = {
        volume: parseFloat(document.getElementById('volume').value),
        pressao: parseFloat(document.getElementById('pressao').value),
        massa: parseFloat(document.getElementById('massa').value),
        angulo: parseFloat(document.getElementById('angulo').value)
    };

    fetch('/simular', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('altura').innerText = data.altura_maxima.toFixed(2);
        document.getElementById('velocidade').innerText = data.velocidade_maxima.toFixed(2);
        document.getElementById('tempo').innerText = data.tempo_total.toFixed(2);
        plotarGrafico(data.trajetoria);
    });
}

function plotarGrafico(trajetoria) {
    new Chart(document.getElementById('graficoTrajetoria'), {
        type: 'line',
        data: {
            labels: trajetoria.map((_, i) => i),
            datasets: [{
                label: 'Altura (m)',
                data: trajetoria,
                borderColor: 'lime',
                fill: false
            }]
        }
    });
}
