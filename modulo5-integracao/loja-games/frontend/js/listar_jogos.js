// Catálogo de jogos

const tabela = document.getElementById("tabela-jogos");
const mensagem = document.getElementById("mensagem");

// Formato de moeda brasileira para o preço
const moeda = { style: "currency", currency: "BRL" };

// Mostra um aviso na página. tipo: "info", "sucesso" ou "erro"
function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = "mensagem " + tipo;
}

// Busca uma rota da API e devolve o JSON já convertido em objeto JavaScript
async function buscar(rota) {
    const resposta = await fetch(`${API_URL}${rota}`);

    if (!resposta.ok) {
        // 404, 500... : vira erro e cai no catch de quem chamou
        throw new Error(`Erro ${resposta.status} em ${rota}`);
    }

    return await resposta.json();
}

// Cria uma célula <td> com o texto informado
function criarCelula(texto, classe) {
    const td = document.createElement("td");
    td.textContent = texto;          // textContent: seguro, nunca interpreta HTML
    if (classe) {
        td.className = classe;
    }
    return td;
}

async function carregarJogos() {
    mostrarMensagem("Carregando jogos...", "info");
    tabela.innerHTML = "";

    try {
        const plataformas = await buscar("/plataformas/");
        const jogos = await buscar("/jogos/");

        // Dicionário  id -> nome   (ex.: { 1: "PlayStation 5" })
        const nomes = {};
        plataformas.forEach(function (plataforma) {
            nomes[plataforma.id] = plataforma.nome;
        });

        if (jogos.length === 0) {
            mostrarMensagem("Nenhum jogo cadastrado ainda.", "info");
            return;
        }

        jogos.forEach(function (jogo) {
            const linha = document.createElement("tr");

            linha.appendChild(criarCelula(jogo.id));
            linha.appendChild(criarCelula(jogo.titulo));
            linha.appendChild(criarCelula(jogo.genero || "—"));

            const preco = jogo.preco.toLocaleString("pt-BR", moeda);
            linha.appendChild(criarCelula(preco, "direita"));

            linha.appendChild(criarCelula(nomes[jogo.plataforma_id] || "—"));
            linha.appendChild(criarCelula("", "acoes"));   // botões 

            tabela.appendChild(linha);
        });

        mostrarMensagem("", "info");   // tudo certo: esconde a mensagem
    } catch (erro) {
        mostrarMensagem(
            "Não foi possível carregar os jogos. A API está rodando?",
            "erro"
        );
        console.error(erro);
    }
}

carregarJogos();
