async function load() {
    const resp = await fetch("/gates");
    const dados = await resp.json();

    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "";

    dados.forEach(g => {
        const row = `
            <tr>
                <td>${g.navio}</td>
                <td>${g.viagem}</td>
                <td>${g.data_gate}</td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}
setInterval(load, 30000);

load();