let timeAtt = 60;
let count = timeAtt;
let timer = null;
let loading = false;

async function load() {
    if (loading) return;

    const tbody = document.querySelector("#tabela-navios tbody");
    tbody.classList.add("loading-row");

    loading = true;
    
    try {
        const resp = await fetch("/gates");
        const dados = await resp.json();
        tbody.innerHTML = "";
        updateTime(dados);

        dados.datas.forEach(g => {
            let classeNavio = "";

            if (g.janelaDry === "SIM") {
                classeNavio = "janela-disponivel"
            } else if(g.gateConfirmado) {
                classeNavio = "gate-confirmado"
            }

            const row = `
                <tr class="${classeNavio}">
                    <td style="font-weight: 700;">${g.navio}</td>
                    <td>${g.agencia}</td>
                    <td>${g.viagem}</td>
                    <td>${g.data_gate}</td>
                    <td>${g.deadline}</td>
                    <td style="font-weight: 600;">${g.janelaDry}</td>
                </tr>
            `;
            tbody.innerHTML += row;
        });

        
        document.getElementById('total-navios').textContent = `Total: ${dados.datas.length} navio(s)`;
        
        updateTime(dados);
        resetCount();
        tbody.classList.remove("loading-row")
    } catch (e) {
        console.error("Erro: ", e);
        tbody.classList.remove("loading-row");
    } finally {
        loading = false;
    }
    
}

function updateTime(datetime) {
    let last_time = datetime.last_update.split(" ")[1];
    let next_time = datetime.next_update.split(" ")[1];

    document.getElementById("ultima-att").textContent = `Última: ${last_time}`;
    document.getElementById("prox-att").textContent = next_time;
}

function startCount() {
    if (timer) clearInterval(timer);
    
    timer = setInterval(() => {
        if (count > 0) count--;

        if (count <= 0 && !loading) {
            load()
        }
    }, 1000);
}

function resetCount() {
    count = timeAtt;
}

function forceUpdate() {
    load();
}

async function run() {
    await load();
    startCount();
}

run();