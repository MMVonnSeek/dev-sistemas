//Selecionar o container principal
const container = document.getElementById("container");

// 1 appendChild - adiciona no final
document.getElementById("btnAppend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Parágrafo adicionado com appendChild no final";
    container.appendChild(p);
});

// 2 prepend - adiciona no início
document.getElementById("btnPrepend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Parágrafo adicionado com prepend no início";
    container.prepend(p);
});

// 3 insertBefore - isere antes do primeiro
document.getElementById("btnInsertBefore").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Parágrafo inserido antes do primeiro";
    const primeiro = container.firstElementChild;
    container.insertBefore(p, primeiro);
});

// 4 btnReplace - substitui o primeiro parágrafo
document.getElementById("btnReplace").addEventListener("click", () => {
    const novo = document.createElement("p");
    novo.textContent = "Primmeiro parágrafo substituido";
    const primeiro = container.firstElementChild;
    primeiro.replaceWith(novo);
});

// btnCard - Criar card com botão de remover
document.getElementById("btnCard").addEventListener("click", () => {
    const card = document.createElement("div");
    card.className ="card";

    const titulo = document.createElement("h3");
    titulo.textContent = "Card Dinâmico";

    const btnRemover = document.createElement("button");
    btnRemover.textContent = "Remover";
    btnRemover.addEventListener("click", () => {
        container.removeChild(card);
    });
    card.appendChild(titulo);
    card.appendChild(btnRemover);
    container.appendChild(card);
});

// 6 Manipulação de texto con textContent
document.getElementById("btnTextContent").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Texto adicionado com textContent";
    container.appendChild(p);
});

// 7 Manipulação de texto com innerHTML
document.getElementById("btnInnerHTML").addEventListener("click", () => {
    const p = document.createElement("p");
    p.innerHTML = "<strong>Texto em negrito</strong> usando innerHTML";
    container.appendChild(p);
});