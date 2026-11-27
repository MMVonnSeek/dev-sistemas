const lista = document.getElementById("lista-plataformas");
const total = document.getElementById("total-plataformas");
const mensagem = document.getElementById("mensagem");
const form = document.getElementById("form-plataforma");
const campoNome = document.getElementById("nome");

// Mostra um aviso na página. tipo: "info", "sucesso" ou "erro"
function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = "mensagem " + tipo;
}

// GET — busca as plataformas e mostra na lista
async function carregarPlataformas() {
    lista.innerHTML = "";

    try {
        const resposta = await fetch(API_URL + "/plataformas/");
        const plataformas = await resposta.json();

        for (const plataforma of plataformas) {
            const item = document.createElement("li");
            item.textContent = `#${plataforma.id} — ${plataforma.nome}`;
            lista.appendChild(item);
        }

        total.textContent = plataformas.length;
    } catch (erro) {
        mostrarMensagem("Não consegui falar com a API. Ela está ligada?", "erro");
    }
}

// POST — envia a nova plataforma para a API
form.addEventListener("submit", async function (evento) {
    evento.preventDefault();   // impede a página de recarregar

    const nome = campoNome.value.trim();
    if (nome === "") {
        mostrarMensagem("Digite o nome da plataforma.", "erro");
        return;
    }

    try {
        const resposta = await fetch(API_URL + "/plataformas/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nome: nome }),
        });

        if (resposta.ok) {
            mostrarMensagem("Plataforma cadastrada!", "sucesso");
            campoNome.value = "";
            carregarPlataformas();
        } else {
            // 409 = nome repetido. A API explica o motivo em "detail"
            const erro = await resposta.json();
            mostrarMensagem(erro.detail, "erro");
        }
    } catch (erro) {
        mostrarMensagem("Não consegui falar com a API. Ela está ligada?", "erro");
    }
});

carregarPlataformas();
