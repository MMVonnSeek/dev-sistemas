const botao = document.getElementById('botao');
const imagem = document.getElementById('imagem');

botao.addEventListener('click', function() {
    console.log('Botão clicado! Vamos buscar um gato...')
    fetch('https://api.thecatapi.com/v1/images/search')

    .then(function(resposta){
        console.log('Resposta HTTP Recebida');
        console.log('Status Code:', resposta.status); //200
        console.log('Headers:', resposta.headers);
        return resposta.json();
    })

    .then(function(dados) {
        console.log('Dados estraídos (JSON - Objeto JS):', dados);

        const urlDoGato = dados[0].url;
        console.log('URL da imagem:', urlDoGato);

        imagem.src = urlDoGato;
        imagem.style.display = 'block';

        console.log('Imagem carregada com sucesso')
    });
});