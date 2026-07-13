# 🤖 LinkedIn Automation Bot (Selenium)

Este é um projeto em Python focado na automação web e teste de fluxos no **LinkedIn** utilizando **Selenium WebDriver**. O robô valida os componentes do ambiente, gerencia dependências e realiza testes estruturados de autenticação.

---

## 🚀 Estrutura do Projeto

* **`test_chromedriver.py`**: Localiza, baixa e valida o funcionamento do ChromeDriver de acordo com a versão do seu navegador Google Chrome.
* **`test_dependencies.py`**: Verifica se as bibliotecas cruciais para o projeto estão instaladas e na versão correta.
* **`test_login.py`**: Realiza o fluxo de login automatizado na página do LinkedIn, tratando possíveis barreiras como CAPTCHAs, além de validar se o redirecionamento para o feed ocorreu com sucesso.
* **`test_search.py`**: Script complementar integrado para fluxos internos de busca.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python** (Linguagem base)
* **Selenium WebDriver** (Interação e automação de navegadores)
* **Webdriver Manager** (Gerenciamento automático de drivers do Chrome)
* **Python-Dotenv** (Gerenciamento seguro de variáveis de ambiente/credenciais)

---

## 📦 Como Instalar e Rodar o Projeto

### 1. Preparar as credenciais
Antes de rodar os testes de login, crie um arquivo chamado `.env` na raiz do seu projeto local e insira suas credenciais (este arquivo não será enviado para o GitHub por questões de segurança):


### 💡 Nota importante sobre segurança:
Como você me enviou o arquivo `.env`, reparei que sua senha e email reais do LinkedIn estavam expostos ali[cite: 1]. Como você seguiu as boas práticas e adicionou o `.env` ao `.gitignore`[cite: 2], **esses dados não foram enviados para o GitHub**, o que é ótimo! 

Porém, caso você queira alterar sua senha do LinkedIn por pura precaução agora que ela passou por uma IA, é uma boa prática de segurança que programadores fazem sempre.
```env
LINKEDIN_EMAIL=seu_email@exemplo.com
LINKEDIN_SENHA=sua_senha_aqui
