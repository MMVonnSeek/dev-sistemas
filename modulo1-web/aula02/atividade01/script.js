// 3. Criando variáveis
const nomeJogador = "AlanGamer";
let idade = 17;
let online = true;

// Objeto com o jogo favorito
let jogoFavorito = {
    nome: "Minecraft",
    anoLancamento: 2011
};

// Array com últimas 3 pontuações
let pontuacoes = [1500, 2000, 1800];

// 4. Mostrando os valores e seus tipos no console
console.log("Nome:", nomeJogador, "Tipo:", typeof nomeJogador);
console.log("Idade:", idade, "Tipo:", typeof idade);
console.log("Online:",online, "Tipo:", typeof online);
console.log("Jogo Favorito:", jogoFavorito, "Tipo:", typeof jogoFavorito);
console.log("Pontuações:", pontuacoes, "Tipo:", typeof pontuacoes);

// 5. Mudando valores da idade e do status 
idade = 18;
online = false;
console.log("Idade:", idade, "Tipo:", typeof idade);
console.log("Online:",online, "Tipo:", typeof online);

//nomeJogador = "Outro Nome";
//console.log("Nome:", nomeJogador, "Tipo:", typeof nomeJogador);
//Não alterar constantes

// Desafio Extra: calcular a média das 3 pontuações
let soma = pontuacoes[0] + pontuacoes[1] + pontuacoes[2];
let media = soma / pontuacoes.length;
console.log("A média de pontos do jogador " + nomeJogador + " foi: " + media.toFixed(2));