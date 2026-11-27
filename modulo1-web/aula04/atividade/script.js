document.addEventListener("DOMContentLoaded", function() {
    const caixas = [
        document.getElementById("caixa1"),
        document.getElementById("caixa2"),
        document.getElementById("caixa3")
    ];

// cores possiveis para alternar
const cores = ["red", "green", "blue", "orange", "purple"];

// função auxiliar: pega índice da cor atual e retornar p/ prox.
  function proximaCorAtual(element) { 
    const estilo = getComputedStyle(element); 
    const bg = estilo.backgroundColor; // retorna rgb(...) 
   
    // tenta mapear rgb para nome aproximado por comparação simples com cores definidas 
    for (let c of cores) { 
      const temp = document.createElement("div"); 
      temp.style.background = c; 
      document.body.appendChild(temp); 
      const comp = getComputedStyle(temp).backgroundColor; 
      document.body.removeChild(temp); 
      if (comp === bg) { 
        
        // encontrou; retorna próxima cor do array 
        const idx = cores.indexOf(c); 
        return cores[(idx + 1) % cores.length]; 
      } 
    } 
    
    // se não identificou, retorna primeira cor 
    return cores[0]; 
  } 
 
  caixas.forEach((caixa, index) => { 
    if (!caixa) return; 
 
    // dblclick: trocar cor e alert com o nome 
    caixa.addEventListener("dblclick", function() { 
      const nova = proximaCorAtual(this); 
      this.style.background = nova; 
      alert(`Cor alterada para: ${nova}`); 
      console.log("this (elemento que disparou dblclick):", this); 
    }); 
 
    // clique simples via arrow function para demonstrar this herdado 
    caixa.addEventListener("click", () => { 
      console.log("Arrow function this (não é o elemento):", this); 
    }); 
  });
});