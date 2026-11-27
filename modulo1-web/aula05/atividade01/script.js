document.getElementById("buscar").addEventListener("click", () => {
    let nome = document.getElementById("usuario").value;
    fetch(`https://api.github.com/users/${nome}`)
    .then((r) => r.json())
    .then((user) => {
        document.getElementById("perfil").innerHTML = `
        <img src="${user.avatar_url}" width="130"
        <h3>${user.name || "Sem nome"}</h3>
        <p>${user.bio || "Sem bio"}</p>`;
    });
});