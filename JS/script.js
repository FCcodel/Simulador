// Configuración básica de Three.js
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff); // Fondo blanco

const camera = new THREE.PerspectiveCamera(75, 800 / 400, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(800, 400);
document.getElementById('wave-chart').appendChild(renderer.domElement);

// Añadir una fuente de luz
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(10, 10, 10).normalize();
scene.add(light);

// Añadir controles de órbita
const controls = new THREE.OrbitControls(camera, renderer.domElement);

// Crear la geometría y material para las ondas
const lineMaterialE = new THREE.LineBasicMaterial({ color: 0x0000ff }); // Azul para E
const lineMaterialB = new THREE.LineBasicMaterial({ color: 0xff0000 }); // Rojo para B

function generateWave(amplitude, frequency, phase = 0) {
    const points = [];
    for (let i = 0; i <= 100; i++) {
        const x = i * 0.1;
        const y = amplitude * Math.sin(frequency * x + phase);
        points.push(new THREE.Vector3(x, y, 0));
    }
    return points;
}

let lineE = new THREE.Line(new THREE.BufferGeometry().setFromPoints(generateWave(1, 1)), lineMaterialE);
let lineB = new THREE.Line(new THREE.BufferGeometry().setFromPoints(generateWave(1, 1, Math.PI / 2)), lineMaterialB);

scene.add(lineE);
scene.add(lineB);

// Añadir ejes de referencia
const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper);

// Añadir etiquetas a las ondas
const spriteE = createTextSprite('Campo Eléctrico (E)', { color: 'blue' });
spriteE.position.set(5, 1, 0);
scene.add(spriteE);

const spriteB = createTextSprite('Campo Magnético (B)', { color: 'red' });
spriteB.position.set(5, -1, 0);
scene.add(spriteB);

camera.position.z = 10;  // Ajustar la posición de la cámara

// Función para crear etiquetas de texto
function createTextSprite(message, parameters) {
    const { color = 'black', fontface = 'Arial', fontsize = 24 } = parameters;
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    context.font = `${fontsize}px ${fontface}`;
    context.fillStyle = color;
    context.fillText(message, 0, fontsize);

    const textura = new THREE.CanvasTexture(canvas);
    const Material = new THREE.SpriteMaterial({ map: texture });
    const sprite = new THREE.Sprite(Material);
    return sprite;
}

// Animación de las ondas
function animate() {
    requestAnimationFrame(animate);
    controls.update();  // Actualizar controles
    lineE.geometry.setFromPoints(generateWave(amplitudE, frecuenciaE));
    lineB.geometry.setFromPoints(generateWave(amplitudB, frecuenciaB, Math.PI / 2));
    renderer.render(scene, camera);
}
animate();
