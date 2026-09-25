// Exemplos de variáveis
var nome = "Max Muller"; // string
let idade = 35;          //number
const aprovado = true;   //boolean
let pessoas = {nome: "Lucas", idade: 18}; //objeto
let notas = [8, 9, 7, 10]; //array ou lista

console.log(nome, typeof nome);
console.log(idade, typeof idade);
console.log(aprovado, typeof aprovado);
console.log(pessoas, typeof pessoas);
console.log(notas, typeof notas);

// Operadores aritméticos
let a = 10;
let b = 3;

console.log("Soma:", a + b);
console.log("Subtração:", a - b);
console.log("Multiplicação:", a * b);
console.log("Divisão:", a / b);
console.log("Módulo:", a % b);
console.log("Exponenciação:", a ** b);

// Operadores lógicos
let x = true;
let y = false;

console.log("AND (&&):", x && y);
console.log("OR (||):", x || y);
console.log("NOT (!):", !x);

// Precendência
console.log("Sem parênteses:", 2 + 3 * 4);
console.log("Com parênteses:", (2 + 3) * 4);

function calcularIMC() {
    let peso = document.getElementById("peso").value;
    let altura = document.getElementById("altura").value;

    if (peso <= 0 || altura <= 0 || isNaN(peso) || isNaN(altura)) {
        document.getElementById("resultado").innerText="Valores Inválidos!";
    }
    let imc = peso / (altura * altura);
    let mensagem = "";

    if (imc < 18.5) {
        mensagem = "Abaixo do peso";
    } else if (imc < 24.9) {
        mensagem = "Peso normal";
    } else if (imc < 29.9) {
        mensagem = "Sobrepeso";
    } else {
        mensagem = "Obesidade";
    }
    document.getElementById("resultado").innerText =
    "Seu IMC é" + imc.toFixed(2) + mensagem;
}