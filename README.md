<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1F9BD4,50:2E75B6,100:16265F&height=200&section=header&text=TesteUnitariosIA&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Agentes+de+IA+que+geram%2C+executam+e+documentam+testes+unitários+automaticamente&descAlignY=58&descSize=16&animation=fadeIn" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-1F9BD4?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Azure](https://img.shields.io/badge/Azure-OpenAI-2E75B6?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![LangChain](https://img.shields.io/badge/LangChain-Agents-16265F?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![TDD](https://img.shields.io/badge/TDD-Red→Green→Refactor-1F9BD4?style=for-the-badge)](https://github.com/fassir/TesteUnitariosIA)
[![Status](https://img.shields.io/badge/Status-Ativo-2E75B6?style=for-the-badge)](https://github.com/fassir/TesteUnitariosIA)

</div>

---

## 🧪 Sobre o Projeto

<div align="center">

> *"O código que se testa sozinho é o futuro do desenvolvimento de software."*

</div>

O **TesteUnitariosIA** é um sistema de agentes inteligentes que automatiza completamente o ciclo de **Test-Driven Development (TDD)**. Utilizando **LangChain** com **Azure ChatGPT** como backbone, os agentes recebem uma função Python e autonomamente:

1. **Analisam** a lógica e os casos de uso
2. **Geram** uma suíte completa de testes unitários
3. **Executam** os testes via `PythonREPLTool`
4. **Documentam** os resultados com relatório estruturado

Este projeto representa a fusão entre **Engenharia de Software** e **IA Generativa**, automatizando uma das tarefas mais críticas — e frequentemente negligenciadas — no desenvolvimento de software.

### ✨ Por que esse projeto importa?

| Problema | Solução |
|---|---|
| 🕐 Testes consomem muito tempo | Geração automática em segundos |
| 🤔 Casos extremos esquecidos | IA cobre edge cases sistematicamente |
| 📄 Documentação inconsistente | Relatório gerado automaticamente |
| 🔁 Ciclo TDD manual e lento | Pipeline Red → Green → Refactor automatizado |
| 🧩 Cobertura baixa de código | Suíte completa por função analisada |

---

## 🔄 Como Funciona — Fluxo dos Agentes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PIPELINE DE GERAÇÃO DE TESTES COM IA                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ENTRADA                AGENTE IA               EXECUÇÃO              │
│                                                                         │
│  def soma(a, b):   ──►  Azure ChatGPT  ──►   PythonREPLTool           │
│      return a + b        LangChain             pytest/unittest          │
│                          Analysis              Executa os testes        │
│                                                                         │
│   RESULTADO              RELATÓRIO             CICLO TDD               │
│                                                                         │
│  ✅ 8/8 passed    ──►  Markdown Doc   ──►   Red → Green → Refactor    │
│  ❌ 1 falhou             gerado auto           Iteração automática      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 🤖 Arquitetura dos Agentes

```
AgentOrchestrator
│
├── 🔍 AnalysisAgent       → Lê a função, identifica tipos, contratos e edge cases
├── ✍️  GeneratorAgent      → Cria os testes unitários (pytest style)
├── ⚡ ExecutorAgent        → Roda os testes via PythonREPLTool
├── 🔧 RefactorAgent        → Corrige testes que falharam (ciclo Green)
└── 📊 ReporterAgent        → Documenta resultados em Markdown estruturado
```

### 🔴🟢🔵 Ciclo TDD Automatizado

```python
# RED  — Testes gerados falham intencionalmente (sem implementação completa)
# GREEN — IA ajusta/valida a função para passar em todos os testes
# REFACTOR — Código limpo e testes documentados são entregues
```

---

## 🛠️ Stack de Tecnologias

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=python,azure&theme=dark)](https://skillicons.dev)

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![OpenAI](https://img.shields.io/badge/Azure_OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black)

</div>

| Biblioteca / Serviço | Versão | Função |
|---|---|---|
| `langchain` | ≥ 0.1 | Orquestração dos agentes de IA |
| `langchain-openai` | ≥ 0.0.5 | Integração com Azure ChatGPT |
| `openai` | ≥ 1.0 | Cliente Azure OpenAI |
| `python-dotenv` | ≥ 1.0 | Gerenciamento de variáveis de ambiente |
| `pytest` | ≥ 7.0 | Framework de testes |
| **Azure OpenAI** | — | LLM hospedado no Azure |

---

## 🚀 Instalação e Configuração

<details>
<summary><b>📦 1. Clone e instale dependências</b></summary>

```bash
# Clone o repositório
git clone https://github.com/fassir/TesteUnitariosIA.git
cd TesteUnitariosIA

# Crie e ative ambiente virtual
python -m venv venv
source venv/bin/activate       # Linux/macOS
# venv\Scripts\activate        # Windows

# Instale dependências
pip install langchain langchain-openai openai python-dotenv pytest
```

</details>

<details>
<summary><b>🔑 2. Configure as variáveis de ambiente</b></summary>

Crie um arquivo `.env` na raiz do projeto:

```bash
# .env — Configuração Azure OpenAI
AZURE_OPENAI_API_KEY=sua_api_key_aqui
AZURE_OPENAI_ENDPOINT=https://seu-recurso.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-01
```

> ⚠️ **Nunca commit o arquivo `.env`** — certifique-se que está no `.gitignore`

</details>

<details>
<summary><b>☁️ 3. Pré-requisitos Azure</b></summary>

Para usar Azure OpenAI você precisa:

1. Uma **Subscription Azure** ativa
2. Um recurso **Azure OpenAI** criado no portal
3. Um **deployment** do modelo GPT-4 ou GPT-3.5-Turbo
4. A **API Key** e o **endpoint** do seu recurso

```bash
# Verifique se o recurso está acessível
curl https://SEU_ENDPOINT.openai.azure.com/openai/deployments \
  -H "api-key: SUA_API_KEY"
```

</details>

<details>
<summary><b>▶️ 4. Execute o agente</b></summary>

```python
# Modo básico — passe uma função e veja os testes gerados
python agente_testes.py

# Modo com arquivo específico
python agente_testes.py --arquivo minha_funcao.py --funcao calcular_desconto
```

```python
# Exemplo programático
from agente_testes import TesteUnitariosAgent

agente = TesteUnitariosAgent()

codigo = """
def calcular_desconto(preco: float, percentual: float) -> float:
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido")
    return preco * (1 - percentual / 100)
"""

resultado = agente.gerar_e_executar(codigo)
print(resultado.relatorio)
```

```
# Saída esperada:
# ✅ test_desconto_simples         PASSED
# ✅ test_desconto_zero            PASSED
# ✅ test_desconto_total           PASSED
# ✅ test_percentual_negativo      PASSED (raises ValueError)
# ✅ test_percentual_acima_100     PASSED (raises ValueError)
# ✅ test_preco_zero               PASSED
# ❌ test_tipo_invalido            FAILED → corrigindo...
# ✅ test_tipo_invalido            PASSED (após refactor)
# 
# 📊 Resultado: 7/7 testes passando | Cobertura estimada: 94%
```

</details>

---

## ✅ Funcionalidades

| # | Funcionalidade | Descrição | Status |
|---|---|---|---|
| 1 | 🔍 **Análise de função** | O agente lê e compreende a lógica, tipos e contratos | ✅ Implementado |
| 2 | ✍️ **Geração de testes** | Cria testes `pytest` cobrindo happy path e edge cases | ✅ Implementado |
| 3 | ⚡ **Execução automática** | Roda os testes via `PythonREPLTool` sem sair do pipeline | ✅ Implementado |
| 4 | 🔧 **Auto-correção** | Refatora testes que falham e reexecuta o ciclo | ✅ Implementado |
| 5 | 📊 **Relatório Markdown** | Documenta cada teste com status, mensagem e cobertura | ✅ Implementado |
| 6 | 🔄 **Ciclo TDD** | Red → Green → Refactor totalmente automatizado | ✅ Implementado |
| 7 | ☁️ **Azure OpenAI** | Integração com deployment GPT-4 via env vars | ✅ Implementado |
| 8 | 🔐 **Segurança** | Credenciais isoladas em `.env`, nunca hardcoded | ✅ Implementado |

---

## 📁 Estrutura de Arquivos

```
TesteUnitariosIA/
│
├── 📄 agente_testes.py          # Orquestrador principal dos agentes
├── 📂 agentes/
│   ├── analise_agent.py         # Análise e compreensão da função
│   ├── gerador_agent.py         # Geração de testes unitários
│   ├── executor_agent.py        # Execução via PythonREPLTool
│   ├── refactor_agent.py        # Auto-correção de testes falhos
│   └── reporter_agent.py        # Geração de relatório final
│
├── 📂 exemplos/
│   ├── funcao_simples.py        # Caso de uso básico
│   ├── funcao_complexa.py       # Caso com múltiplas regras de negócio
│   └── relatorios/              # Relatórios gerados automaticamente
│
├── 📄 .env.example              # Modelo de configuração (sem segredos)
├── 📄 requirements.txt          # Dependências do projeto
└── 📄 README.md                 # Documentação
```

---

## 📊 Exemplo de Relatório Gerado

<details>
<summary><b>📄 Ver relatório de exemplo</b></summary>

```markdown
## Relatório de Testes — calcular_desconto()
**Data:** 2025-01-15 14:32:07
**Modelo:** Azure GPT-4 (gpt-4-turbo)
**Ciclos TDD:** 2

| Teste | Resultado | Tempo |
|---|---|---|
| test_desconto_simples | ✅ PASSED | 0.002s |
| test_desconto_zero | ✅ PASSED | 0.001s |
| test_desconto_total | ✅ PASSED | 0.001s |
| test_percentual_negativo | ✅ PASSED | 0.003s |
| test_tipo_invalido | ✅ PASSED* | 0.002s |

*Corrigido na iteração 2 do ciclo TDD

**Cobertura estimada:** 94%
**Testes gerados:** 5 | **Passando:** 5/5
```

</details>

---

## 👨‍💻 Autor

<div align="center">

| | |
|---|---|
| **Nome** | Fabio Piassi |
| **Formação** | Física · Ciência de Dados · IA · DevSecOps |
| **Especialidade** | IA Aplicada · LangChain · Azure · TDD |
| **Localização** | Volta Redonda — RJ 🇧🇷 |
| **GitHub** | [@fassir](https://github.com/fassir) |

[![GitHub](https://img.shields.io/badge/GitHub-fassir-1F9BD4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fassir)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Fabio_Piassi-2E75B6?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/fassir)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16265F,50:2E75B6,100:1F9BD4&height=120&section=footer&fontSize=14&fontColor=ffffff&text=TesteUnitariosIA+·+by+Fabio+Piassi&fontAlignY=65" />

*"Qualidade não é um ato, é um hábito — e agora, é também um agente."*

</div>
