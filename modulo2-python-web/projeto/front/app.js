// front/app.js -- Consome a API de Tarefas FastAPI
const BASE = 'http://localhost:8000';

// ── Elementos do DOM ─────────────────────────────────────────
const listaEl   = document.querySelector('#lista');
const loadingEl = document.querySelector('#loading');
const erroEl    = document.querySelector('#erro');
const resumoEl  = document.querySelector('#resumo');
const modalEl   = document.querySelector('#modal-tarefa');
const formEl    = document.querySelector('#form-tarefa');

// ── Estados visuais ───────────────────────────────────────────
const mostrarLoading = () => { loadingEl.classList.remove('hidden'); erroEl.classList.add('hidden'); listaEl.classList.add('hidden'); };
const mostrarErro    = (m) => { loadingEl.classList.add('hidden'); erroEl.classList.remove('hidden'); erroEl.textContent = m; };
const mostrarLista   = () => { loadingEl.classList.add('hidden'); erroEl.classList.add('hidden'); listaEl.classList.remove('hidden'); };

// ── Renderizar cards ──────────────────────────────────────────
const renderizar = (tarefas) => {
    listaEl.innerHTML = tarefas.map(t => `
        <article class="card-tarefa ${t.prioridade}" data-id="${t.id}">
            <p class="card-titulo">${t.titulo}</p>
            ${t.descricao ? `<p class="card-desc">${t.descricao}</p>` : ''}
            <div class="card-meta">
                <span class="badge badge-${t.status}">${t.status.replace('_',' ')}</span>
                <span class="badge">${t.prioridade}</span>
                ${t.responsavel ? `<span>${t.responsavel}</span>` : ''}
                ${t.prazo ? `<span>Prazo: ${t.prazo}</span>` : ''}
            </div>
            <div class="card-acoes">
                ${t.status !== 'concluida' ? `<button class="btn-concluir" data-id="${t.id}">Concluir</button>` : ''}
                <button class="btn-deletar" data-id="${t.id}">Remover</button>
            </div>
        </article>
    `).join('');
    mostrarLista();
};

// ── Buscar estatisticas ───────────────────────────────────────
const atualizarResumo = async () => {
    try {
        const r = await fetch(`${BASE}/tarefas/estatisticas`);
        const d = await r.json();
        resumoEl.textContent =
            `Total: ${d.total} | Pendentes: ${d.por_status.pendente} | Em andamento: ${d.por_status.em_andamento} | Concluidas: ${d.por_status.concluida}`;
    } catch { resumoEl.textContent = ''; }
};

// ── Listar tarefas ────────────────────────────────────────────
const listar = async () => {
    mostrarLoading();
    const status     = document.querySelector('#filtro-status').value;
    const prioridade = document.querySelector('#filtro-prioridade').value;
    const params     = new URLSearchParams();
    if (status)     params.append('status', status);
    if (prioridade) params.append('prioridade', prioridade);
    try {
        const r = await fetch(`${BASE}/tarefas?${params}`);
        if (!r.ok) throw new Error(`Erro ${r.status}`);
        renderizar(await r.json());
        await atualizarResumo();
    } catch (e) { mostrarErro(e.message); }
};

// ── Criar tarefa via modal ────────────────────────────────────
formEl.addEventListener('submit', async (e) => {
    e.preventDefault();
    const dados = {
        titulo:      document.querySelector('#titulo').value,
        descricao:   document.querySelector('#descricao').value || null,
        responsavel: document.querySelector('#responsavel').value || null,
        prioridade:  document.querySelector('#prioridade').value,
        prazo:       document.querySelector('#prazo').value || null,
    };
    try {
        const r = await fetch(`${BASE}/tarefas`, {
            method:'POST', headers:{'Content-Type':'application/json'},
            body:JSON.stringify(dados),
        });
        if (!r.ok) { const err = await r.json(); throw new Error(err.detail); }
        modalEl.close();
        formEl.reset();
        await listar();
    } catch (e) { alert(`Erro: ${e.message}`); }
});

// ── Event delegation: concluir e deletar ─────────────────────
listaEl.addEventListener('click', async (e) => {
    const id = e.target.dataset.id;
    if (!id) return;
    if (e.target.classList.contains('btn-concluir')) {
        await fetch(`${BASE}/tarefas/${id}`, {
            method:'PATCH', headers:{'Content-Type':'application/json'},
            body:JSON.stringify({status:'concluida'}),
        });
        await listar();
    }
    if (e.target.classList.contains('btn-deletar')) {
        if (!confirm('Remover esta tarefa?')) return;
        await fetch(`${BASE}/tarefas/${id}`, { method:'DELETE' });
        await listar();
    }
});

// ── Modal ─────────────────────────────────────────────────────
document.querySelector('#btn-nova').addEventListener('click', () => { formEl.reset(); modalEl.showModal(); });
document.querySelector('#btn-cancelar').addEventListener('click', () => modalEl.close());
document.querySelector('#btn-filtrar').addEventListener('click', listar);

// Inicializar
listar();
