# 🚀 GUIA RÁPIDO DE USO

## ⚡ Início Rápido (1 Comando)

```bash
python iniciar_projeto.py
```

**Pronto!** O script irá:
1. ✅ Verificar/coletar dados
2. ✅ Iniciar dashboard
3. ✅ Abrir em http://localhost:8501

---

## 📋 Três Formas de Usar

### 1️⃣ Forma Automática (Recomendado)
```bash
python iniciar_projeto.py
```

### 2️⃣ Forma Manual
```bash
# Passo 1: Coletar dados
python coletar_dados.py

# Passo 2: Abrir dashboard
streamlit run app.py
```

### 3️⃣ Apenas Dashboard (se dados já existem)
```bash
streamlit run app.py
```

---

## 🎯 O Que Você Verá

### Dashboard com 9 Seções:

1. **🏠 Início** - Visão geral e métricas
2. **📄 Resumo** - Resumo executivo
3. **📖 Introdução** - Contexto e problema
4. **📚 Referencial** - Base teórica
5. **🔬 Metodologia** - Métodos usados
6. **📊 Dados** - Visualizações interativas ⭐
7. **📈 Estatísticas** - Análises completas ⭐
8. **📋 Quadros** - Tabelas do trabalho
9. **📚 Referências** - Bibliografia

---

## 📊 Dados Disponíveis

### Arquivos CSV Gerados:
- `dados_precos.csv` - Preços diários
- `dados_retornos.csv` - Retornos logarítmicos
- `dados_pesos_bigtech.csv` - Composição do índice

### Período:
- **Início:** 01/01/2022
- **Fim:** 31/12/2024
- **Total:** 752 dias de negociação

---

## 🔍 Principais Achados

```
📈 Correlação S&P 500 vs Big Tech: 0.8691 (86.9%)
💰 Retorno Anual S&P 500: ~7.0%
🚀 Retorno Anual Big Tech: ~15.5%
📊 Volatilidade S&P 500: ~17.5%
⚡ Volatilidade Big Tech: ~31.2%
📉 Correlação VIX vs Retornos: -0.19 (negativa)
```

---

## 🛑 Encerrando

Para parar o servidor Streamlit:
```
Ctrl + C
```

---

## 💡 Dicas

- ✨ Navegue pelas seções usando a **sidebar**
- 📊 Interaja com os gráficos (zoom, hover, etc)
- 💾 Faça download dos dados via botão no dashboard
- 🔄 Recarregue dados usando `python coletar_dados.py`

---

## ⚠️ Problemas?

### Dashboard não abre?
```bash
# Verificar porta 8501
streamlit run app.py --server.port 8502
```

### Erro ao coletar dados?
- Verificar conexão internet
- Aguardar alguns minutos e tentar novamente
- Yahoo Finance pode ter limites de requisição

### Gráficos não aparecem?
```bash
pip install --upgrade plotly streamlit
```

---

## 📞 Arquivos Importantes

| Arquivo | Descrição |
|---------|-----------|
| `app.py` | Dashboard principal |
| `coletar_dados.py` | Coleta de dados |
| `iniciar_projeto.py` | Script all-in-one |
| `README.md` | Documentação completa |
| `RESUMO_PROJETO.md` | Resumo detalhado |

---

**🎓 Projeto Acadêmico - Magnificent Seven & S&P 500**  
**📊 Dashboard Interativo com Análise de Dados Reais**

✨ **Acesse:** http://localhost:8501
