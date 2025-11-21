# 📊 Magnificent Seven & S&P 500 - Análise Estatística

[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](http://localhost:8501)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-blue)](LICENSE)

> ⚡ **PRONTO PARA USO:** Este repositório já contém todos os dados pré-processados! Execute o dashboard imediatamente após clonar, sem precisar rodar scripts de coleta.

---

## 📖 Sobre o Projeto

Trabalho acadêmico que analisa empiricamente a **influência do desempenho e concentração do setor de tecnologia** (Magnificent Seven) sobre a **volatilidade e retorno do índice S&P 500** durante o período de **janeiro de 2022 a dezembro de 2024**.

**Autor:** Iago Santos Azevedo  
**Disciplina:** Métodos Quantitativos Aplicados à Administração  
**Período:** 2022-2024 (752 dias de negociação)

---

## 🏢 Empresas Analisadas (Magnificent Seven)

| Empresa | Ticker | Setor |
|---------|--------|-------|
| 🍎 Apple | AAPL | Tecnologia |
| 🪟 Microsoft | MSFT | Tecnologia |
| 🔍 Alphabet/Google | GOOGL | Tecnologia |
| 📦 Amazon | AMZN | E-commerce/Cloud |
| 🎮 NVIDIA | NVDA | Semicondutores/IA |
| 🚗 Tesla | TSLA | Automotivo/Energia |
| 📱 Meta | META | Redes Sociais |

---

## 🤖 Assistente IA (Opcional)

O dashboard inclui um **Assistente IA** alimentado pelo Google Gemini que explica análises e termos estatísticos de forma simples e interativa.

### ⚡ Configuração Rápida (3 passos):

1. **Obter chave API grátis:** https://makersuite.google.com/app/apikey
2. **Editar arquivo:** `.streamlit/secrets.toml` (cole sua chave)
3. **Recarregar:** Pressione R no terminal ou F5 no navegador

📖 **Guia completo:** Veja `CONFIGURAR_IA.md`

> ⚠️ Sem a API, o dashboard funciona normalmente mas mostra um glossário estático ao invés do chat interativo.

---

## 🚀 Início Rápido

### Opção 1: Visualização Imediata (Recomendada) ⚡

```bash
# 1. Clone o repositório
git clone https://github.com/iago-azevedo-py/Analise-Magnifique-Seven.git
cd Analise-Magnifique-Seven

# 2. Crie ambiente virtual (opcional mas recomendado)
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute o dashboard
streamlit run app.py
```

✅ **Pronto!** O dashboard abrirá em `http://localhost:8501` com todas as análises prontas.

### Opção 2: Atualizar Dados 🔄

Para coletar dados mais recentes do Yahoo Finance:

```bash
# 1. Coletar novos dados
python coletar_dados.py

# 2. Executar análises estatísticas
python analises_estatisticas.py

# 3. Visualizar no dashboard
streamlit run app.py
```

---

## 📊 Dados Incluídos

O repositório já contém todos os dados processados:

### Datasets (CSV)
- ✅ `dados_final.csv` - Dataset principal (751 observações)
- ✅ `dados_precos.csv` - Preços diários históricos
- ✅ `dados_retornos.csv` - Retornos logarítmicos
- ✅ `dados_final_sem_outliers.csv` - Dataset limpo (663 obs.)
- ✅ `estatisticas_descritivas.csv` - Estatísticas completas
- ✅ `matriz_correlacao.csv` - Correlações de Pearson
- ✅ `regressao_multipla.csv` - Resultados dos modelos
- ✅ `erro_amostral.csv` - Intervalos de confiança

### Visualizações (HTML Interativos)
- ✅ `scatter_modelo1.html` - Regressão S&P 500 vs Big Tech
- ✅ `scatter_modelo2.html` - Regressão VIX vs Big Tech
- ✅ `scatter_vix_juros.html` - VIX vs Taxa de Juros
- ✅ `heatmap_correlacao.html` - Heatmap de correlações
- ✅ `boxplots_outliers.html` - Identificação de outliers

---

## 🎯 Funcionalidades do Dashboard

O dashboard interativo possui **11 seções completas**:

| Seção | Descrição |
|-------|-----------|
| 🏠 **Início** | Apresentação e visão geral |
| 📄 **Resumo** | Resumo executivo e palavras-chave |
| 📖 **Introdução** | Contexto, questão de pesquisa e hipótese |
| 📚 **Referencial Teórico** | Base teórica e literatura |
| 🔬 **Metodologia** | Métodos, técnicas e modelos |
| 📊 **Dados Coletados** | Séries temporais e visualizações |
| 📈 **Análise Estatística** | Estatísticas descritivas e correlações |
| 🔮 **Regressão Linear** | Modelos econométricos (2 modelos) |
| 📋 **Quadros** | Tabelas e definições |
| 🎯 **Conclusão** | Síntese, limitações e pesquisas futuras |
| 📚 **Referências** | Bibliografia completa |

---

## 📈 Principais Resultados

### 🔍 Modelo 1: Retorno S&P 500
```
retorno_sp500 = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε
```

- **R² = 0.7554** (75.54% de poder explicativo)
- **β₁ = 0.4892*** (altamente significativo, p < 0.001)
- **F-statistic = 1154.86***

**Interpretação:** Para cada 1% de aumento no retorno do Big Tech Index, o S&P 500 aumenta em média 0.49%.

### 📉 Modelo 2: Volatilidade (VIX)
```
vix = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε
```

- **R² = 0.3766** (37.66% de poder explicativo)
- **β₁ = -46.18*** (p < 0.001)
- **β₂ = -4.57*** (p < 0.001)
- **F-statistic = 225.92***

**Interpretação:** Retornos positivos do Big Tech reduzem a volatilidade do mercado (efeito estabilizador).

### 🔗 Correlações Chave
- **S&P 500 vs Big Tech Index:** r = 0.8691 (correlação muito forte)
- **VIX vs Taxa de Juros:** r = -0.5931 (correlação negativa moderada)
- **VIX vs Retornos:** correlação negativa (confirma "índice do medo")

---

## 🛠️ Tecnologias Utilizadas

```yaml
Linguagem: Python 3.13+
Dashboard: Streamlit 1.28+
Dados: yfinance 0.2+
Análise: pandas 2.0+, numpy 1.24+
Visualização: plotly 5.17+
Estatística: statsmodels 0.14+, scikit-learn 1.3+
```

---

## 📁 Estrutura do Projeto

```
Analise-Magnifique-Seven/
│
├── 📊 app.py                          # Dashboard Streamlit (1750+ linhas)
├── 📥 coletar_dados.py                # Coleta de dados Yahoo Finance
├── 📈 analises_estatisticas.py       # Análises estatísticas completas
├── 📄 extract_pdf_better.py           # Extração de texto do PDF
│
├── 📊 Dados CSV (15 arquivos)
│   ├── dados_final.csv
│   ├── estatisticas_descritivas.csv
│   ├── matriz_correlacao.csv
│   ├── regressao_multipla.csv
│   └── ...
│
├── 📈 Gráficos HTML (5 arquivos)
│   ├── scatter_modelo1.html
│   ├── heatmap_correlacao.html
│   └── ...
│
├── 📝 Documentação
│   ├── README.md
│   ├── QUICK_START.md
│   ├── requirements.txt
│   └── .gitignore
│
└── 📚 Métodos - Iago Santos Azevedo.pdf
```

---

## 🔬 Metodologia

### Tipo de Pesquisa
- **Natureza:** Descritiva e quantitativa
- **Abordagem:** Análise de séries temporais
- **Período:** 2022-2024 (752 dias de negociação)

### Técnicas Estatísticas Aplicadas
- ✅ Estatísticas descritivas completas (média, mediana, quartis, IQR, assimetria, curtose)
- ✅ Identificação de outliers (método IQR)
- ✅ Análise de correlação (Pearson)
- ✅ Erro amostral e intervalos de confiança (95%)
- ✅ Regressão linear múltipla (OLS)
- ✅ Análise de volatilidade

### Variáveis do Estudo

| Variável | Tipo | Fonte | Descrição |
|----------|------|-------|-----------|
| Retorno S&P 500 | Dependente | ^GSPC | Retorno logarítmico diário |
| Big Tech Index | Independente | AAPL+MSFT+GOOGL+AMZN+NVDA+TSLA+META | Índice ponderado por market cap |
| VIX | Dependente | ^VIX | Índice de volatilidade implícita |
| Taxa Juros 10Y | Controle | ^TNX | Yield do Tesouro Americano |

---

## 💡 Principais Conclusões

### ✅ Questão de Pesquisa Respondida

**"Qual a influência do desempenho e da concentração das Magnificent Seven sobre a volatilidade e o retorno do S&P 500?"**

**Resposta:** As Magnificent Seven exercem **influência substancial e estatisticamente significativa** tanto sobre o retorno (R² = 75.54%) quanto sobre a volatilidade do S&P 500. A forte correlação (0.8691) demonstra que essas empresas são **fatores determinantes** da trajetória do índice.

### 📌 Achados Principais

1. **Concentração elevada:** O setor tech exerce influência desproporcional sobre o índice
2. **Risco sistêmico:** Dependência do S&P 500 cria vulnerabilidade estrutural
3. **Efeito estabilizador:** Bom desempenho das big techs reduz volatilidade do mercado
4. **Diversificação limitada:** Fundos indexados têm exposição indireta concentrada
5. **Significância estatística:** Todos os modelos são altamente significativos (p < 0.001)

---

## 🎓 Contribuições

### Acadêmicas
- Quantificação empírica da influência do setor tech no período recente
- Metodologia replicável para outros setores/períodos
- Análise multidimensional (retorno + volatilidade + macro)

### Práticas
- Insights para gestão de portfólio e alocação de ativos
- Avaliação de risco de concentração em fundos passivos
- Identificação de setor-chave para monitoramento de mercado

---

## ⚠️ Limitações

- Período de 3 anos (alta volatilidade pós-pandemia)
- Simplificação da capitalização de mercado (preços como proxy)
- Não estabelece causalidade definitiva
- Variáveis omitidas (política monetária, eventos geopolíticos)
- Coeficientes podem não ser estáveis ao longo do tempo

---

## 🔬 Pesquisas Futuras

1. **Janelas temporais:** Análise em diferentes ciclos econômicos (rolling regressions)
2. **Comparação internacional:** Replicar para mercados europeus e asiáticos
3. **Quebras estruturais:** Testes de Chow e Markov-switching
4. **Contágio financeiro:** Modelos DCC-GARCH e Copulas
5. **Análise desagregada:** Influência individual de cada empresa
6. **Machine Learning:** Previsão com Random Forest, XGBoost, Redes Neurais
7. **Sentiment analysis:** Incorporar dados de redes sociais e notícias
8. **Implicações regulatórias:** Estudos sobre antitruste e estabilidade

---

## 📥 Download e Exportação

O dashboard permite download de:

- ✅ Todos os datasets em CSV
- ✅ Resultados das regressões
- ✅ Estatísticas descritivas
- ✅ Matriz de correlação
- ✅ Dados sem outliers

---

## 📝 Licença

Este projeto é de uso **acadêmico**. Código aberto para fins educacionais.

---

## 👤 Autor

**Iago Santos Azevedo**

- GitHub: [@iago-azevedo-py](https://github.com/iago-azevedo-py)
- Repositório: [Analise-Magnifique-Seven](https://github.com/iago-azevedo-py/Analise-Magnifique-Seven)

---

## 🙏 Agradecimentos

- **Yahoo Finance** pela disponibilização de dados financeiros via API
- **CBOE** pelos dados históricos do VIX
- **U.S. Treasury** pelas taxas de juros
- **Streamlit** pela framework de dashboard interativo

---

<div align="center">

**📊 Trabalho Acadêmico - Métodos Quantitativos Aplicados à Administração**

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!

</div>
