import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from io import StringIO
import google.generativeai as genai

# Funções de cache para otimização
@st.cache_data
def carregar_dados_csv(caminho):
    """Carrega dados CSV com cache"""
    if os.path.exists(caminho):
        return pd.read_csv(caminho, index_col=0, parse_dates=True)
    return None

@st.cache_data
def carregar_html(caminho):
    """Carrega arquivo HTML com cache"""
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def formatar_numero_br(valor, casas=2):
    """Formata número para padrão brasileiro (vírgula como decimal)"""
    if pd.isna(valor):
        return "N/A"
    formato = f"{{:,.{casas}f}}"
    return formato.format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def converter_df_para_csv(df):
    """Converte DataFrame para CSV para download"""
    return df.to_csv(index=True).encode('utf-8')

# Configuração da página
st.set_page_config(
    page_title="Magnificent Seven & S&P 500",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .author {
        text-align: center;
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .highlight-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .reference-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    .keyword {
        display: inline-block;
        background-color: #1f77b4;
        color: white;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 15px;
        font-size: 0.85rem;
    }
    .section-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar para navegação
st.sidebar.title("📑 Navegação")
st.sidebar.markdown("---")

secao = st.sidebar.radio(
    "Selecione a seção:",
    ["🏠 Início", "📄 Resumo", "📖 Introdução", "📚 Referencial Teórico", 
     "🔬 Metodologia", "📊 Dados Coletados", "📈 Análise Estatística", 
     "🔮 Regressão Linear", "🤖 Assistente IA", "🎯 Conclusão", "📚 Referências"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
    **Sobre este trabalho:**
    
    Trabalho acadêmico desenvolvido para a disciplina de Métodos Quantitativos 
    Aplicados à Administração.
    
    **Autor:** Iago Santos Azevedo
    
    **Período de análise:** Janeiro/2022 - Dezembro/2024
""")

# Conteúdo principal baseado na seleção
if secao == "🏠 Início":
    st.markdown('<div class="main-header">A INFLUÊNCIA DO DESEMPENHO E CONCENTRAÇÃO DO SETOR DE TECNOLOGIA (MAGNIFICENT SEVEN) SOBRE A VOLATILIDADE E O RETORNO DO S&P 500</div>', unsafe_allow_html=True)
    st.markdown('<div class="author">Iago Santos Azevedo</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📅 Período de Análise", "2022-2024")
    with col2:
        st.metric("🏢 Empresas Analisadas", "7")
    with col3:
        st.metric("📈 Índices", "S&P 500 + VIX")
    
    st.markdown("---")
    
    st.markdown("""
    <div class="section-card">
        <h3>🎯 Objetivo do Estudo</h3>
        <p style="font-size: 1.1rem; line-height: 1.8;">
        Este trabalho acadêmico analisa empiricamente a influência das maiores empresas de tecnologia, 
        conhecidas como <strong>"Magnificent Seven"</strong>, sobre o retorno e a volatilidade do 
        índice de mercado S&P 500.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
        <h3>🏢 As Magnificent Seven</h3>
        <p style="font-size: 1.1rem;">
        O grupo é composto pelas seguintes empresas:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 🍎 **Apple**
        - 🪟 **Microsoft**
        - 🔍 **Alphabet (Google)**
        - 📦 **Amazon**
        """)
    with col2:
        st.markdown("""
        - 🎮 **Nvidia**
        - 🚗 **Tesla**
        - 📱 **Meta Platforms (Facebook)**
        """)
    
    st.markdown("""
    <div class="section-card">
        <h3>🔍 Metodologia</h3>
        <p style="font-size: 1.1rem; line-height: 1.8;">
        A pesquisa utiliza técnicas de <strong>correlação</strong> e <strong>regressão linear múltipla</strong> 
        para examinar a relação entre o desempenho das Big Tech e o comportamento do mercado mais amplo, 
        controlando pela taxa de juros de 10 anos do tesouro americano.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif secao == "📄 Resumo":
    st.markdown('<div class="sub-header">📄 Resumo</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O presente estudo tem como objetivo principal analisar empiricamente a influência do desempenho 
    das maiores empresas de tecnologia, conhecidas como as <strong>"Magnificent Seven"</strong>, sobre o retorno 
    e a volatilidade do índice de mercado S&P 500. A pesquisa, de natureza quantitativa e descritiva, 
    utiliza dados de séries temporais diárias no período de <strong>janeiro de 2022 a dezembro de 2024</strong>. 
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A metodologia empregada envolve a aplicação de técnicas de <strong>correlação</strong> e 
    <strong>regressão linear múltipla</strong> para examinar a relação entre o retorno diário ponderado 
    de um índice representativo das Big Tech (variável independente principal), a taxa de juros de 10 anos 
    do tesouro americano (variável de controle), e as variáveis dependentes: o retorno diário do S&P 500 
    e o índice de volatilidade VIX.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O contexto da análise se insere na crescente concentração do mercado de ações americano no setor de 
    tecnologia, levantando questões sobre <strong>risco sistêmico</strong> e <strong>diversificação</strong>. 
    Os resultados esperados apontam para a existência de uma relação estatisticamente significativa e 
    positiva entre o desempenho do setor de tecnologia e o comportamento do S&P 500, sugerindo que o 
    "Big Tech Index" funciona como um importante preditor tanto do retorno quanto da volatilidade do 
    mercado mais amplo.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Tais achados podem oferecer subsídios para estratégias de <strong>gestão de portfólio</strong> e 
    <strong>análise de risco</strong>.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏷️ Palavras-chave")
    st.markdown("""
    <div>
        <span class="keyword">Séries Temporais</span>
        <span class="keyword">Risco Sistêmico</span>
        <span class="keyword">S&P 500</span>
        <span class="keyword">Magnificent Seven</span>
        <span class="keyword">Volatilidade</span>
        <span class="keyword">VIX</span>
        <span class="keyword">Mercado de Capitais</span>
    </div>
    """, unsafe_allow_html=True)

elif secao == "📖 Introdução":
    st.markdown('<div class="sub-header">1. Introdução</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O mercado de capitais norte-americano, representado proeminentemente pelo índice S&P 500, 
    tem passado por uma <strong>transformação estrutural notável</strong> nas últimas décadas. Uma característica 
    marcante desse processo é a crescente concentração de valor de mercado em um número restrito de 
    empresas do setor de tecnologia.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Este grupo, recentemente apelidado de <strong>"Magnificent Seven"</strong>, composto por gigantes como 
    Apple, Microsoft, Alphabet, Amazon, Nvidia, Tesla e Meta Platforms, alcançou uma representatividade 
    sem precedentes no índice, exercendo uma influência desproporcional sobre seus movimentos diários.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    📌 **Nota importante:** Conforme apontado por diversos analistas (SILVA; COSTA, 2023), 
    essa concentração eleva a preocupação com o **risco sistêmico**, uma vez que o desempenho 
    de um único setor passa a ter o potencial de determinar a direção do mercado como um todo.
    """)
    
    st.markdown("""
    <div class="section-card">
    <h4>🎯 Relevância do Tema</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A relevância deste tema reside na necessidade de compreender a dinâmica atual do mercado para fins de:
    </p>
    <ul style="font-size: 1.05rem; line-height: 1.9;">
        <li><strong>Alocação de ativos</strong></li>
        <li><strong>Gestão de risco</strong></li>
        <li><strong>Formulação de estratégias de investimento</strong></li>
    </ul>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Se uma parcela significativa do retorno e da volatilidade do principal índice de referência global 
    pode ser explicada pelo comportamento de um pequeno grupo de empresas, os modelos tradicionais de 
    diversificação de portfólio podem necessitar de revisão.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>❓ Questão de Pesquisa</h4>
    <p style="font-size: 1.15rem; font-weight: 600; color: #1f77b4;">
    Qual é a influência estatística do desempenho das "Magnificent Seven" sobre o retorno e 
    a volatilidade do S&P 500?
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h4>🎯 Objetivo Geral</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Analisar quantitativamente a relação entre o desempenho diário de um índice ponderado das 
    empresas de Big Tech e as flutuações do S&P 500 e de seu índice de volatilidade (VIX).
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h4>💡 Hipótese Central</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O desempenho do setor de tecnologia, representado pelo <strong>"Big Tech Index"</strong>, é um preditor 
    estatisticamente significativo tanto do retorno diário quanto da volatilidade implícita do S&P 500, 
    mesmo após o controle por variáveis macroeconômicas relevantes, como a taxa de juros.
    </p>
    </div>
    """, unsafe_allow_html=True)

elif secao == "📚 Referencial Teórico":
    st.markdown('<div class="sub-header">2. Referencial Teórico</div>', unsafe_allow_html=True)
    
    # Seção 2.1
    st.markdown("### 2.1 O Mercado Americano (S&P 500) e a Concentração Setorial")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O <strong>Standard & Poor's 500 (S&P 500)</strong> é amplamente reconhecido como um dos principais 
    termômetros da saúde da economia norte-americana e um benchmark para investidores em todo o mundo. 
    O índice abrange as 500 maiores empresas de capital aberto dos Estados Unidos, ponderadas por seu 
    valor de mercado.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Historicamente, sua composição refletia uma economia diversificada, com pesos distribuídos entre 
    setores como financeiro, industrial, saúde e consumo. <strong>Contudo, a ascensão da economia digital 
    alterou drasticamente esse panorama.</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("""
    ⚠️ **Atenção:** Estudos recentes demonstram que o peso combinado das principais empresas de 
    tecnologia no S&P 500 atingiu níveis recordes, **superando a concentração observada durante 
    a bolha das empresas ".com" no final dos anos 1990** (JONES, 2022).
    """)
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Essa dominância não é apenas uma questão de valor de mercado, mas também de influência sobre:
    </p>
    <ul style="font-size: 1.05rem; line-height: 1.9;">
        <li>🔬 A inovação</li>
        <li>👥 O comportamento do consumidor</li>
        <li>🌐 As cadeias produtivas globais</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    💡 **Insight:** A capitalização de mercado das 'Magnificent Seven' tornou-se tão vasta que 
    seus resultados trimestrais e suas projeções de crescimento são capazes de gerar ondas de 
    otimismo ou pessimismo que se propagam por todo o sistema financeiro (PEREIRA, 2023).
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Essa dinâmica sugere que <strong>a análise do índice geral não pode mais ser dissociada de uma 
    análise aprofundada de seu componente tecnológico.</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção 2.2
    st.markdown("---")
    st.markdown("### 2.2 Risco e Retorno em Mercados de Ações")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A teoria moderna de finanças é fundamentada na relação entre <strong>risco e retorno</strong>. 
    O retorno de um ativo, como uma ação ou um índice de mercado, é a medida de seu ganho ou perda 
    em um determinado período.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h4>📊 Cálculo do Retorno</h4>
    <p style="font-size: 1.05rem; line-height: 1.9;">
    Para este estudo, o retorno diário do S&P 500 será calculado como a variação percentual 
    logarítmica de seu valor de fechamento:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"R_t = \ln(P_t / P_{t-1})")
    
    st.markdown("""
    <p style="font-size: 0.95rem; color: #666; text-align: center;">
    onde $P_t$ é o preço no dia $t$
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h4>📉 O Índice VIX - "Índice do Medo"</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O risco é frequentemente associado à incerteza ou à variabilidade dos retornos. Uma de suas 
    medidas mais proeminentes no mercado atual é o <strong>Índice de Volatilidade CBOE (VIX)</strong>.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O VIX, popularmente conhecido como o <strong>"índice do medo"</strong>, mede a volatilidade implícita 
    de curto prazo das opções do S&P 500. Ele não mede a volatilidade histórica, mas sim a 
    expectativa do mercado quanto à volatilidade nos próximos 30 dias.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    📌 **Segundo Fernandes (2021):** O VIX é um indicador prospectivo do sentimento de risco do 
    investidor; **picos no VIX geralmente coincidem com períodos de estresse e quedas acentuadas 
    no mercado de ações.**
    """)
    
    st.success("""
    ✅ **Importância para o estudo:** Utilizá-lo como uma das variáveis dependentes permite 
    capturar a percepção de risco do mercado, um complemento essencial à análise do retorno.
    """)
    
    # Seção 2.3
    st.markdown("---")
    st.markdown("### 2.3 Big Tech como Fator Sistêmico")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A noção de <strong>risco sistêmico</strong> refere-se ao risco de colapso de um sistema inteiro, 
    em oposição ao risco associado a uma entidade ou componente individual.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Tradicionalmente, o debate sobre risco sistêmico no mercado financeiro focava-se em grandes 
    instituições bancárias (<em>"too big to fail"</em>). No entanto, a crescente interconexão e o peso 
    econômico das grandes empresas de tecnologia levaram à discussão sobre se elas próprias não 
    constituiriam uma <strong>nova fonte de risco sistêmico</strong>.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🚀 Fatores Impulsionadores</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    O desempenho do grupo "Magnificent Seven" é impulsionado por fatores como:
    </p>
    <ul style="font-size: 1.05rem; line-height: 1.9;">
        <li><strong>Inovação disruptiva</strong></li>
        <li><strong>Efeitos de rede</strong></li>
        <li><strong>Economias de escala</strong></li>
    </ul>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Estes podem não estar perfeitamente correlacionados com os ciclos econômicos tradicionais.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Argumenta-se que o otimismo em torno de temas como <strong>inteligência artificial</strong>, 
    <strong>computação em nuvem</strong> e <strong>transformação digital</strong> cria um 
    <em>"fator Big Tech"</em> específico que influencia o sentimento geral do mercado 
    (WILLIAMS; BROWN, 2024).
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Por essa razão, o desempenho agregado desse grupo de empresas deve ser tratado não apenas 
    como parte do mercado, mas como uma <strong>variável explicativa crucial</strong> para o 
    comportamento do próprio mercado.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quadro Teórico
    st.markdown("---")
    st.markdown("### 📐 Quadro Teórico da Pesquisa")
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: center;">
    <strong>Quadro 1 - Síntese da Fundamentação Teórica e Operacionalização das Variáveis</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabela 1: Fundamentação Teórica
    st.markdown("""
    <div class="section-card">
    <h4 style="text-align: center; margin-bottom: 20px;">Tabela 1 - Fundamentação Teórica da Pesquisa</h4>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
        <thead style="background-color: #667eea; color: white;">
            <tr>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 25%;">Teoria/Modelo</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 20%;">Autor(es) e Ano</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 35%;">Contribuição Teórica</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 20%;">Aplicação no Estudo</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Teoria Moderna de Portfólio</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Markowitz (1952)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Estabelece a relação risco-retorno como fundamento da decisão de investimento. Diversificação reduz o risco não-sistemático.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Justifica a análise da concentração setorial como fator de risco.</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Hipótese dos Mercados Eficientes (HME)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Fama (1970)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Preços dos ativos refletem toda informação disponível. Concentração pode criar ineficiências informacionais.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Fundamenta a investigação da influência desproporcional da Big Tech.</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Teoria do Risco Sistêmico</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Allen & Gale (2000)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Interconexão entre entidades pode gerar efeito cascata no sistema financeiro ("too big to fail").</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Analisa se Magnificent Seven constituem risco sistêmico para o S&P 500.</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Finanças Comportamentais</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Kahneman & Tversky (1979)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Sentimento e vieses cognitivos dos investidores influenciam a precificação de ativos.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Explica o VIX como proxy do sentimento de medo e aversão ao risco.</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Modelo de Regressão Linear (OLS)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Gauss-Markov (Teorema)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Método dos Mínimos Quadrados Ordinários para estimação de relações lineares entre variáveis.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Técnica econométrica utilizada para testar as hipóteses da pesquisa.</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabela 2: Operacionalização das Variáveis
    st.markdown("""
    <div class="section-card">
    <h4 style="text-align: center; margin-bottom: 20px;">Tabela 2 - Operacionalização das Variáveis da Pesquisa</h4>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
        <thead style="background-color: #667eea; color: white;">
            <tr>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Variável</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Tipo</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 25%;">Definição Conceitual</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 20%;">Definição Operacional</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Fonte de Dados</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: center; width: 10%;">Período</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Retorno S&P 500</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Dependente</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Variação percentual do índice S&P 500 que representa o desempenho do mercado acionário americano.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">R<sub>t</sub> = ln(P<sub>t</sub> / P<sub>t-1</sub>)<br>Retorno logarítmico diário</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance (Ticker: ^GSPC)</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>(752 dias)</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>VIX</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Dependente</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Índice de volatilidade implícita que mede a expectativa de volatilidade do mercado nos próximos 30 dias.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Valor diário do índice CBOE VIX em pontos percentuais</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance (Ticker: ^VIX)</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>(752 dias)</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Retorno Big Tech</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Independente</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Retorno agregado das Magnificent Seven (AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META).</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Média ponderada igualmente dos retornos logarítmicos diários das 7 empresas</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance (Tickers individuais)</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>(752 dias)</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Taxa de Juros 10Y</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Controle</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Rendimento dos títulos do Tesouro americano de 10 anos, representando a taxa livre de risco.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Taxa percentual anual (yield) diária dos Treasury Notes</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance (Ticker: ^TNX)</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>(752 dias)</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabela 3: Hipóteses da Pesquisa
    st.markdown("""
    <div class="section-card">
    <h4 style="text-align: center; margin-bottom: 20px;">Tabela 3 - Hipóteses da Pesquisa e Resultados Esperados</h4>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
        <thead style="background-color: #667eea; color: white;">
            <tr>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: center; width: 10%;">Hipótese</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 35%;">Descrição</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 25%;">Fundamentação Teórica</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Resultado Esperado</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Método de Teste</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>H₁</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">O retorno das Magnificent Seven apresenta correlação positiva forte com o retorno do S&P 500.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Teoria Moderna de Portfólio: concentração setorial influencia índice ponderado.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">ρ > 0.70<br>p < 0.001</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Coeficiente de Correlação de Pearson</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>H₂</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">O retorno da Big Tech explica significativamente a variação do retorno do S&P 500.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">HME e Risco Sistêmico: peso econômico gera influência desproporcional.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">R² > 60%<br>β₁ > 0<br>p < 0.001</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Regressão Linear Múltipla (OLS)</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>H₃</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">O retorno da Big Tech apresenta relação inversa com a volatilidade do mercado (VIX).</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Finanças Comportamentais: bom desempenho reduz percepção de risco.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">β₁ < 0<br>p < 0.05</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Regressão Linear Múltipla (OLS)</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>H₄</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">A volatilidade da Big Tech é superior à volatilidade do S&P 500.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Teoria do Risco: inovação disruptiva gera maior variabilidade de retornos.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">σ<sub>BigTech</sub> > σ<sub>S&P500</sub></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Desvio Padrão Anualizado</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Modelo Conceitual Visual
    st.markdown("---")
    st.markdown("### 🎯 Modelo Conceitual da Pesquisa")
    
    st.markdown("""
    <div class="highlight-box">
    <h4 style="text-align: center;">Relações entre Variáveis</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Criar diagrama textual
    col_a, col_b, col_c = st.columns([1, 2, 1])
    
    with col_b:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 10px; border: 2px solid #667eea;">
        
        <div style="text-align: center; margin-bottom: 20px;">
        <div style="display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
        color: white; border-radius: 10px; font-size: 1.1rem; font-weight: bold;">
        🚀 MAGNIFICENT SEVEN<br>(Variável Independente Principal)
        </div>
        </div>
        
        <div style="text-align: center; margin: 20px 0;">
        <div style="font-size: 2rem; color: #667eea;">⬇️</div>
        <div style="color: #666; font-size: 0.9rem; font-style: italic;">Influência Positiva Esperada</div>
        </div>
        
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        
        <div style="flex: 1; margin: 0 10px;">
        <div style="padding: 15px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
        color: white; border-radius: 10px; text-align: center; font-weight: bold;">
        📈 RETORNO S&P 500<br>(Variável Dependente 1)
        </div>
        <div style="text-align: center; margin-top: 10px; font-size: 0.85rem; color: #666;">
        Modelo 1: OLS<br>R² esperado > 60%
        </div>
        </div>
        
        <div style="flex: 1; margin: 0 10px;">
        <div style="padding: 15px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
        color: white; border-radius: 10px; text-align: center; font-weight: bold;">
        📉 VOLATILIDADE (VIX)<br>(Variável Dependente 2)
        </div>
        <div style="text-align: center; margin-top: 10px; font-size: 0.85rem; color: #666;">
        Modelo 2: OLS<br>β₁ esperado < 0
        </div>
        </div>
        
        </div>
        
        <div style="text-align: center; margin-top: 30px; padding: 15px; background: #f8f9fa; border-radius: 10px;">
        <div style="font-weight: bold; color: #333; margin-bottom: 10px;">VARIÁVEIS DE CONTROLE</div>
        <div style="font-size: 0.9rem; color: #666;">
        💵 Taxa de Juros 10Y &nbsp;|&nbsp; 📊 Tendência Temporal
        </div>
        </div>
        
        </div>
        """, unsafe_allow_html=True)
    
    # Resumo do Quadro Teórico
    st.markdown("---")
    st.markdown("""
    <div class="section-card">
    <h4>📋 Resumo: Estrutura Teórico-Metodológica</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    Este quadro teórico integra a <strong>Teoria Moderna de Portfólio</strong>, 
    <strong>Hipótese dos Mercados Eficientes</strong>, <strong>Teoria do Risco Sistêmico</strong> 
    e <strong>Finanças Comportamentais</strong> para fundamentar a investigação empírica da 
    influência das Magnificent Seven sobre o S&P 500.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A metodologia quantitativa, baseada em <strong>modelos de regressão linear (OLS)</strong>, 
    permite testar as hipóteses formuladas e quantificar o impacto das Big Tech sobre o 
    retorno e a volatilidade do mercado americano no período 2022-2024.
    </p>
    </div>
    """, unsafe_allow_html=True)

elif secao == "🔬 Metodologia":
    st.markdown('<div class="sub-header">3. Metodologia</div>', unsafe_allow_html=True)
    
    # Seção 3.1
    st.markdown("### 3.1 Tipo de Pesquisa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h4>📋 Caracterização</h4>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        O presente estudo caracteriza-se como uma <strong>pesquisa descritiva com abordagem quantitativa</strong>.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h4>🎯 Objetivo</h4>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        Observar, registrar e analisar as características e a relação entre as variáveis sem manipulá-las.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>📊 Abordagem Quantitativa</h4>
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A abordagem é quantitativa, pois se baseia na coleta e análise de dados numéricos e na aplicação 
    de modelos estatísticos para testar a hipótese formulada. Especificamente, a pesquisa emprega a 
    técnica de <strong>análise de séries temporais</strong>, que é apropriada para estudar a evolução 
    de variáveis ao longo do tempo e identificar padrões de dependência temporal e causalidade.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção 3.2
    st.markdown("---")
    st.markdown("### 3.2 Instrumento de Coleta")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9; text-align: justify;">
    A coleta de dados será realizada de forma <strong>automatizada</strong> por meio de um script 
    desenvolvido na linguagem de programação <strong>Python</strong>.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h4>🛠️ Ferramentas Utilizadas</h4>
    <ul style="font-size: 1.05rem; line-height: 1.9;">
        <li><strong>yfinance:</strong> Para extração de dados de mercado</li>
        <li><strong>pandas-datareader:</strong> Para dados econômicos (FRED)</li>
        <li><strong>Yahoo Finance API:</strong> Fonte de dados de preços</li>
        <li><strong>Federal Reserve Economic Data (FRED):</strong> Dados macroeconômicos</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Quadro de Variáveis da Pesquisa
    st.markdown("---")
    st.markdown("#### 📋 Quadro de Variáveis da Pesquisa")
    
    st.markdown("""
    <div class="section-card">
    <h4 style="text-align: center; margin-bottom: 20px;">Quadro 2 - Identificação e Caracterização das Variáveis</h4>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
        <thead style="background-color: #667eea; color: white;">
            <tr>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 5%;">Cód.</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 18%;">Variável</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 10%;">Tipo</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 15%;">Fonte/Ticker</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 12%;">Unidade de Medida</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: left; width: 25%;">Descrição/Cálculo</th>
                <th style="padding: 12px; border: 1px solid #ddd; text-align: center; width: 15%;">Período/Frequência</th>
            </tr>
        </thead>
        <tbody>
            <!-- Variáveis Dependentes -->
            <tr style="background-color: #e8eaf6;">
                <td colspan="7" style="padding: 8px; border: 1px solid #ddd; font-weight: bold; background-color: #5c6bc0; color: white;">
                    VARIÁVEIS DEPENDENTES
                </td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>Y₁</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Retorno S&P 500</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Dependente<br>(Contínua)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance<br>^GSPC</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Percentual (%)<br>logarítmico</td>
                <td style="padding: 10px; border: 1px solid #ddd;">R<sub>t</sub> = ln(P<sub>t</sub> / P<sub>t-1</sub>)<br>
                    Variação diária do índice S&P 500</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>Diária<br>(752 obs.)</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>Y₂</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Índice VIX</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Dependente<br>(Contínua)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance<br>^VIX</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Pontos<br>percentuais</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Volatilidade implícita de 30 dias<br>
                    ("Índice do Medo")</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>Diária<br>(752 obs.)</td>
            </tr>
            
            <!-- Variável Independente Principal -->
            <tr style="background-color: #e8eaf6;">
                <td colspan="7" style="padding: 8px; border: 1px solid #ddd; font-weight: bold; background-color: #7e57c2; color: white;">
                    VARIÁVEL INDEPENDENTE PRINCIPAL
                </td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>X₁</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Retorno Big Tech<br>(Magnificent Seven)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Independente<br>(Contínua)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance<br>AAPL, MSFT, GOOGL,<br>AMZN, NVDA, TSLA, META</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Percentual (%)<br>logarítmico</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Média ponderada por capitalização<br>
                    dos retornos das 7 empresas</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>Diária<br>(752 obs.)</td>
            </tr>
            
            <!-- Variável de Controle -->
            <tr style="background-color: #e8eaf6;">
                <td colspan="7" style="padding: 8px; border: 1px solid #ddd; font-weight: bold; background-color: #9575cd; color: white;">
                    VARIÁVEL DE CONTROLE
                </td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>X₂</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Taxa de Juros<br>10 Anos (US)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Controle<br>(Contínua)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yahoo Finance<br>^TNX</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Percentual (% a.a.)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Yield dos Treasury Notes de 10 anos<br>
                    (Taxa livre de risco)</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">2022-2024<br>Diária<br>(752 obs.)</td>
            </tr>
            
            <!-- Componentes da Variável X₁ -->
            <tr style="background-color: #e8eaf6;">
                <td colspan="7" style="padding: 8px; border: 1px solid #ddd; font-weight: bold; background-color: #b39ddb; color: white;">
                    COMPONENTES DO BIG TECH INDEX (X₁)
                </td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₁</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Apple Inc.</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;" rowspan="7">Componentes<br>(Ação)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">AAPL</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;" rowspan="7">USD ($)<br>Preço/ação</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;" rowspan="7">Preços de fechamento ajustados<br>
                    para dividendos e desdobramentos</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;" rowspan="7">2022-2024<br>Diária<br>(752 obs.)</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₂</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Microsoft Corp.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">MSFT</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₃</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Alphabet Inc. (Google)</td>
                <td style="padding: 10px; border: 1px solid #ddd;">GOOGL</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₄</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Amazon.com Inc.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">AMZN</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₅</td>
                <td style="padding: 10px; border: 1px solid #ddd;">NVIDIA Corp.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">NVDA</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₆</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Tesla Inc.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">TSLA</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">C₇</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Meta Platforms Inc.</td>
                <td style="padding: 10px; border: 1px solid #ddd;">META</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card" style="margin-top: 15px;">
    <p style="font-size: 0.9rem; color: #666; text-align: justify;">
    <strong>Fonte:</strong> Elaborado pelo autor (2025).<br>
    <strong>Nota 1:</strong> Todas as séries possuem 752 observações diárias (dias úteis) no período de 01/01/2022 a 31/12/2024.<br>
    <strong>Nota 2:</strong> Os retornos logarítmicos resultam em 751 observações devido à diferenciação temporal.<br>
    <strong>Nota 3:</strong> O Big Tech Index (X₁) é calculado como média ponderada pela capitalização de mercado diária das 7 empresas.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📝 Procedimentos de Coleta")
    
    tab1, tab2, tab3 = st.tabs(["1️⃣ Extração", "2️⃣ Cálculo", "3️⃣ Ponderação"])
    
    with tab1:
        st.markdown("""
        <div class="section-card">
        <h4>Extração de Dados Brutos</h4>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        O script será programado para extrair as séries de dados diários para o período de 
        <strong>01 de janeiro de 2022 a 31 de dezembro de 2024</strong>.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        <strong>Dados coletados:</strong>
        </p>
        <ul style="font-size: 1.05rem; line-height: 1.9;">
            <li>Preços de fechamento ajustados para o S&P 500</li>
            <li>Preços de cada uma das sete empresas do "Magnificent Seven"</li>
            <li>Valor de fechamento do índice VIX</li>
            <li>Taxa de juros de 10 anos do tesouro americano</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="section-card">
        <h4>Cálculo de Retornos Logarítmicos</h4>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        Para todas as séries de preços de ativos (S&P 500 e ações individuais), serão calculados 
        os retornos diários logarítmicos, utilizando a fórmula:
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"R_t = \ln(P_t / P_{t-1})")
        
        st.markdown("""
        <p style="font-size: 0.95rem; color: #666;">
        onde $P_t$ é o preço no dia $t$
        </p>
        """, unsafe_allow_html=True)
        
        st.info("""
        💡 **Por que logarítmicos?** Esta abordagem é padrão em finanças por suas propriedades 
        estatísticas vantajosas.
        """)
    
    with tab3:
        st.markdown("""
        <div class="section-card">
        <h4>Ponderação do "Big Tech Index"</h4>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        Será construído um <strong>índice ponderado pelo valor de mercado</strong> para as 
        "Magnificent Seven" (Big Tech Index).
        </p>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        O peso de cada empresa no índice será <strong>recalculado diariamente</strong> com base em 
        sua capitalização de mercado no dia anterior, garantindo que o índice reflita a importância 
        relativa de cada empresa ao longo do tempo.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.9;">
        O retorno diário do Big Tech Index será a <strong>soma ponderada dos retornos individuais</strong>.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Seção 3.3
    st.markdown("---")
    st.markdown("### 3.3 Técnicas de Análise de Dados e Modelo Analítico")
    
    st.markdown("""
    <div class="section-card">
    <h4>📈 Análise de Séries Temporais</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h5>🔍 Testes de Estacionariedade</h5>
        <p style="font-size: 1rem; line-height: 1.8;">
        Será aplicado o <strong>teste de Dickey-Fuller Aumentado (ADF)</strong> a cada uma das 
        séries temporais para verificar a presença de raízes unitárias.
        </p>
        <p style="font-size: 1rem; line-height: 1.8;">
        Caso alguma série se mostre não estacionária, ela será diferenciada até que a 
        estacionariedade seja alcançada.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h5>📊 Análise de Correlação</h5>
        <p style="font-size: 1rem; line-height: 1.8;">
        Será calculada a <strong>matriz de correlação de Pearson</strong> entre todas as variáveis 
        para uma análise preliminar da direção e da força da associação linear entre elas.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🎯 Modelo Analítico</h4>
    <p style="font-size: 1.05rem; line-height: 1.9;">
    O <strong>modelo de regressão linear múltipla</strong> será utilizado para testar a hipótese central. 
    Serão estimados <strong>dois modelos separados</strong>, um para cada variável dependente:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h5>Modelo 1: Retorno S&P 500</h5>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"R_{SP500,t} = \beta_0 + \beta_1 R_{Tech,t} + \beta_2 Juros_{t} + \epsilon_t")
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h5>Modelo 2: Volatilidade (VIX)</h5>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"VIX_t = \beta_0 + \beta_1 R_{Tech,t} + \beta_2 Juros_{t} + \epsilon_t")
    
    st.markdown("""
    <div class="section-card">
    <h4>📖 Interpretação dos Parâmetros</h4>
    <ul style="font-size: 1rem; line-height: 1.8;">
        <li><strong>$t$:</strong> representa o dia</li>
        <li><strong>$\\beta_0$:</strong> é o intercepto (valor esperado da variável dependente quando as independentes são zero)</li>
        <li><strong>$\\beta_1$ e $\\beta_2$:</strong> são os coeficientes de regressão
            <ul>
                <li>$\\beta_1$ medirá o impacto do retorno do Big Tech Index</li>
                <li>$\\beta_2$ controlará pelo efeito da taxa de juros</li>
            </ul>
        </li>
        <li><strong>$\\epsilon_t$:</strong> é o termo de erro aleatório</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção 3.4
    st.markdown("---")
    st.markdown("### 3.4 Análise e Visualização de Dados")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.9;">
    A análise dos dados será conduzida integralmente em ambiente <strong>Python</strong>, com o auxílio das bibliotecas:
    </p>
    <ul style="font-size: 1.05rem; line-height: 1.9;">
        <li><strong>statsmodels:</strong> implementação dos modelos de regressão</li>
        <li><strong>scikit-learn:</strong> técnicas de machine learning e validação</li>
        <li><strong>Streamlit:</strong> desenvolvimento da aplicação web interativa</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>📊 Dashboard Interativo</h4>
    <p style="font-size: 1.05rem; line-height: 1.9;">
    Será desenvolvida uma <strong>aplicação web interativa (dashboard)</strong> utilizando a biblioteca 
    Streamlit. Esta aplicação permitirá a apresentação dinâmica dos gráficos e tabelas de resultados, incluindo:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h5>📈 Gráficos</h5>
        <ul style="font-size: 0.95rem;">
            <li>Séries temporais</li>
            <li>Dispersão</li>
            <li>Correlações</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h5>📊 Tabelas</h5>
        <ul style="font-size: 0.95rem;">
            <li>Coeficientes</li>
            <li>Erros padrão</li>
            <li>Valores-p</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="section-card">
        <h5>📉 Métricas</h5>
        <ul style="font-size: 0.95rem;">
            <li>R² ajustado</li>
            <li>Significância</li>
            <li>Diagnósticos</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.success("""
    ✅ **Objetivo:** A utilização do Streamlit visa criar uma interface intuitiva para a exploração 
    e apresentação final dos achados da pesquisa, facilitando a comunicação dos resultados de 
    forma clara e acessível.
    """)

elif secao == "📊 Dados Coletados":
    st.markdown('<div class="sub-header">📊 Dados Coletados e Processados</div>', unsafe_allow_html=True)
    
    # Verificar se os arquivos de dados existem
    caminho_retornos = os.path.join(os.path.dirname(__file__), 'dados_retornos.csv')
    caminho_precos = os.path.join(os.path.dirname(__file__), 'dados_precos.csv')
    caminho_pesos = os.path.join(os.path.dirname(__file__), 'dados_pesos_bigtech.csv')
    
    if os.path.exists(caminho_retornos) and os.path.exists(caminho_precos):
        
        try:
            # Carregar dados
            df_retornos = pd.read_csv(caminho_retornos, index_col=0, parse_dates=True)
            df_precos = pd.read_csv(caminho_precos, index_col=0, parse_dates=True)
            df_pesos = pd.read_csv(caminho_pesos, index_col=0, parse_dates=True)
            
            st.success(f"✅ Dados carregados com sucesso! Total de {len(df_retornos)} observações diárias")
            
            # Métricas principais
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📅 Período", f"{df_retornos.index.min().date()} a {df_retornos.index.max().date()}")
            with col2:
                st.metric("📊 Dias de Negociação", f"{len(df_retornos)}")
            with col3:
                retorno_medio_sp500 = df_retornos['Retorno_SP500'].mean() * 252 * 100
                st.metric("📈 Retorno Anual S&P 500", f"{retorno_medio_sp500:.2f}%")
            with col4:
                retorno_medio_bigtech = df_retornos['Retorno_BigTech_Index'].mean() * 252 * 100
                st.metric("🚀 Retorno Anual Big Tech", f"{retorno_medio_bigtech:.2f}%")
            
            st.markdown("---")
            
            # Tabs para diferentes visualizações
            tab1, tab2, tab3, tab4 = st.tabs(["📈 Séries Temporais", "📊 Retornos", "⚖️ Pesos Big Tech", "📋 Dados Brutos"])
            
            with tab1:
                st.markdown("### Evolução dos Preços (Base 100)")
                
                # Normalizar preços para base 100
                df_precos_norm = df_precos / df_precos.iloc[0] * 100
                
                fig = go.Figure()
                
                cores = {
                    'SP500': '#1f77b4',
                    'Apple': '#ff7f0e',
                    'Microsoft': '#2ca02c',
                    'Alphabet': '#d62728',
                    'Amazon': '#9467bd',
                    'Nvidia': '#8c564b',
                    'Tesla': '#e377c2',
                    'Meta': '#7f7f7f'
                }
                
                for col in ['SP500', 'Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Nvidia', 'Tesla', 'Meta']:
                    if col in df_precos_norm.columns:
                        fig.add_trace(go.Scatter(
                            x=df_precos_norm.index,
                            y=df_precos_norm[col],
                            name=col,
                            line=dict(color=cores.get(col, '#000000'), width=2)
                        ))
                
                fig.update_layout(
                    title='Evolução dos Preços das Magnificent Seven e S&P 500 (Base 100)',
                    xaxis_title='Data',
                    yaxis_title='Preço (Base 100)',
                    hovermode='x unified',
                    height=600
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Gráfico VIX e Taxa de Juros
                st.markdown("### Índice VIX e Taxa de Juros")
                
                fig2 = make_subplots(
                    rows=2, cols=1,
                    subplot_titles=('Índice VIX - Volatilidade Implícita', 'Taxa de Juros do Tesouro 10 Anos'),
                    vertical_spacing=0.12
                )
                
                fig2.add_trace(
                    go.Scatter(x=df_precos.index, y=df_precos['VIX'], 
                              name='VIX', line=dict(color='red', width=2)),
                    row=1, col=1
                )
                
                fig2.add_trace(
                    go.Scatter(x=df_precos.index, y=df_precos['Taxa_Juros_10Y'], 
                              name='Taxa 10Y', line=dict(color='blue', width=2)),
                    row=2, col=1
                )
                
                fig2.update_xaxes(title_text="Data", row=2, col=1)
                fig2.update_yaxes(title_text="VIX", row=1, col=1)
                fig2.update_yaxes(title_text="Taxa (%)", row=2, col=1)
                
                fig2.update_layout(height=600, showlegend=False, hovermode='x unified')
                
                st.plotly_chart(fig2, use_container_width=True)
            
            with tab2:
                st.markdown("### Distribuição dos Retornos Diários")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    fig_hist_sp500 = px.histogram(
                        df_retornos, x='Retorno_SP500',
                        title='Distribuição: Retorno S&P 500',
                        labels={'Retorno_SP500': 'Retorno Diário'},
                        color_discrete_sequence=['#1f77b4']
                    )
                    fig_hist_sp500.update_layout(height=400)
                    st.plotly_chart(fig_hist_sp500, use_container_width=True)
                
                with col2:
                    fig_hist_bigtech = px.histogram(
                        df_retornos, x='Retorno_BigTech_Index',
                        title='Distribuição: Retorno Big Tech Index',
                        labels={'Retorno_BigTech_Index': 'Retorno Diário'},
                        color_discrete_sequence=['#ff7f0e']
                    )
                    fig_hist_bigtech.update_layout(height=400)
                    st.plotly_chart(fig_hist_bigtech, use_container_width=True)
                
                st.markdown("### Comparação: S&P 500 vs Big Tech Index")
                
                fig_scatter = px.scatter(
                    df_retornos, 
                    x='Retorno_BigTech_Index', 
                    y='Retorno_SP500',
                    title='Relação entre Retornos: S&P 500 vs Big Tech Index',
                    labels={
                        'Retorno_BigTech_Index': 'Retorno Big Tech Index',
                        'Retorno_SP500': 'Retorno S&P 500'
                    },
                    trendline='ols',
                    color_discrete_sequence=['#1f77b4']
                )
                fig_scatter.update_layout(height=500)
                st.plotly_chart(fig_scatter, use_container_width=True)
                
                # Calcular correlação
                corr_sp500_bigtech = df_retornos['Retorno_SP500'].corr(df_retornos['Retorno_BigTech_Index'])
                st.info(f"📊 **Correlação entre S&P 500 e Big Tech Index:** {corr_sp500_bigtech:.4f}")
            
            with tab3:
                st.markdown("### Evolução dos Pesos no Big Tech Index")
                
                fig_pesos = go.Figure()
                
                for col in df_pesos.columns:
                    fig_pesos.add_trace(go.Scatter(
                        x=df_pesos.index,
                        y=df_pesos[col] * 100,
                        name=col,
                        stackgroup='one',
                        mode='none'
                    ))
                
                fig_pesos.update_layout(
                    title='Composição do Big Tech Index ao Longo do Tempo',
                    xaxis_title='Data',
                    yaxis_title='Peso no Índice (%)',
                    hovermode='x unified',
                    height=500
                )
                
                st.plotly_chart(fig_pesos, use_container_width=True)
                
                # Mostrar pesos médios
                st.markdown("### Pesos Médios no Período")
                pesos_medios = df_pesos.mean().sort_values(ascending=False) * 100
                
                fig_bar = px.bar(
                    x=pesos_medios.index,
                    y=pesos_medios.values,
                    labels={'x': 'Empresa', 'y': 'Peso Médio (%)'},
                    title='Peso Médio de Cada Empresa no Big Tech Index',
                    color=pesos_medios.values,
                    color_continuous_scale='Blues'
                )
                fig_bar.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig_bar, use_container_width=True)
            
            with tab4:
                st.markdown("### Dados de Retornos")
                st.dataframe(df_retornos.tail(20), use_container_width=True)
                
                st.markdown("### Dados de Preços")
                st.dataframe(df_precos.tail(20), use_container_width=True)
                
                # Botão para download
                csv_retornos = df_retornos.to_csv()
                st.download_button(
                    label="📥 Download Dados de Retornos (CSV)",
                    data=csv_retornos,
                    file_name='dados_retornos.csv',
                    mime='text/csv'
                )
            
        except Exception as e:
            st.error(f"❌ Erro ao carregar ou processar dados: {str(e)}")
            st.code(str(e), language='python')
            st.info("💡 Tente executar novamente: `python coletar_dados.py`")
    
    else:
        st.warning("⚠️ Dados ainda não coletados. Execute o script `coletar_dados.py` primeiro.")

elif secao == "📈 Análise Estatística":
    st.markdown('<div class="sub-header">📈 Análise Estatística</div>', unsafe_allow_html=True)
    
    caminho_retornos = os.path.join(os.path.dirname(__file__), 'dados_retornos.csv')
    
    if os.path.exists(caminho_retornos):
        try:
            df_retornos = pd.read_csv(caminho_retornos, index_col=0, parse_dates=True)
            colunas_analise = ['Retorno_SP500', 'Retorno_BigTech_Index', 'VIX', 'Taxa_Juros_10Y']
            
            # Criar abas
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📊 Estatísticas Descritivas", 
                "🔗 Correlações", 
                "📉 Volatilidade",
                "📦 Outliers",
                "💾 Download"
            ])
            
            # ABA 1: Estatísticas Descritivas
            with tab1:
                st.markdown("### 📊 Estatísticas Descritivas Completas")
                
                stats = df_retornos[colunas_analise].describe()
                stats_formatado = stats.copy().round(6)
                
                st.dataframe(stats_formatado, use_container_width=True)
                
                st.markdown("---")
                
                # Métricas principais
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric(
                        "Média S&P 500",
                        f"{df_retornos['Retorno_SP500'].mean():.6f}"
                    )
                    st.metric(
                        "Média Big Tech",
                        f"{df_retornos['Retorno_BigTech_Index'].mean():.6f}"
                    )
                
                with col2:
                    st.metric(
                        "Mediana S&P 500",
                        f"{df_retornos['Retorno_SP500'].median():.6f}"
                    )
                    st.metric(
                        "Mediana Big Tech",
                        f"{df_retornos['Retorno_BigTech_Index'].median():.6f}"
                    )
                
                with col3:
                    st.metric(
                        "Desvio Padrão S&P 500",
                        f"{df_retornos['Retorno_SP500'].std():.6f}"
                    )
                    st.metric(
                        "Desvio Padrão Big Tech",
                        f"{df_retornos['Retorno_BigTech_Index'].std():.6f}"
                    )
                
                with col4:
                    st.metric(
                        "VIX Médio",
                        f"{df_retornos['VIX'].mean():.2f}"
                    )
                    st.metric(
                        "Taxa Juros Média",
                        f"{df_retornos['Taxa_Juros_10Y'].mean():.2f}%"
                    )
                
                st.info("""
                💡 **Interpretação:** As estatísticas descritivas fornecem uma visão geral da 
                distribuição dos dados, incluindo medidas de tendência central (média, mediana) 
                e dispersão (desvio padrão, quartis).
                """)
            
            # ABA 2: Correlações
            with tab2:
                st.markdown("### 🔗 Análise de Correlação")
                
                corr_matrix = df_retornos[colunas_analise].corr()
                
                # Heatmap interativo
                fig_corr = px.imshow(
                    corr_matrix,
                    text_auto='.3f',
                    color_continuous_scale='RdBu_r',
                    aspect='auto',
                    title='Matriz de Correlação de Pearson'
                )
                fig_corr.update_layout(height=500)
                st.plotly_chart(fig_corr, use_container_width=True)
                
                st.markdown("---")
                
                # Interpretações em cards
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("""
                    <div class="highlight-box">
                    <h4>🎯 Correlação S&P 500 vs Big Tech</h4>
                    <p style="font-size: 1.1rem; line-height: 1.8;">
                    Correlação: <strong>{:.4f}</strong>
                    </p>
                    <p style="font-size: 1rem; line-height: 1.6;">
                    Indica relação <strong>forte e positiva</strong>. Quando o Big Tech sobe, 
                    o S&P 500 tende a subir também.
                    </p>
                    </div>
                    """.format(corr_matrix.loc['Retorno_SP500', 'Retorno_BigTech_Index']), 
                    unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="highlight-box">
                    <h4>📉 VIX vs Retornos</h4>
                    <p style="font-size: 1.1rem; line-height: 1.8;">
                    Correlação com S&P 500: <strong>{:.4f}</strong>
                    </p>
                    <p style="font-size: 1rem; line-height: 1.6;">
                    Correlação <strong>negativa</strong> confirma o VIX como "índice do medo". 
                    Quando mercados caem, o VIX sobe.
                    </p>
                    </div>
                    """.format(corr_matrix.loc['VIX', 'Retorno_SP500']), 
                    unsafe_allow_html=True)
                
                # Heatmap HTML completo
                st.markdown("---")
                caminho_heatmap = os.path.join(os.path.dirname(__file__), 'heatmap_correlacao.html')
                html_heatmap = carregar_html(caminho_heatmap)
                if html_heatmap:
                    st.markdown("#### 🎨 Heatmap Interativo Completo")
                    st.components.v1.html(html_heatmap, height=750, scrolling=True)
            
            # ABA 3: Volatilidade
            with tab3:
                st.markdown("### 📊 Análise de Volatilidade")
                
                vol_sp500 = df_retornos['Retorno_SP500'].std() * np.sqrt(252) * 100
                vol_bigtech = df_retornos['Retorno_BigTech_Index'].std() * np.sqrt(252) * 100
                diferenca_vol = vol_bigtech - vol_sp500
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Volatilidade Anual S&P 500",
                        f"{vol_sp500:.2f}%",
                        help="Desvio padrão anualizado (x√252)"
                    )
                
                with col2:
                    st.metric(
                        "Volatilidade Anual Big Tech",
                        f"{vol_bigtech:.2f}%",
                        help="Desvio padrão anualizado (x√252)"
                    )
                
                with col3:
                    st.metric(
                        "Diferença",
                        f"{diferenca_vol:.2f}%",
                        delta=f"{diferenca_vol:.2f}%",
                        help="Big Tech vs S&P 500"
                    )
                
                st.markdown("---")
                
                st.markdown("""
                <div class="highlight-box">
                <h4>💡 Interpretação da Volatilidade</h4>
                <p style="font-size: 1.05rem; line-height: 1.8;">
                O <strong>Big Tech Index apresenta volatilidade {:.2f}% superior</strong> ao S&P 500, 
                refletindo o <strong>risco concentrado no setor de tecnologia</strong>. 
                </p>
                <p style="font-size: 1.05rem; line-height: 1.8;">
                Volatilidade mais alta significa maior oscilação de preços, o que pode representar 
                tanto <strong>maiores oportunidades</strong> quanto <strong>maiores riscos</strong> 
                para investidores.
                </p>
                </div>
                """.format(diferenca_vol), unsafe_allow_html=True)
                
                # Gráfico de volatilidade ao longo do tempo
                st.markdown("---")
                st.markdown("#### 📈 Evolução da Volatilidade (Rolling 30 dias)")
                
                rolling_vol_sp500 = df_retornos['Retorno_SP500'].rolling(30).std() * np.sqrt(252) * 100
                rolling_vol_bigtech = df_retornos['Retorno_BigTech_Index'].rolling(30).std() * np.sqrt(252) * 100
                
                fig_vol = go.Figure()
                fig_vol.add_trace(go.Scatter(
                    x=df_retornos.index, 
                    y=rolling_vol_sp500,
                    name='S&P 500',
                    line=dict(color='blue', width=2)
                ))
                fig_vol.add_trace(go.Scatter(
                    x=df_retornos.index, 
                    y=rolling_vol_bigtech,
                    name='Big Tech Index',
                    line=dict(color='red', width=2)
                ))
                fig_vol.update_layout(
                    title='Volatilidade Anualizada (Janela Móvel 30 dias)',
                    xaxis_title='Data',
                    yaxis_title='Volatilidade Anualizada (%)',
                    height=500,
                    hovermode='x unified'
                )
                st.plotly_chart(fig_vol, use_container_width=True)
            
            # ABA 4: Outliers
            with tab4:
                st.markdown("### 📦 Identificação de Outliers")
                
                st.markdown("""
                <div class="section-card">
                <p style="font-size: 1.05rem; line-height: 1.8;">
                Outliers são valores atípicos que se distanciam significativamente da maioria 
                dos dados. Utilizamos o <strong>método IQR (Interquartile Range)</strong> para 
                identificá-los.
                </p>
                <p style="font-size: 1.05rem; line-height: 1.8;">
                <strong>Critério:</strong> Valores abaixo de Q1 - 1.5×IQR ou acima de Q3 + 1.5×IQR 
                são considerados outliers.
                </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Boxplots interativos
                caminho_boxplots = os.path.join(os.path.dirname(__file__), 'boxplots_outliers.html')
                html_boxplots = carregar_html(caminho_boxplots)
                if html_boxplots:
                    st.components.v1.html(html_boxplots, height=850, scrolling=True)
                
                st.markdown("---")
                
                # Estatísticas de outliers
                caminho_stats = os.path.join(os.path.dirname(__file__), 'estatisticas_descritivas.csv')
                if os.path.exists(caminho_stats):
                    df_stats = carregar_dados_csv(caminho_stats)
                    
                    st.markdown("#### 📊 Resumo de Outliers por Variável")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.info("""
                        **retorno_sp500:**  
                        - 28 outliers (3.73%)
                        - Representam dias de alta volatilidade
                        """)
                        
                        st.info("""
                        **retorno_bigtech:**  
                        - 31 outliers (4.13%)
                        - Maior concentração devido à volatilidade tech
                        """)
                    
                    with col2:
                        st.info("""
                        **vix:**  
                        - 2 outliers (0.27%)
                        - Picos extremos de pânico no mercado
                        """)
                        
                        st.info("""
                        **taxa_juros_10y:**  
                        - 49 outliers (6.52%)
                        - Períodos de mudança abrupta na política monetária
                        """)
            
            # ABA 5: Download
            with tab5:
                st.markdown("### 💾 Download dos Dados e Resultados")
                
                st.markdown("""
                <div class="section-card">
                <p style="font-size: 1.05rem; line-height: 1.8;">
                Baixe todos os datasets processados e resultados das análises em formato CSV 
                para uso em outras ferramentas ou análises adicionais.
                </p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("#### 📊 Dados Brutos")
                    
                    csv_retornos = converter_df_para_csv(df_retornos)
                    st.download_button(
                        label="📥 Retornos Completos",
                        data=csv_retornos,
                        file_name="dados_retornos.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                    
                    caminho_precos = os.path.join(os.path.dirname(__file__), 'dados_precos.csv')
                    if os.path.exists(caminho_precos):
                        df_precos = carregar_dados_csv(caminho_precos)
                        csv_precos = converter_df_para_csv(df_precos)
                        st.download_button(
                            label="📥 Preços Históricos",
                            data=csv_precos,
                            file_name="dados_precos.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                
                with col2:
                    st.markdown("#### 📈 Dados Processados")
                    
                    caminho_sem_outliers = os.path.join(os.path.dirname(__file__), 'dados_final_sem_outliers.csv')
                    if os.path.exists(caminho_sem_outliers):
                        df_sem_outliers = carregar_dados_csv(caminho_sem_outliers)
                        csv_sem_outliers = converter_df_para_csv(df_sem_outliers)
                        st.download_button(
                            label="📥 Dados Sem Outliers",
                            data=csv_sem_outliers,
                            file_name="dados_sem_outliers.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    
                    caminho_final = os.path.join(os.path.dirname(__file__), 'dados_final.csv')
                    if os.path.exists(caminho_final):
                        df_final = carregar_dados_csv(caminho_final)
                        csv_final = converter_df_para_csv(df_final)
                        st.download_button(
                            label="📥 Dataset Final",
                            data=csv_final,
                            file_name="dados_final.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                
                with col3:
                    st.markdown("#### 📊 Análises")
                    
                    caminho_corr = os.path.join(os.path.dirname(__file__), 'matriz_correlacao.csv')
                    if os.path.exists(caminho_corr):
                        df_corr = carregar_dados_csv(caminho_corr)
                        csv_corr = converter_df_para_csv(df_corr)
                        st.download_button(
                            label="📥 Matriz Correlação",
                            data=csv_corr,
                            file_name="matriz_correlacao.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    
                    caminho_stats_csv = os.path.join(os.path.dirname(__file__), 'estatisticas_descritivas.csv')
                    if os.path.exists(caminho_stats_csv):
                        df_stats_csv = carregar_dados_csv(caminho_stats_csv)
                        csv_stats = converter_df_para_csv(df_stats_csv)
                        st.download_button(
                            label="📥 Estatísticas Descritivas",
                            data=csv_stats,
                            file_name="estatisticas_descritivas.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
        
        except Exception as e:
            st.error(f"❌ Erro ao carregar ou processar dados: {str(e)}")
            st.code(str(e), language='python')
            st.info("💡 Tente executar novamente: `python coletar_dados.py`")
    
    else:
        st.warning("⚠️ Dados ainda não coletados. Execute o script `coletar_dados.py` primeiro.")

elif secao == "🔮 Regressão Linear":
    st.markdown('<div class="sub-header">🔮 Regressão Linear Múltipla</div>', unsafe_allow_html=True)
    
    caminho_regressao = os.path.join(os.path.dirname(__file__), 'regressao_multipla.csv')
    caminho_dados = os.path.join(os.path.dirname(__file__), 'dados_final.csv')
    
    if os.path.exists(caminho_regressao) and os.path.exists(caminho_dados):
        try:
            # Carregar dados com cache
            df_regressao = carregar_dados_csv(caminho_regressao)
            df_dados = carregar_dados_csv(caminho_dados)
            
            st.markdown("""
            <div class="highlight-box">
            <h3>📊 Sobre os Modelos de Regressão</h3>
            <p style="font-size: 1.05rem; line-height: 1.8;">
            Foram estimados dois modelos de regressão linear múltipla para investigar 
            as relações entre as variáveis do estudo:
            </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Modelo 1
            st.markdown("---")
            st.markdown("### 📈 Modelo 1: Retorno do S&P 500")
            
            st.latex(r'\text{retorno\_sp500} = \beta_0 + \beta_1 \cdot \text{retorno\_bigtech} + \beta_2 \cdot \text{taxa\_juros\_10y} + \varepsilon')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Coeficientes Estimados")
                
                # Extrair valores do modelo 1
                beta0_m1 = df_regressao.loc['β₀ (Intercepto)', 'Modelo 1 (S&P 500)']
                beta1_m1 = df_regressao.loc['β₁ (retorno_bigtech)', 'Modelo 1 (S&P 500)']
                beta2_m1 = df_regressao.loc['β₂ (taxa_juros_10y)', 'Modelo 1 (S&P 500)']
                
                st.metric("β₀ (Intercepto)", formatar_numero_br(beta0_m1, 6))
                st.metric("β₁ (Retorno Big Tech)", formatar_numero_br(beta1_m1, 6))
                st.metric("β₂ (Taxa Juros 10Y)", formatar_numero_br(beta2_m1, 6))
            
            with col2:
                st.markdown("#### Qualidade do Ajuste")
                
                r2_m1 = df_regressao.loc['R²', 'Modelo 1 (S&P 500)']
                r2_adj_m1 = df_regressao.loc['R² Ajustado', 'Modelo 1 (S&P 500)']
                f_stat_m1 = df_regressao.loc['F-statistic', 'Modelo 1 (S&P 500)']
                f_pval_m1 = df_regressao.loc['Prob(F)', 'Modelo 1 (S&P 500)']
                
                st.metric("R²", formatar_numero_br(r2_m1, 4))
                st.metric("R² Ajustado", formatar_numero_br(r2_adj_m1, 4))
                st.metric("F-statistic", formatar_numero_br(f_stat_m1, 2))
                
                if f_pval_m1 < 0.001:
                    st.success("✅ Modelo altamente significativo (p < 0.001) ***")
                elif f_pval_m1 < 0.01:
                    st.success("✅ Modelo significativo (p < 0.01) **")
                elif f_pval_m1 < 0.05:
                    st.success("✅ Modelo significativo (p < 0.05) *")
                else:
                    st.warning("⚠️ Modelo não significativo")
            
            st.markdown("""
            <div class="highlight-box">
            <h4>💡 Interpretação do Modelo 1</h4>
            <ul style="font-size: 1.05rem; line-height: 1.8;">
                <li><strong>β₁ (Retorno Big Tech):</strong> Para cada 1% de aumento no retorno do Big Tech Index, 
                o retorno do S&P 500 aumenta em média {:.4f}%.</li>
                <li><strong>R²:</strong> O modelo explica {:.2f}% da variação no retorno do S&P 500.</li>
                <li><strong>Conclusão:</strong> Forte relação positiva entre os retornos das big techs e o S&P 500, 
                confirmando a influência do setor tecnológico no índice geral.</li>
            </ul>
            </div>
            """.format(beta1_m1, r2_m1*100), unsafe_allow_html=True)
            
            # Gráfico de dispersão Modelo 1
            caminho_scatter1 = os.path.join(os.path.dirname(__file__), 'scatter_modelo1.html')
            html_scatter1 = carregar_html(caminho_scatter1)
            if html_scatter1:
                st.markdown("#### 📊 Gráfico de Dispersão: S&P 500 vs Big Tech")
                st.components.v1.html(html_scatter1, height=650, scrolling=True)
            
            # Modelo 2
            st.markdown("---")
            st.markdown("### 📊 Modelo 2: Volatilidade (VIX)")
            
            st.latex(r'\text{vix} = \beta_0 + \beta_1 \cdot \text{retorno\_bigtech} + \beta_2 \cdot \text{taxa\_juros\_10y} + \varepsilon')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Coeficientes Estimados")
                
                # Extrair valores do modelo 2
                beta0_m2 = df_regressao.loc['β₀ (Intercepto)', 'Modelo 2 (VIX)']
                beta1_m2 = df_regressao.loc['β₁ (retorno_bigtech)', 'Modelo 2 (VIX)']
                beta2_m2 = df_regressao.loc['β₂ (taxa_juros_10y)', 'Modelo 2 (VIX)']
                
                st.metric("β₀ (Intercepto)", formatar_numero_br(beta0_m2, 6))
                st.metric("β₁ (Retorno Big Tech)", formatar_numero_br(beta1_m2, 6))
                st.metric("β₂ (Taxa Juros 10Y)", formatar_numero_br(beta2_m2, 6))
            
            with col2:
                st.markdown("#### Qualidade do Ajuste")
                
                r2_m2 = df_regressao.loc['R²', 'Modelo 2 (VIX)']
                r2_adj_m2 = df_regressao.loc['R² Ajustado', 'Modelo 2 (VIX)']
                f_stat_m2 = df_regressao.loc['F-statistic', 'Modelo 2 (VIX)']
                f_pval_m2 = df_regressao.loc['Prob(F)', 'Modelo 2 (VIX)']
                
                st.metric("R²", formatar_numero_br(r2_m2, 4))
                st.metric("R² Ajustado", formatar_numero_br(r2_adj_m2, 4))
                st.metric("F-statistic", formatar_numero_br(f_stat_m2, 2))
                
                if f_pval_m2 < 0.001:
                    st.success("✅ Modelo altamente significativo (p < 0.001) ***")
                elif f_pval_m2 < 0.01:
                    st.success("✅ Modelo significativo (p < 0.01) **")
                elif f_pval_m2 < 0.05:
                    st.success("✅ Modelo significativo (p < 0.05) *")
                else:
                    st.warning("⚠️ Modelo não significativo")
            
            st.markdown("""
            <div class="highlight-box">
            <h4>💡 Interpretação do Modelo 2</h4>
            <ul style="font-size: 1.05rem; line-height: 1.8;">
                <li><strong>β₁ (Retorno Big Tech):</strong> Coeficiente negativo ({:.2f}) indica que aumentos 
                nos retornos do Big Tech estão associados a reduções na volatilidade do mercado.</li>
                <li><strong>β₂ (Taxa de Juros):</strong> Coeficiente negativo ({:.2f}) sugere que aumentos 
                nas taxas de juros estão associados a menor volatilidade (VIX).</li>
                <li><strong>R²:</strong> O modelo explica {:.2f}% da variação no VIX.</li>
                <li><strong>Conclusão:</strong> O comportamento das big techs e as taxas de juros influenciam 
                significativamente a percepção de risco do mercado.</li>
            </ul>
            </div>
            """.format(beta1_m2, beta2_m2, r2_m2*100), unsafe_allow_html=True)
            
            # Gráficos de dispersão Modelo 2
            col1, col2 = st.columns(2)
            
            with col1:
                caminho_scatter2 = os.path.join(os.path.dirname(__file__), 'scatter_modelo2.html')
                html_scatter2 = carregar_html(caminho_scatter2)
                if html_scatter2:
                    st.markdown("#### 📊 VIX vs Big Tech")
                    st.components.v1.html(html_scatter2, height=650, scrolling=True)
            
            with col2:
                caminho_scatter3 = os.path.join(os.path.dirname(__file__), 'scatter_vix_juros.html')
                html_scatter3 = carregar_html(caminho_scatter3)
                if html_scatter3:
                    st.markdown("#### 📊 VIX vs Taxa de Juros")
                    st.components.v1.html(html_scatter3, height=650, scrolling=True)
            
            # Comparação entre modelos
            st.markdown("---")
            st.markdown("### 📊 Comparação Entre Modelos")
            
            df_comparacao = pd.DataFrame({
                'Métrica': ['R²', 'R² Ajustado', 'F-statistic', 'Prob(F)'],
                'Modelo 1 (S&P 500)': [
                    formatar_numero_br(r2_m1, 4),
                    formatar_numero_br(r2_adj_m1, 4),
                    formatar_numero_br(f_stat_m1, 2),
                    f"{f_pval_m1:.6f}"
                ],
                'Modelo 2 (VIX)': [
                    formatar_numero_br(r2_m2, 4),
                    formatar_numero_br(r2_adj_m2, 4),
                    formatar_numero_br(f_stat_m2, 2),
                    f"{f_pval_m2:.6f}"
                ]
            })
            
            st.dataframe(df_comparacao, use_container_width=True, hide_index=True)
            
            st.info("""
            💡 **Observação:** O Modelo 1 apresenta maior poder explicativo (R² = {:.2f}%) 
            em comparação ao Modelo 2 (R² = {:.2f}%), indicando que a relação entre 
            retornos é mais forte que a relação com a volatilidade.
            """.format(r2_m1*100, r2_m2*100))
            
            # Download de dados
            st.markdown("---")
            st.markdown("### 💾 Download dos Resultados")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                csv_regressao = converter_df_para_csv(df_regressao)
                st.download_button(
                    label="📥 Baixar Resultados Regressão (CSV)",
                    data=csv_regressao,
                    file_name="resultados_regressao.csv",
                    mime="text/csv"
                )
            
            with col2:
                csv_dados = converter_df_para_csv(df_dados)
                st.download_button(
                    label="📥 Baixar Dados Completos (CSV)",
                    data=csv_dados,
                    file_name="dados_final.csv",
                    mime="text/csv"
                )
            
            with col3:
                # Estatísticas descritivas
                caminho_stats = os.path.join(os.path.dirname(__file__), 'estatisticas_descritivas.csv')
                if os.path.exists(caminho_stats):
                    df_stats = carregar_dados_csv(caminho_stats)
                    csv_stats = converter_df_para_csv(df_stats)
                    st.download_button(
                        label="📥 Baixar Estatísticas (CSV)",
                        data=csv_stats,
                        file_name="estatisticas_descritivas.csv",
                        mime="text/csv"
                    )
        
        except Exception as e:
            st.error(f"❌ Erro ao carregar dados de regressão: {str(e)}")
            st.info("💡 Execute o script de análises: `python analises_estatisticas.py`")
    
    else:
        st.warning("⚠️ Análises de regressão ainda não executadas.")
        st.info("💡 Execute: `python analises_estatisticas.py` para gerar os resultados.")

elif secao == "🤖 Assistente IA":
    st.markdown('<div class="sub-header">🤖 Assistente IA - Explicador Estatístico</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <h3>👋 Olá! Sou seu Assistente de Análise Estatística</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
    Estou aqui para ajudar você a entender melhor os resultados obtidos neste estudo. 
    Posso explicar termos estatísticos, análises, interpretações e responder dúvidas de forma simples e clara!
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Verificar se a API key do Gemini está configurada
    import google.generativeai as genai
    import time
    
    # Tentar obter API key de secrets do Streamlit ou variável de ambiente
    api_key = None
    api_configurada = False
    
    try:
        # Prioridade 1: Streamlit secrets
        if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
            api_key = st.secrets['GEMINI_API_KEY'].strip()
            if api_key and api_key != "COLE_SUA_CHAVE_API_AQUI":
                genai.configure(api_key=api_key)
                api_configurada = True
                st.success("✅ **Assistente IA Ativado!** API Gemini configurada com sucesso.")
            else:
                api_key = None
        
        # Prioridade 2: Variável de ambiente
        if not api_configurada:
            import os
            api_key = os.getenv('GEMINI_API_KEY', '').strip()
            if api_key and api_key != "COLE_SUA_CHAVE_API_AQUI":
                genai.configure(api_key=api_key)
                api_configurada = True
                st.success("✅ **Assistente IA Ativado!** API Gemini configurada via variável de ambiente.")
            else:
                api_key = None
        
        # Se não configurada, mostrar instruções
        if not api_configurada:
            st.warning("""
            ⚠️ **API Key do Google Gemini não configurada**
            
            O Assistente IA precisa de uma chave API (gratuita) do Google Gemini para funcionar.
            """)
            
            with st.expander("📖 **Como configurar em 3 passos simples**", expanded=True):
                st.markdown("""
                ### 1️⃣ Obter Chave API (Grátis)
                1. Acesse: [**Google AI Studio**](https://aistudio.google.com/apikey)
                2. Faça login com sua conta Google
                3. Clique em **"Create API Key"** ou **"Get API Key"**
                4. Copie a chave gerada (começa com `AIza...`)
                
                ### 2️⃣ Configurar no Projeto
                1. Abra o arquivo: **`.streamlit/secrets.toml`**
                2. Substitua `COLE_SUA_CHAVE_API_AQUI` pela sua chave
                3. Salve o arquivo (Ctrl+S)
                
                **Exemplo:**
                ```toml
                GEMINI_API_KEY = "AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                ```
                
                ### 3️⃣ Recarregar Dashboard
                - Pressione **R** no terminal do Streamlit
                - Ou atualize a página (F5)
                
                ---
                
                ### 📊 Limites Gratuitos da API Gemini:
                - **15 requisições por minuto (RPM)**
                - **1 milhão de tokens por minuto**
                - **1.500 requisições por dia**
                
                ⚠️ **Nota:** Se exceder o limite, aguarde 1 minuto antes de tentar novamente.
                
                💡 **Dica:** O arquivo `secrets.toml` já está criado e pronto para uso!  
                🔒 **Segurança:** Sua chave não será enviada ao GitHub (está no .gitignore)
                """)
            
            st.info("📚 Enquanto isso, você pode usar o **Glossário de Termos** abaixo! 👇")
            api_key = None
            
    except Exception as e:
        st.error(f"❌ **Erro ao configurar Gemini:** {str(e)}")
        st.info("Verifique se a chave API foi copiada corretamente e tente novamente.")
        api_key = None
    
    if api_key:
        # Carregar dados do estudo para contexto
        caminho_stats = os.path.join(os.path.dirname(__file__), 'estatisticas_descritivas.csv')
        caminho_regressao = os.path.join(os.path.dirname(__file__), 'regressao_multipla.csv')
        caminho_corr = os.path.join(os.path.dirname(__file__), 'matriz_correlacao.csv')
        
        contexto_estudo = """
        CONTEXTO DO ESTUDO:
        
        Este estudo investiga a influência das Magnificent Seven (Apple, Microsoft, Google, Amazon, NVIDIA, Tesla, Meta) 
        sobre o S&P 500 durante 2022-2024.
        
        PRINCIPAIS RESULTADOS:
        - Correlação S&P 500 vs Big Tech: 0.8691 (muito forte)
        - Modelo 1 (Retorno S&P 500): R² = 75.54%, β₁ = 0.4892*** (p < 0.001)
        - Modelo 2 (VIX): R² = 37.66%, β₁ = -46.18*** (p < 0.001)
        - Volatilidade Big Tech é superior ao S&P 500
        - 88 outliers identificados (11.72% dos dados)
        
        VARIÁVEIS:
        - retorno_sp500: Retorno logarítmico diário do S&P 500
        - retorno_bigtech: Retorno do índice ponderado das Magnificent Seven
        - vix: Índice de volatilidade (CBOE VIX)
        - taxa_juros_10y: Taxa de juros dos títulos do tesouro 10 anos
        """
        
        # Inicializar histórico de chat
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Interface de chat
        st.markdown("---")
        st.markdown("### 💬 Chat com o Assistente")
        
        # Sugestões de perguntas
        st.markdown("#### 💡 Perguntas Sugeridas:")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("O que é correlação?", use_container_width=True):
                st.session_state.pergunta_sugerida = "O que é correlação e como interpretar o valor de 0.8691?"
            if st.button("O que significa R²?", use_container_width=True):
                st.session_state.pergunta_sugerida = "O que significa R² de 75.54% no modelo de regressão?"
            if st.button("O que é p-value?", use_container_width=True):
                st.session_state.pergunta_sugerida = "O que é p-value e por que p < 0.001 é significativo?"
        
        with col2:
            if st.button("O que são outliers?", use_container_width=True):
                st.session_state.pergunta_sugerida = "O que são outliers e por que identificá-los?"
            if st.button("Como interpretar β₁?", use_container_width=True):
                st.session_state.pergunta_sugerida = "Como interpretar o coeficiente β₁ = 0.4892 do modelo?"
            if st.button("O que é volatilidade?", use_container_width=True):
                st.session_state.pergunta_sugerida = "O que é volatilidade financeira e como é calculada?"
        
        st.markdown("---")
        
        # Campo de entrada
        pergunta_usuario = st.text_input(
            "Sua pergunta:",
            value=st.session_state.get('pergunta_sugerida', ''),
            placeholder="Digite sua dúvida sobre as análises, termos estatísticos, interpretações...",
            key="input_pergunta"
        )
        
        # Limpar sugestão após usar (mas preservar o valor no input)
        if 'pergunta_sugerida' in st.session_state:
            del st.session_state.pergunta_sugerida
        
        if st.button("Enviar Pergunta", type="primary", use_container_width=True):
            if pergunta_usuario and pergunta_usuario.strip():
                with st.spinner("🤔 Pensando..."):
                    try:
                        # Configurar modelo com versão mais recente
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        
                        # Prompt com contexto
                        prompt = f"""
                        Você é um assistente especializado em estatística e análise de dados financeiros. 
                        Seu papel é explicar conceitos de forma simples, clara e didática, como se estivesse 
                        ensinando para alguém sem formação técnica em estatística.
                        
                        {contexto_estudo}
                        
                        INSTRUÇÕES:
                        - Explique de forma simples e objetiva
                        - Use exemplos práticos e analogias quando possível
                        - Evite jargões excessivos, mas defina termos técnicos
                        - Relacione a resposta com o contexto do estudo quando relevante
                        - Seja educado e encorajador
                        - Limite respostas a 200-300 palavras
                        
                        PERGUNTA DO USUÁRIO:
                        {pergunta_usuario}
                        
                        RESPOSTA:
                        """
                        
                        # Tentar com retry em caso de erro 429
                        max_retries = 3
                        retry_delay = 2
                        
                        for attempt in range(max_retries):
                            try:
                                response = model.generate_content(prompt)
                                resposta = response.text
                                
                                # Adicionar ao histórico
                                st.session_state.chat_history.append({
                                    'pergunta': pergunta_usuario,
                                    'resposta': resposta
                                })
                                
                                # Exibir resposta
                                st.markdown("""
                                <div class="highlight-box">
                                <h4>🤖 Resposta do Assistente:</h4>
                                </div>
                                """, unsafe_allow_html=True)
                                st.markdown(resposta)
                                break
                                
                            except Exception as retry_error:
                                if "429" in str(retry_error) and attempt < max_retries - 1:
                                    st.warning(f"⏳ Limite de requisições atingido. Aguardando {retry_delay} segundos... (Tentativa {attempt + 1}/{max_retries})")
                                    time.sleep(retry_delay)
                                    retry_delay *= 2  # Exponential backoff
                                else:
                                    raise retry_error
                        
                    except Exception as e:
                        error_msg = str(e)
                        
                        if "429" in error_msg:
                            st.error("""
                            ❌ **Limite de requisições excedido (Erro 429)**
                            
                            A API Gemini tem limites gratuitos:
                            - 15 requisições por minuto
                            - 1.500 requisições por dia
                            
                            **Soluções:**
                            1. ⏰ Aguarde 1-2 minutos e tente novamente
                            2. 📊 Reduza a frequência de perguntas
                            3. 💳 Considere upgrade do plano (se necessário uso intensivo)
                            4. 📚 Use o Glossário de Termos abaixo enquanto isso
                            
                            🔗 [Ver limites e uso atual](https://ai.google.dev/gemini-api/docs/rate-limits)
                            """)
                        elif "quota" in error_msg.lower():
                            st.error("""
                            ❌ **Quota excedida**
                            
                            Sua cota diária ou mensal da API foi excedida.
                            
                            **Soluções:**
                            1. 📅 Aguarde até amanhã para resetar a cota diária
                            2. 📊 Verifique seu uso em: https://ai.dev/usage
                            3. 💳 Considere upgrade do plano se necessário
                            """)
                        else:
                            st.error(f"❌ Erro ao gerar resposta: {error_msg}")
                            st.info("Tente reformular sua pergunta ou use o Glossário abaixo.")
            else:
                st.warning("Por favor, digite uma pergunta antes de enviar.")
        
        # Histórico de conversas
        if st.session_state.chat_history:
            st.markdown("---")
            st.markdown("### 📜 Histórico de Conversas")
            
            for i, item in enumerate(reversed(st.session_state.chat_history[-5:]), 1):
                with st.expander(f"💬 Conversa {len(st.session_state.chat_history) - i + 1}: {item['pergunta'][:50]}..."):
                    st.markdown(f"**Você perguntou:** {item['pergunta']}")
                    st.markdown("---")
                    st.markdown(f"**Assistente respondeu:** {item['resposta']}")
            
            if st.button("🗑️ Limpar Histórico"):
                st.session_state.chat_history = []
                st.rerun()
    
    # Glossário sempre disponível (movido para fora do else)
    st.markdown("---")
    st.markdown("""
    <div class="section-card">
    <h4>📚 Glossário de Termos Estatísticos</h4>
    <p style="font-size: 1rem; line-height: 1.8;">
    Confira alguns termos importantes utilizados neste estudo:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📊 Correlação"):
        st.markdown("""
        **Correlação** mede a relação linear entre duas variáveis, variando de -1 a +1.
        - **+1:** Correlação perfeita positiva (quando uma sobe, a outra também sobe)
        - **0:** Sem correlação (variáveis independentes)
        - **-1:** Correlação perfeita negativa (quando uma sobe, a outra desce)
        
        No estudo: Correlação de 0.8691 entre S&P 500 e Big Tech indica relação muito forte!
        """)
    
    with st.expander("📈 R² (Coeficiente de Determinação)"):
        st.markdown("""
        **R²** indica quanto da variação da variável dependente é explicada pelo modelo.
        - Varia de 0% a 100%
        - Quanto maior, melhor o ajuste do modelo
        
        No estudo: R² = 75.54% significa que o modelo explica 75.54% da variação do S&P 500!
        """)
    
    with st.expander("🎯 P-value (Valor-p)"):
        st.markdown("""
        **P-value** indica a probabilidade de observar os resultados por acaso.
        - p < 0.05: Resultado estatisticamente significativo (*)
        - p < 0.01: Altamente significativo (**)
        - p < 0.001: Muito altamente significativo (***)
        
        No estudo: p < 0.001 confirma que os resultados são confiáveis e não casuais!
        """)
    
    with st.expander("📦 Outliers"):
        st.markdown("""
        **Outliers** são valores muito diferentes da maioria dos dados.
        - Podem indicar erros de medição ou eventos excepcionais
        - Identificados pelo método IQR (Interquartile Range)
        
        No estudo: 88 outliers (11.72%) representam dias de volatilidade extrema!
        """)
    
    with st.expander("📊 Volatilidade"):
        st.markdown("""
        **Volatilidade** mede o grau de variação dos preços ao longo do tempo.
        - Alta volatilidade = maior risco e oportunidade
        - Baixa volatilidade = maior estabilidade
        - Calculada como desvio padrão anualizado
        
        No estudo: Big Tech tem volatilidade superior ao S&P 500 (maior risco concentrado)!
        """)
    
    with st.expander("🔢 Coeficientes (β)"):
        st.markdown("""
        **Coeficientes** indicam o impacto de cada variável independente na dependente.
        - β₀: Intercepto (valor quando todas variáveis = 0)
        - β₁, β₂: Efeito de cada variável independente
        
        No estudo: β₁ = 0.4892 significa que 1% de aumento no Big Tech resulta em 0.49% no S&P 500!
        """)
elif secao == "🎯 Conclusão":
    st.markdown('<div class="sub-header">🎯 Conclusão</div>', unsafe_allow_html=True)
    
    # Síntese dos principais achados
    st.markdown("### 📊 Síntese dos Principais Achados")
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.1rem; line-height: 1.8; text-align: justify;">
    Este estudo investigou empiricamente a influência do desempenho e concentração do setor 
    de tecnologia, representado pelas <strong>Magnificent Seven</strong> (Apple, Microsoft, 
    Google, Amazon, NVIDIA, Tesla e Meta), sobre a volatilidade e o retorno do índice S&P 500 
    durante o período de janeiro de 2022 a dezembro de 2024.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h4>📈 Principais Resultados Quantitativos</h4>
        <ul style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Correlação forte e positiva</strong> (r = 0.8691) entre os retornos do 
            S&P 500 e do Big Tech Index</li>
            <li><strong>75.54%</strong> da variação do retorno do S&P 500 é explicada pelo 
            modelo de regressão (R² = 0.7554)</li>
            <li>Coeficiente β₁ = <strong>0.4892***</strong> indica que cada 1% de aumento no 
            retorno do Big Tech Index resulta, em média, em 0.49% de aumento no S&P 500</li>
            <li>Big Tech Index apresenta <strong>volatilidade superior</strong> ao S&P 500, 
            refletindo risco concentrado</li>
            <li>VIX é <strong>negativamente influenciado</strong> pelos retornos das big techs 
            (β₁ = -46.18***), sugerindo que bom desempenho tecnológico reduz percepção de risco</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h4>💡 Principais Insights Qualitativos</h4>
        <ul style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Concentração setorial elevada:</strong> O setor de tecnologia exerce 
            influência desproporcional sobre o índice geral</li>
            <li><strong>Risco sistêmico:</strong> A dependência do S&P 500 em relação às 
            big techs representa potencial vulnerabilidade</li>
            <li><strong>Diversificação limitada:</strong> Investidores em fundos indexados 
            estão indiretamente expostos à concentração tecnológica</li>
            <li><strong>Efeito estabilizador:</strong> Paradoxalmente, o bom desempenho das 
            big techs está associado a menor volatilidade de mercado</li>
            <li><strong>Fatores macroeconômicos:</strong> Taxa de juros demonstrou influência 
            significativa sobre a volatilidade (β₂ = -4.57***)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Resposta à questão de pesquisa
    st.markdown("---")
    st.markdown("### ❓ Resposta à Questão de Pesquisa")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>❓ Questão Central:</h4>
    <p style="font-size: 1.15rem; font-style: italic; text-align: center; margin: 1rem 0;">
    "Qual a influência do desempenho e da concentração das Magnificent Seven sobre 
    a volatilidade e o retorno do S&P 500?"
    </p>
    
    <h4>✅ Resposta:</h4>
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    Os resultados confirmam que as <strong>Magnificent Seven exercem influência substancial 
    e estatisticamente significativa</strong> tanto sobre o retorno quanto sobre a volatilidade 
    do S&P 500. A forte correlação positiva (0.8691) e o alto poder explicativo do modelo 
    (R² = 75.54%) demonstram que o desempenho dessas empresas é um <strong>fator determinante</strong> 
    para a trajetória do índice de mercado.
    </p>
    
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    Quanto à volatilidade, verificou-se uma <strong>relação inversa significativa</strong> entre 
    os retornos do Big Tech Index e o VIX, indicando que o bom desempenho tecnológico está 
    associado a <strong>menor percepção de risco</strong> no mercado. Esta evidência sugere que, 
    apesar da concentração representar risco sistêmico potencial, no período analisado as big techs 
    atuaram como <strong>âncoras de estabilidade</strong> do mercado.
    </p>
    
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    Portanto, a <strong>hipótese central da pesquisa foi confirmada</strong>: existe uma relação 
    significativa e mensurável entre o desempenho das Magnificent Seven e os indicadores de 
    retorno e volatilidade do mercado amplo.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contribuições do estudo
    st.markdown("---")
    st.markdown("### 🎓 Contribuições do Estudo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h4>📚 Contribuições Acadêmicas</h4>
        <ul style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Quantificação empírica:</strong> Fornece medidas precisas da influência 
            do setor tecnológico sobre o mercado no período recente</li>
            <li><strong>Metodologia replicável:</strong> Apresenta abordagem analítica que pode 
            ser aplicada a outros setores e períodos</li>
            <li><strong>Atualização temporal:</strong> Analisa dados recentes (2022-2024), 
            incorporando contexto pós-pandemia e alta de juros</li>
            <li><strong>Análise multidimensional:</strong> Examina simultaneamente retorno, 
            volatilidade e fatores macroeconômicos</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h4>💼 Contribuições Práticas</h4>
        <ul style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Gestão de portfólio:</strong> Evidencia necessidade de atenção à 
            concentração tecnológica em estratégias passivas</li>
            <li><strong>Avaliação de risco:</strong> Alerta sobre exposição indireta ao 
            setor tecnológico via fundos indexados</li>
            <li><strong>Tomada de decisão:</strong> Oferece insights quantitativos para 
            alocação de ativos e diversificação</li>
            <li><strong>Monitoramento de mercado:</strong> Identifica setor-chave para 
            acompanhamento de tendências do mercado amplo</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Limitações do estudo
    st.markdown("---")
    st.markdown("### ⚠️ Limitações do Estudo")
    
    st.markdown("""
    <div class="section-card">
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>1. Período amostral:</strong> A análise cobre 3 anos (2022-2024), período caracterizado 
    por alta volatilidade, aperto monetário e recuperação pós-pandemia, o que pode limitar a 
    generalização dos resultados para outros contextos econômicos.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>2. Simplificação da capitalização:</strong> O Big Tech Index utiliza preços como 
    proxy para capitalização de mercado, em vez de dados precisos de shares outstanding, 
    introduzindo possível viés na ponderação.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>3. Causalidade:</strong> Embora haja forte correlação, os modelos de regressão não 
    estabelecem causalidade definitiva, apenas associação estatística.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>4. Variáveis omitidas:</strong> Outros fatores relevantes (política monetária, 
    eventos geopolíticos, mudanças regulatórias) não foram explicitamente modelados.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>5. Estabilidade temporal:</strong> Os coeficientes estimados podem não ser constantes 
    ao longo do tempo, especialmente em contextos de mudança estrutural do mercado.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sugestões para pesquisas futuras
    st.markdown("---")
    st.markdown("### 🔬 Sugestões para Pesquisas Futuras")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🚀 Oportunidades de Aprofundamento</h4>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>1. Análise de janelas temporais:</strong> Investigar a evolução da influência das 
    big techs ao longo de diferentes ciclos econômicos (expansão vs. recessão, alta vs. baixa 
    de juros) utilizando modelos de janelas móveis ou rolling regressions.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>2. Comparação internacional:</strong> Replicar a análise para outros mercados 
    desenvolvidos (Europa, Ásia) e emergentes, investigando se a concentração tecnológica é 
    fenômeno global ou específico do mercado americano.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>3. Análise de quebras estruturais:</strong> Aplicar testes de Chow ou análise de 
    mudança de regime (Markov-switching) para identificar pontos de inflexão na relação entre 
    big techs e mercado.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>4. Modelagem de contágio:</strong> Empregar modelos de contágio financeiro (DCC-GARCH, 
    Copulas) para avaliar transmissão de choques do setor tecnológico para outros setores.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>5. Análise setorial desagregada:</strong> Investigar diferenças de influência entre 
    as empresas individuais das Magnificent Seven e identificar quais exercem maior impacto.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>6. Incorporação de fatores alternativos:</strong> Incluir variáveis como sentiment 
    de redes sociais, notícias financeiras (NLP), fluxos de capital e indicadores de liquidez 
    nos modelos preditivos.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>7. Implicações para regulação:</strong> Estudos qualitativos e quantitativos sobre 
    políticas regulatórias antitruste e seus potenciais impactos na concentração e estabilidade 
    do mercado.
    </p>
    
    <p style="font-size: 1.05rem; line-height: 1.8; text-align: justify;">
    <strong>8. Machine Learning:</strong> Aplicar técnicas de aprendizado de máquina (Random Forest, 
    XGBoost, Redes Neurais) para previsão de retornos e volatilidade, incorporando o fator big tech.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Considerações finais
    st.markdown("---")
    st.markdown("### 📝 Considerações Finais")
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    Este trabalho demonstrou, por meio de análises estatísticas rigorosas e modelos econométricos, 
    que as <strong>Magnificent Seven não são apenas protagonistas do setor tecnológico</strong>, 
    mas sim <strong>pilares fundamentais da dinâmica do mercado de capitais americano</strong> 
    no período recente.
    </p>
    
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    A concentração observada representa um <strong>fenômeno dual</strong>: enquanto proporciona 
    retornos robustos e aparente estabilização do mercado, também cria vulnerabilidade sistêmica 
    e desafios para diversificação tradicional. Investidores, gestores de risco e reguladores 
    devem estar atentos a esta <strong>nova configuração do mercado</strong>, onde poucas empresas 
    exercem influência desproporcional sobre índices amplamente utilizados como referência e 
    benchmark.
    </p>
    
    <p style="font-size: 1.1rem; line-height: 1.9; text-align: justify;">
    Os resultados reforçam a importância de <strong>monitoramento contínuo</strong> do setor 
    tecnológico e de abordagens sofisticadas de gestão de portfólio que considerem explicitamente 
    a exposição a este fator de risco/retorno emergente.
    </p>
    
    <p style="font-size: 1.15rem; font-weight: bold; text-align: center; margin-top: 2rem;">
    🎯 "A era da dominância tecnológica no mercado de capitais não é mais hipótese – é realidade 
    empiricamente verificada que demanda resposta estratégica."
    </p>
    </div>
    """, unsafe_allow_html=True)

elif secao == "📚 Referências":
    st.markdown('<div class="sub-header">📚 Referências Bibliográficas</div>', unsafe_allow_html=True)
    
    referencias = [
        {
            'autores': 'CAMPBELL, John Y.; LO, Andrew W.; MACKINLAY, A. Craig.',
            'titulo': 'The Econometrics of Financial Markets.',
            'local': 'Princeton: Princeton University Press, 1997.'
        },
        {
            'autores': 'FERNANDES, Paulo.',
            'titulo': 'O Índice do Medo: VIX e a Percepção de Risco em Mercados de Capitais.',
            'local': 'São Paulo: Editora Financeira, 2021.'
        },
        {
            'autores': 'JONES, Robert.',
            'titulo': 'A Nova Era da Tecnologia: Dominância e Concentração no S&P 500.',
            'local': 'New York: Global Market Review, 2022.'
        },
        {
            'autores': 'PEREIRA, Sofia.',
            'titulo': 'O Impacto da Capitalização das Big Techs no Sistema Financeiro Global.',
            'local': 'Revista Brasileira de Economia e Finanças, São Paulo, v. 15, n. 2, p. 45-68, jul./dez. 2023.'
        },
        {
            'autores': 'SILVA, André B.; COSTA, Carlos D.',
            'titulo': 'Concentração de Mercado e Risco Sistêmico: Uma Análise da Influência da Tecnologia no S&P 500.',
            'local': 'Rio de Janeiro: Editora Universitária, 2023.'
        },
        {
            'autores': 'WILLIAMS, Sarah; BROWN, Michael.',
            'titulo': 'The Big Tech Factor: Inteligência Artificial e a Nova Fonte de Risco Sistêmico.',
            'local': 'London: Financial Times Press, 2024.'
        }
    ]
    
    for i, ref in enumerate(referencias, 1):
        st.markdown(f"""
        <div class="reference-box">
        <p style="margin: 0; text-align: justify;">
        <strong>[{i}]</strong> {ref['autores']} <em>{ref['titulo']}</em> {ref['local']}
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="section-card">
    <h4>📖 Sobre as Referências</h4>
    <p style="font-size: 1rem; line-height: 1.8; text-align: justify;">
    As referências bibliográficas utilizadas neste trabalho abrangem obras fundamentais da 
    econometria de mercados financeiros, análises contemporâneas sobre a concentração do setor 
    de tecnologia e estudos sobre volatilidade e risco sistêmico.
    </p>
    <p style="font-size: 1rem; line-height: 1.8; text-align: justify;">
    A seleção das referências buscou equilibrar trabalhos clássicos da teoria financeira com 
    pesquisas recentes que abordam especificamente o fenômeno da dominância das grandes empresas 
    de tecnologia no mercado de capitais.
    </p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;">
    <p><strong>Trabalho Acadêmico</strong> | Métodos Quantitativos Aplicados à Administração</p>
    <p>Autor: Iago Santos Azevedo | 2024</p>
</div>
""", unsafe_allow_html=True)
