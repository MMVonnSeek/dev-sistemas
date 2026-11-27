//Catálogo de jogos
const tabela = document.getElementById("tabela-jogos");
const mensagem = document.getElementById("mensagem");

// Formato de moeda brasileira para o preço
const moeda = {style: "currency", currency:"BRL"};

//Mostra um aviso na página - tipo: "info", "sucesso" ou "erro"
function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = "mensagem" + tipo;
}

// Busca uma rota da API e devolver o JSON já convertido
// em objeto javascript
async function buscar(rota) {
    const resposta = await fetch(`${API_URL}${rota}`);
    if(!resposta.ok) {
        // 404, 500... Vira um erro que será tratado por quem chamou
        throw new Error(`Erro ${resposta.status} em ${rota}`);
    }
    return await resposta.jason();
}
// Criar uma célula <td> com o texto informado
function criarCelula(texto, classe) {
    const td = document.createElement("td");
    td.textContent = texto;
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

        // Dicionário id -> nome (ex: {1: "PlayStation 5"})
        const nomes = {};
        plataformas.forEach(function (plataforma){
            nomes[plataforma.id] = plataforma.name;
        });
        if (jogos.lenght === 0){
            mostrarMensagem("Nenhum jogo cadastrado ainda", "info");
            return;
        }
        jogos.for.Each(function (jogo) {
            const linha = document.createElement("tr");

            linha.appendChild(criarCelula(jogo.id));
            linha.appendChild(criarCelula(jogo.titulo));
            linha.appendChild(criarCelula(jogo.genero || "-"));

            const preco = jogo.preco.toLocaleString("pt-BR", moeda);
            linha.appendChild(criarCelula(preco, "direita"));

            linha.appendChild(criarCelula(nomes[jogo.plataforma_id] || "-"));
            linha.appendChild(criarCelula("", "acoes"));
            
            tabela.appendChild(linha);
        });
        mostrarMensagem("", "info");
    } catch (erro) {
        mostrarMensagem(
            "Não foi possível carregar os jogos. API está rodando?",
            "erro"
        );
        console.erro(erro);
    }
}
carregarJogos();