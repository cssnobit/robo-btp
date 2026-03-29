let timeAtt = 900;
let count = timeAtt;
let timer = null;

async function load() {
    const resp = await fetch("/gates");
    const dados = await resp.json();

    const tbody = document.querySelector("#tabela-navios tbody");
    tbody.innerHTML = "";

    dados.forEach(g => {
        const row = `
            <tr>
                <td>${g.navio}</td>
                <td>${g.agencia}</td>
                <td>${g.viagem}</td>
                <td>${g.data_gate}</td>
                <td>${g.deadline}</td>
            </tr>
        `;
        tbody.innerHTML += row;
    });

    document.getElementById('total-navios').textContent = `Total: ${dados.length} navios`;

    document.getElementById('prox-att').textContent = formatTime(count);
    updateTime();
    resetCount();
}

function updateTime() {
    const now = new Date();
    document.getElementById("ultima-att").textContent = `Última: ${now.toLocaleTimeString()}`;
}

function startCount() {
    if (timer) clearInterval(timer);
    
    timer = setInterval(() => {
        count--;
        document.getElementById('prox-att').textContent = formatTime(count);

        if (count <= 0) {
            load()
        }
    }, 1000);
}

function formatTime(secs) {
    const min = Math.floor(secs / 60);
    const sec = secs % 60;

    return `${String(min).padStart(2, "0")}:${String(sec).padStart(2, "0")}`;
}

function resetCount() {
    count = timeAtt;
}

function forceUpdate() {
    load();
}

async function run() {
    await load();
    document.getElementById('prox-att').textContent = formatTime(count);
    startCount();
}

run();