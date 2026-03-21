# 🚢 Monitor de Gate BTP

Aplicação web simples para monitoramento de abertura de gate (DRY) do terminal **BTP**, com atualização automática em tela.

---

## 📌 Objetivo

Automatizar a consulta de disponibilidade de gates de exportação e exibir em tempo real os navios com abertura prevista para:

* Hoje
* D+1

---

## 🧱 Estrutura do Projeto

```
robo_btp/
│
├── app.py              # Servidor Flask (rotas e API)
├── scraper.py          # Coleta de dados (requisição ao portal BTP)
├── parser.py           # Tratamento e filtro dos dados
│
├── templates/
│   └── index.html      # Interface web
│
└── static/
    └── js/
        └── main.js     # Lógica frontend (requisições e renderização)
```

---

## ⚙️ Tecnologias utilizadas

* Python
* Flask
* Requests
* BeautifulSoup
* JavaScript (frontend)

---

## 🚀 Como executar

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install flask requests beautifulsoup4
```

---

### 4. Executar a aplicação

```bash
python app.py
```

---

### 5. Acessar no navegador

```
http://localhost:5000
```

---

## 🔄 Funcionamento

* O backend realiza uma requisição ao sistema da BTP
* Os dados são filtrados para gates DRY (Hoje + D+1)
* O frontend consome a API `/gates`
* A tela é atualizada automaticamente a cada 30 segundos

---

## 📈 Possíveis melhorias

* Destaque visual para novos gates
* Cache para otimização de requisições
* Dashboard com layout aprimorado
* Deploy como serviço no servidor

---

## ⚠️ Observações

* A aplicação depende da estrutura atual do portal da BTP
* Mudanças no sistema podem impactar o funcionamento

---

## 👨‍💻 Autor

Projeto desenvolvido para automação e melhoria operacional no monitoramento de gates portuários.
