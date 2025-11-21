import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from io import StringIO

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
     "🔮 Regressão Linear", "📋 Quadros", "🎯 Conclusão", "📚 Referências"]
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
        
        st.code("""
# Execute no terminal:
python coletar_dados.py
        """, language='bash')

elif secao == "📈 Análise Estatística":
    st.markdown('<div class="sub-header">📈 Análise Estatística Descritiva</div>', unsafe_allow_html=True)
    
    caminho_retornos = os.path.join(os.path.dirname(__file__), 'dados_retornos.csv')
    
    if os.path.exists(caminho_retornos):
        try:
            df_retornos = pd.read_csv(caminho_retornos, index_col=0, parse_dates=True)
            
            # Estatísticas descritivas
            st.markdown("### 📊 Estatísticas Descritivas")
            
            colunas_analise = ['Retorno_SP500', 'Retorno_BigTech_Index', 'VIX', 'Taxa_Juros_10Y']
            stats = df_retornos[colunas_analise].describe()
            
            # Formatar para exibição
            stats_formatado = stats.copy()
            stats_formatado = stats_formatado.round(6)
            
            st.dataframe(stats_formatado, use_container_width=True)
            
            # Análise de correlação
            st.markdown("---")
            st.markdown("### 🔗 Matriz de Correlação")
            
            corr_matrix = df_retornos[colunas_analise].corr()
            
            fig_corr = px.imshow(
                corr_matrix,
                text_auto='.3f',
                color_continuous_scale='RdBu_r',
                aspect='auto',
                title='Matriz de Correlação entre Variáveis'
            )
            fig_corr.update_layout(height=500)
            st.plotly_chart(fig_corr, use_container_width=True)
            
            # Interpretações
            st.markdown("---")
            st.markdown("### 💡 Principais Achados")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="highlight-box">
                <h4>🎯 Correlação S&P 500 vs Big Tech</h4>
                <p style="font-size: 1.1rem; line-height: 1.8;">
                A correlação entre o retorno do S&P 500 e o Big Tech Index é de 
                <strong>{:.4f}</strong>, indicando uma relação <strong>forte e positiva</strong> 
                entre os dois índices.
                </p>
                </div>
                """.format(corr_matrix.loc['Retorno_SP500', 'Retorno_BigTech_Index']), 
                unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="highlight-box">
                <h4>📉 VIX e Retornos</h4>
                <p style="font-size: 1.1rem; line-height: 1.8;">
                O VIX apresenta correlação <strong>negativa</strong> com os retornos 
                ({:.4f} com S&P 500), confirmando seu papel como "índice do medo".
                </p>
                </div>
                """.format(corr_matrix.loc['VIX', 'Retorno_SP500']), 
                unsafe_allow_html=True)
            
            # Volatilidade
            st.markdown("---")
            st.markdown("### 📊 Análise de Volatilidade")
            
            col1, col2, col3 = st.columns(3)
            
            vol_sp500 = df_retornos['Retorno_SP500'].std() * np.sqrt(252) * 100
            vol_bigtech = df_retornos['Retorno_BigTech_Index'].std() * np.sqrt(252) * 100
            
            with col1:
                st.metric(
                    "Volatilidade Anual S&P 500",
                    f"{vol_sp500:.2f}%"
                )
            
            with col2:
                st.metric(
                    "Volatilidade Anual Big Tech",
                    f"{vol_bigtech:.2f}%"
                )
            
            with col3:
                diferenca_vol = vol_bigtech - vol_sp500
                st.metric(
                    "Diferença de Volatilidade",
                    f"{diferenca_vol:.2f}%",
                    delta=f"{diferenca_vol:.2f}%"
                )
            
            st.info("""
            💡 **Observação:** O Big Tech Index apresenta maior volatilidade que o S&P 500, 
            refletindo o risco concentrado no setor de tecnologia.
            """)
            
            # Visualizações adicionais
            st.markdown("---")
            st.markdown("### 📊 Visualizações Adicionais")
            
            # Carregar boxplots
            caminho_boxplots = os.path.join(os.path.dirname(__file__), 'boxplots_outliers.html')
            html_boxplots = carregar_html(caminho_boxplots)
            if html_boxplots:
                st.markdown("#### 📦 Boxplots - Identificação de Outliers")
                st.components.v1.html(html_boxplots, height=850, scrolling=True)
            
            # Carregar heatmap
            caminho_heatmap = os.path.join(os.path.dirname(__file__), 'heatmap_correlacao.html')
            html_heatmap = carregar_html(caminho_heatmap)
            if html_heatmap:
                st.markdown("#### 🎨 Heatmap - Matriz de Correlação")
                st.components.v1.html(html_heatmap, height=750, scrolling=True)
            
            # Download de dados
            st.markdown("---")
            st.markdown("### 💾 Download dos Dados")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                csv_retornos = converter_df_para_csv(df_retornos)
                st.download_button(
                    label="📥 Baixar Retornos (CSV)",
                    data=csv_retornos,
                    file_name="dados_retornos.csv",
                    mime="text/csv"
                )
            
            with col2:
                # Carregar dados sem outliers
                caminho_sem_outliers = os.path.join(os.path.dirname(__file__), 'dados_final_sem_outliers.csv')
                if os.path.exists(caminho_sem_outliers):
                    df_sem_outliers = carregar_dados_csv(caminho_sem_outliers)
                    csv_sem_outliers = converter_df_para_csv(df_sem_outliers)
                    st.download_button(
                        label="📥 Baixar Dados Sem Outliers (CSV)",
                        data=csv_sem_outliers,
                        file_name="dados_sem_outliers.csv",
                        mime="text/csv"
                    )
            
            with col3:
                # Carregar matriz de correlação
                caminho_corr = os.path.join(os.path.dirname(__file__), 'matriz_correlacao.csv')
                if os.path.exists(caminho_corr):
                    df_corr = carregar_dados_csv(caminho_corr)
                    csv_corr = converter_df_para_csv(df_corr)
                    st.download_button(
                        label="📥 Baixar Correlação (CSV)",
                        data=csv_corr,
                        file_name="matriz_correlacao.csv",
                        mime="text/csv"
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

elif secao == "📋 Quadros":
    st.markdown('<div class="sub-header">📊 Quadros e Tabelas</div>', unsafe_allow_html=True)
    
    st.markdown("### Quadro 1 - Definição e Papel das Variáveis no Modelo")
    
    # Criar DataFrame para Quadro 1
    df_quadro1 = pd.DataFrame({
        'Variável': [
            'Retorno S&P 500',
            'Índice VIX',
            'Retorno Tech Index',
            'Taxa de Juros 10Y'
        ],
        'Definição': [
            'Variação percentual logarítmica diária do índice S&P 500',
            'Valor de fechamento diário do Índice de Volatilidade CBOE',
            'Variação percentual logarítmica diária de um índice de mercado ponderado, composto pelas ações das "Magnificent Seven"',
            'Taxa de rendimento (yield) diária dos títulos do tesouro americano com vencimento em 10 anos'
        ],
        'Papel no modelo': [
            '🎯 Dependente',
            '🎯 Dependente',
            '📊 Independente',
            '🔧 Controle'
        ]
    })
    
    # Estilizar e exibir tabela
    st.dataframe(
        df_quadro1,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    st.markdown("### Quadro 2 - Exemplo da Estrutura dos Resultados da Regressão")
    
    # Criar DataFrame para Quadro 2
    df_quadro2 = pd.DataFrame({
        'Modelo': [
            'Modelo 1: Retorno S&P 500',
            '',
            '',
            '',
            'Modelo 2: VIX',
            '',
            '',
            ''
        ],
        'Variável': [
            '',
            'Intercepto (β₀)',
            'Retorno Tech Index (β₁)',
            'Taxa de Juros 10Y (β₂)',
            '',
            'Intercepto (β₀)',
            'Retorno Tech Index (β₁)',
            'Taxa de Juros 10Y (β₂)'
        ],
        'Coeficiente': ['', '—', '—', '—', '', '—', '—', '—'],
        'Erro Padrão': ['', '—', '—', '—', '', '—', '—', '—'],
        'Valor-p': ['', '—', '—', '—', '', '—', '—', '—'],
        'R² Ajustado': ['—', '', '', '', '—', '', '', '']
    })
    
    st.dataframe(
        df_quadro2,
        use_container_width=True,
        hide_index=True
    )
    
    st.info("""
    💡 **Nota:** Esta é uma estrutura de exemplo. Os valores serão preenchidos após a execução 
    da análise estatística dos dados coletados.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="section-card">
    <h4>📝 Observações sobre os Quadros</h4>
    <p style="font-size: 1rem; line-height: 1.8;">
    <strong>Quadro 1</strong> apresenta a definição operacional de cada variável utilizada no estudo 
    e seu papel no modelo estatístico (dependente, independente ou de controle).
    </p>
    <p style="font-size: 1rem; line-height: 1.8;">
    <strong>Quadro 2</strong> ilustra a estrutura esperada dos resultados das regressões que serão 
    estimadas. Para cada modelo, serão reportados os coeficientes estimados, os erros padrão, 
    os valores-p (que indicam a significância estatística) e o R² ajustado (que mede a qualidade 
    do ajuste do modelo).
    </p>
    </div>
    """, unsafe_allow_html=True)

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
