# 🚀 Guia Rápido de Uso

## ⚡ Opção 1: Visualização Imediata (Recomendada para primeiros acessos)

O dashboard já vem com **dados pré-processados** incluídos no repositório. Você pode visualizar todas as análises imediatamente:

```bash
# 1. Clone o repositório
git clone https://github.com/iago-azevedo-py/Analise-Magnifique-Seven.git
cd Analise-Magnifique-Seven

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o dashboard
streamlit run app.py
```

✅ O dashboard abrirá em `http://localhost:8501` com **todos os dados e análises prontos**!

## 🔄 Opção 2: Atualizar Dados (Para dados mais recentes)

Se quiser coletar dados atualizados do Yahoo Finance:

```bash
# 1. Coletar novos dados (pode demorar alguns minutos)
python coletar_dados.py

# 2. Executar análises estatísticas
python analises_estatisticas.py

# 3. Visualizar no dashboard
streamlit run app.py
```

## 📊 Dados Incluídos no Repositório

O repositório já contém:

- ✅ **dados_final.csv** - Dataset principal (751 observações, 2022-2024)
- ✅ **estatisticas_descritivas.csv** - Estatísticas completas
- ✅ **matriz_correlacao.csv** - Correlações entre variáveis
- ✅ **regressao_multipla.csv** - Resultados dos modelos
- ✅ **scatter_modelo1.html** - Gráfico de regressão S&P 500
- ✅ **scatter_modelo2.html** - Gráfico de regressão VIX
- ✅ **heatmap_correlacao.html** - Heatmap interativo
- ✅ **boxplots_outliers.html** - Visualização de outliers

## 🎯 Navegação no Dashboard

O dashboard possui 11 seções:

1. **🏠 Início** - Apresentação do trabalho
2. **📄 Resumo** - Resumo executivo
3. **📖 Introdução** - Contexto e objetivos
4. **📚 Referencial Teórico** - Base teórica
5. **🔬 Metodologia** - Métodos utilizados
6. **📊 Dados Coletados** - Visualização de dados
7. **📈 Análise Estatística** - Estatísticas descritivas
8. **🔮 Regressão Linear** - Modelos econométricos
9. **📋 Quadros** - Tabelas e definições
10. **🎯 Conclusão** - Síntese e considerações finais
11. **📚 Referências** - Bibliografia

## 💡 Dicas

- Use a barra lateral para navegar entre as seções
- Todos os gráficos são **interativos** (zoom, hover, pan)
- Você pode **baixar os dados em CSV** nas seções de análise
- O cache do Streamlit torna o carregamento muito rápido

## 🛠️ Tecnologias

- Python 3.13+
- Streamlit
- pandas, numpy
- plotly
- yfinance
- statsmodels

## 📧 Suporte

Problemas ou dúvidas? Abra uma issue no GitHub!

---

**🎓 Trabalho Acadêmico - Métodos Quantitativos Aplicados à Administração**
