const botao = document.getElementById("buscar");
const resultado = document.getElementById("resultado");
botao.addEventListener("click", () => {
    const cep = document.getElementById("cep").value;
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(resposta => resposta.json())
        .then(dados => {
            if (dados.erro) {
                resultado.innerHTML = "<p>CEP não encontrado.</p>";
                return;
            }
            resultado.innerHTML = `
                <h2>Endereço encontrado</h2>
                <p><strong>Logradouro:</strong> ${dados.logradouro}</p>
                <p><strong>Bairro:</strong> ${dados.bairro}</p>
                <p><strong>Cidade:</strong> ${dados.localidade}</p>
                <p><strong>UF:</strong> ${dados.uf}</p>
            `;
        })
        .catch(erro => {
            resultado.innerHTML = "<p>Erro ao consultar o CEP.</p>";
            console.error(erro);
        });
});