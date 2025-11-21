# 📊 Análise: Magnificent Seven & S&P 500

Trabalho acadêmico desenvolvido para a disciplina de **Métodos Quantitativos Aplicados à Administração**.

**Autor:** Iago Santos Azevedo  
**Período de Análise:** Janeiro/2022 - Dezembro/2024

## 🎯 Objetivo

Analisar empiricamente a influência do desempenho das maiores empresas de tecnologia, conhecidas como as **"Magnificent Seven"**, sobre o retorno e a volatilidade do índice de mercado S&P 500.

## 🏢 Empresas Analisadas (Magnificent Seven)

- 🍎 Apple (AAPL)
- 🪟 Microsoft (MSFT)
- 🔍 Alphabet/Google (GOOGL)
- 📦 Amazon (AMZN)
- 🎮 Nvidia (NVDA)
- 🚗 Tesla (TSLA)
- 📱 Meta Platforms (META)

## 📋 Estrutura do Projeto

```
Pesquisa - Métodos/
│
├── app.py                          # Aplicação Streamlit principal
├── coletar_dados.py                # Script de coleta e processamento de dados
├── extract_pdf.py                  # Script auxiliar de extração do PDF
├── extract_pdf_better.py           # Versão melhorada de extração
│
├── dados_precos.csv                # Dados de preços coletados
├── dados_retornos.csv              # Dados de retornos calculados
├── dados_pesos_bigtech.csv         # Pesos do Big Tech Index
├── conteudo_pdf.txt                # Texto extraído do PDF
│
└── Métodos - Iago Santos Azevedo - Seções 1, 2 e 3 do trabalho final.pdf
```

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip install streamlit pandas numpy yfinance plotly PyPDF2 pillow
```

### 2. Coletar e Processar Dados

Execute o script de coleta de dados:

```bash
python coletar_dados.py
```

Este script irá:
- ✅ Coletar preços diários do S&P 500 e das Magnificent Seven
- ✅ Coletar dados do VIX e Taxa de Juros 10Y
- ✅ Calcular retornos logarítmicos
- ✅ Construir o Big Tech Index ponderado por capitalização
- ✅ Gerar estatísticas descritivas
- ✅ Salvar dados processados em CSV

**Período:** 01/01/2022 a 31/12/2024  
**Fonte de Dados:** Yahoo Finance (via yfinance)

### 3. Executar Dashboard Streamlit

```bash
streamlit run app.py
```

O dashboard estará disponível em: **http://localhost:8501**

## 📊 Dados Coletados

### Variáveis Principais

| Variável | Ticker | Descrição |
|----------|--------|-----------|
| S&P 500 | ^GSPC | Índice de mercado principal |
| VIX | ^VIX | Índice de volatilidade implícita |
| Taxa de Juros 10Y | ^TNX | Yield do Tesouro Americano |
| Big Tech Index | - | Índice ponderado das Magnificent Seven |

### Processamento de Dados

1. **Retornos Logarítmicos:**
   ```python
   retorno = np.log(preco_hoje / preco_ontem)
   ```

2. **Big Tech Index:**
   - Cálculo de capitalização de mercado diária
   - Ponderação por market cap
   - Retorno ponderado: `Σ(peso_i × retorno_i)`

## 📈 Funcionalidades do Dashboard

### 🏠 Página Inicial
- Visão geral do estudo
- Métricas principais
- Objetivos e metodologia

### 📄 Resumo
- Resumo executivo do trabalho
- Palavras-chave
- Contexto da pesquisa

### 📖 Introdução
- Contextualização do problema
- Questão de pesquisa
- Hipótese central

### 📚 Referencial Teórico
- Mercado americano e concentração setorial
- Risco e retorno em mercados de ações
- Big Tech como fator sistêmico

### 🔬 Metodologia
- Tipo de pesquisa
- Instrumentos de coleta
- Técnicas de análise
- Modelos analíticos

### 📊 Dados Coletados
- **Séries Temporais:** Evolução dos preços e índices
- **Retornos:** Distribuição e correlações
- **Pesos Big Tech:** Composição do índice ao longo do tempo
- **Dados Brutos:** Tabelas completas e download

### 📈 Análise Estatística
- Estatísticas descritivas
- Matriz de correlação interativa
- Análise de volatilidade
- Principais achados

### 📋 Quadros
- Definição das variáveis
- Estrutura dos modelos de regressão

### 📚 Referências
- Bibliografia completa

## 🔬 Metodologia

### Tipo de Pesquisa
- **Natureza:** Descritiva
- **Abordagem:** Quantitativa
- **Técnica:** Análise de séries temporais

### Modelos Analíticos

**Modelo 1: Retorno S&P 500**
```
R_SP500,t = β₀ + β₁ R_Tech,t + β₂ Juros_t + ε_t
```

**Modelo 2: Volatilidade (VIX)**
```
VIX_t = β₀ + β₁ R_Tech,t + β₂ Juros_t + ε_t
```

### Técnicas Estatísticas
- ✅ Teste de Dickey-Fuller Aumentado (ADF)
- ✅ Correlação de Pearson
- ✅ Regressão Linear Múltipla
- ✅ Análise de séries temporais

## 📊 Principais Resultados

### Correlações Observadas
- **S&P 500 vs Big Tech Index:** Correlação forte e positiva (≈0.87)
- **VIX vs Retornos:** Correlação negativa, confirmando papel de "índice do medo"
- **Taxa de Juros:** Correlação negativa com VIX

### Volatilidade
- Big Tech Index apresenta maior volatilidade que o S&P 500
- Reflete risco concentrado no setor de tecnologia

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **Streamlit** - Dashboard interativo
- **pandas** - Manipulação de dados
- **numpy** - Cálculos numéricos
- **yfinance** - Coleta de dados financeiros
- **plotly** - Visualizações interativas
- **PyPDF2** - Extração de texto do PDF

## 📝 Notas Importantes

1. Os dados são coletados diretamente do Yahoo Finance
2. O Big Tech Index usa preços como proxy para capitalização de mercado
3. Para produção, recomenda-se usar dados de shares outstanding
4. Todos os retornos são calculados como logarítmicos
5. As séries temporais são testadas para estacionariedade

## 🎓 Contexto Acadêmico

Este trabalho investiga a crescente concentração do mercado de ações americano no setor de tecnologia e seus impactos sobre:

- 🎯 Risco sistêmico
- 📊 Diversificação de portfólio
- 💹 Gestão de risco
- 📈 Estratégias de investimento

## 📧 Contato

**Autor:** Iago Santos Azevedo  
**Disciplina:** Métodos Quantitativos Aplicados à Administração  
**Ano:** 2024

---

**© 2024 - Trabalho Acadêmico**
