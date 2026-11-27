document.addEventListener("DOMContentLoaded", function() {
    
// 1. Duplo clique    
    const duploClique = document.getElementById("duploClique");
    duploClique.addEventListener("dblclick", function() {
        alert("Você deu um duplo clique nesse parágrafo");
        console.log("this se refere a: ", this); // Exibe o elemento clicado
    });

// Demonstração arrow function x função regular
    duploClique.addEventListener("click", () => {
        console.log("Arrow function this: ", this);
    });

// 2. Remoção de elementos
const btnRemoveritem2 = document.getElementById("btnRemoverItem2");
const lista = document.getElementById("lista");

btnRemoverItem2.addEventListener("click", function() {
    const item2 = document.getElementById("item2");
    if (item2) {
        item2.remove(); // método moderno
        console.log("item2 removido usado remove()")
    }
});

// Remoção com this.removeChild() para item 3
const item3 = document.getElementById("item3");
if(item3) {
    lista.removeChild(item3); // Método mais antigo
    console.log("Item 3 removido usando removeChild()");
}

// 3. Delegação de eventos
const tarefas = document.getElementById("tarefas");
const btnAdicionarTarefa = document.getElementById("btnAdicionarTarefa");
let contador = 4;

// Adicionar novas tarefas dinamicamante
btnAdicionarTarefa.addEventListener("click", function() {
    const li = document.createElement("li");
    li.textContent = "Tarefa " + contador;
    contador++;
    tarefas.appendChild(li);
});

// Delegação: remover tarefas ao clicar
tarefas.addEventListener("click", function() {
    if(event.target.tagName === "LI") {
        event.target.remove();
        console.log("Tarefa removida: ", event.target.textContent);
    }
});
});