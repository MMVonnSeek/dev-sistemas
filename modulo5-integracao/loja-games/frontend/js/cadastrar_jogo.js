// Cadastrar (POST) e editar (PUT) jogos

const form = document.getElementById("form-jogo");
const tituloPagina = document.getElementById("titulo-pagina");
const mensagem = document.getElementById("mensagem");
const botao = document.getElementById("btn-salvar");

const campoTitulo = document.getElementById("titulo");
const campoGenero = document.getElementById("genero");
const campoPreco = document.getElementById("preco");
const campoPlataforma = document.getElementById("plataforma");

// Se o endereço tiver ?id=3 estamos EDITANDO o jogo 3; sem id, estamos cadastrando
const id = new URLSearchParams(window.location.search).get("id");

// Mostra um aviso na página. tipo: "info", "sucesso" ou "erro"
function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = "mensagem " + tipo;
}

// Busca as plataformas na API e cria uma <option> para cada uma
async function carregarPlataformas() {
    const resposta = await fetch(API_URL + "/plataformas/");
    const plataformas = await resposta.json();

    for (const plataforma of plataformas) {
        const opcao = document.createElement("option");
        opcao.value = plataforma.id;
        opcao.textContent = plataforma.nome;
        campoPlataforma.appendChild(opcao);
    }
}

// No modo edição, busca o jogo e preenche o formulário
async function carregarJogo() {
    const resposta = await fetch(API_URL + "/jogos/" + id);

    if (!resposta.ok) {
        mostrarMensagem("Jogo não encontrado.", "erro");
        botao.disabled = true;
        return;
    }

    const jogo = await resposta.json();
    campoTitulo.value = jogo.titulo;
    campoGenero.value = jogo.genero || "";
    campoPreco.value = jogo.preco;
    campoPlataforma.value = jogo.plataforma_id;
}

// Confere os campos. Devolve true se está tudo certo
function validar() {
    let valido = true;

    document.getElementById("erro-titulo").textContent = "";
    document.getElementById("erro-preco").textContent = "";
    document.getElementById("erro-plataforma").textContent = "";

    if (campoTitulo.value.trim() === "") {
        document.getElementById("erro-titulo").textContent = "Digite o título.";
        valido = false;
    }
    if (campoPreco.value === "" || Number(campoPreco.value) <= 0) {
        document.getElementById("erro-preco").textContent = "O preço deve ser maior que zero.";
        valido = false;
    }
    if (campoPlataforma.value === "") {
        document.getElementById("erro-plataforma").textContent = "Escolha uma plataforma.";
        valido = false;
    }

    return valido;
}

// Pega o que a API respondeu de errado e transforma em texto
function textoDoErro(erro) {
    // 422: "detail" é uma lista de problemas. 404/409: "detail" é um texto.
    if (Array.isArray(erro.detail)) {
        return "Dados inválidos: confira os campos.";
    }
    return erro.detail;
}

// Ao enviar o formulário: valida e manda para a API (POST ou PUT)
form.addEventListener("submit", async function (evento) {
    evento.preventDefault();

    if (!validar()) {
        return;
    }

    const dados = {
        titulo: campoTitulo.value.trim(),
        genero: campoGenero.value.trim() || null,
        preco: Number(campoPreco.value),
        plataforma_id: Number(campoPlataforma.value),
    };

    // Com id é edição (PUT em /jogos/3); sem id é cadastro (POST em /jogos/)
    const url = id ? API_URL + "/jogos/" + id : API_URL + "/jogos/";
    const metodo = id ? "PUT" : "POST";

    botao.disabled = true;

    try {
        const resposta = await fetch(url, {
            method: metodo,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados),
        });

        if (resposta.ok) {
            if (id) {
                mostrarMensagem("Jogo atualizado!", "sucesso");
            } else {
                mostrarMensagem("Jogo cadastrado!", "sucesso");
                form.reset();
            }
        } else {
            const erro = await resposta.json();
            mostrarMensagem(textoDoErro(erro), "erro");
        }
    } catch (erro) {
        mostrarMensagem("Não consegui falar com a API. Ela está ligada?", "erro");
    }

    botao.disabled = false;
});

// Ao abrir a página
async function iniciar() {
    try {
        await carregarPlataformas();

        if (id) {
            tituloPagina.textContent = "Editar Jogo";
            botao.textContent = "Salvar alterações";
            await carregarJogo();
        }
    } catch (erro) {
        mostrarMensagem("Não consegui falar com a API. Ela está ligada?", "erro");
    }
}

iniciar();