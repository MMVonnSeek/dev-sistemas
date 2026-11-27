const container = document.getElementById("cardsContainer");
const input = document.getElementById("tituloCard");
const btnCriar = document.getElementById("criarCard");

btnCriar.addEventListener("click", () => {
    const card = document.createElement("div");
    card.className = "card";


const h3 = document.createElement("h3");
h3.textContent = input.value;

const btnRemover = document.createElement("button");
btnRemover.textContent = "Remover";
btnRemover.addEventListener("click", () => {
    container.removeChild(card);
});

card.appendChild(h3);
card.appendChild(btnRemover);
container.appendChild(card);

input.value = "";
});