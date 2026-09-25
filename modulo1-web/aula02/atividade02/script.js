// 3.
let precoProduto = 20;
let quantidade = 3;

// 4.
let total = precoProduto * quantidade;
let dobro = total * 2;
let resto = total % 2;

// 5.
let cupomValido = true;
let freteGratis = false;

// 6.
let algumBeneficio = cupomValido || freteGratis;
let todosBeneficios = cupomValido && freteGratis;

// Mostrando na Tela
document.getElementById("preco").innerText = "R$ " + precoProduto;
document.getElementById("quantidade").innerText = quantidade;
document.getElementById("total").innerText = "R$ " + total;
document.getElementById("dobro").innerText = "R$ " + dobro;
document.getElementById("resto").innerText = resto;
document.getElementById("cupom").innerText = cupomValido ? "Sim" : "Não";
document.getElementById("frete").innerText = freteGratis ? "Sim" : "Não";
document.getElementById("algum").innerText = algumBeneficio ? "Sim" : "Não";
document.getElementById("todos").innerText = todosBeneficios ? "Sim" : "Não";