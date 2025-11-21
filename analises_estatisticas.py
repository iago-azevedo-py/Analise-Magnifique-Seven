"""
Análises Estatísticas Avançadas
Implementa todas as análises estatísticas solicitadas
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
from statsmodels.formula.api import ols


def carregar_dados_final():
    """Carrega o DataFrame final processado"""
    try:
        df = pd.read_csv('dados_final.csv', index_col=0, parse_dates=True)
        return df
    except FileNotFoundError:
        print("❌ Arquivo dados_final.csv não encontrado!")
        print("Execute primeiro: python coletar_dados.py")
        return None


def estatisticas_descritivas_completas(df):
    """
    4.1 Estatísticas Descritivas Completas
    """
    print("\n" + "="*80)
    print("  📊 ESTATÍSTICAS DESCRITIVAS COMPLETAS")
    print("="*80)
    
    stats_dict = {}
    
    for col in df.columns:
        stats_dict[col] = {
            'Média': df[col].mean(),
            'Mediana': df[col].median(),
            'Desvio Padrão': df[col].std(),
            'Mínimo': df[col].min(),
            'Máximo': df[col].max(),
            'Q1 (25%)': df[col].quantile(0.25),
            'Q3 (75%)': df[col].quantile(0.75),
            'IQR': df[col].quantile(0.75) - df[col].quantile(0.25),
            'Assimetria': df[col].skew(),
            'Curtose': df[col].kurtosis()
        }
    
    df_stats = pd.DataFrame(stats_dict).T
    print(df_stats.round(6))
    
    return df_stats


def identificar_outliers(df):
    """
    4.2 Identificação de Outliers usando método IQR
    """
    print("\n" + "="*80)
    print("  🔍 IDENTIFICAÇÃO DE OUTLIERS (Método IQR)")
    print("="*80)
    
    outliers_info = {}
    df_sem_outliers = df.copy()
    
    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        # Identificar outliers
        outliers_mask = (df[col] < limite_inferior) | (df[col] > limite_superior)
        outliers = df[outliers_mask][col]
        
        outliers_info[col] = {
            'Q1': Q1,
            'Q3': Q3,
            'IQR': IQR,
            'Limite Inferior': limite_inferior,
            'Limite Superior': limite_superior,
            'Número de Outliers': len(outliers),
            'Porcentagem': (len(outliers) / len(df)) * 100,
            'Outliers': outliers.to_dict()
        }
        
        print(f"\n📊 {col}:")
        print(f"  • IQR: {IQR:.6f}")
        print(f"  • Limites: [{limite_inferior:.6f}, {limite_superior:.6f}]")
        print(f"  • Outliers encontrados: {len(outliers)} ({outliers_info[col]['Porcentagem']:.2f}%)")
        
        # Remover outliers do dataset
        df_sem_outliers = df_sem_outliers[~outliers_mask]
    
    print(f"\n✅ Dataset original: {len(df)} observações")
    print(f"✅ Dataset sem outliers: {len(df_sem_outliers)} observações")
    print(f"📉 Outliers removidos: {len(df) - len(df_sem_outliers)} ({((len(df) - len(df_sem_outliers)) / len(df)) * 100:.2f}%)")
    
    # Salvar dataset sem outliers
    df_sem_outliers.to_csv('dados_final_sem_outliers.csv')
    print("\n💾 Dataset sem outliers salvo em: dados_final_sem_outliers.csv")
    
    return outliers_info, df_sem_outliers


def calcular_erro_amostral(df):
    """
    4.3 Cálculo de Erro Amostral
    """
    print("\n" + "="*80)
    print("  📏 ERRO AMOSTRAL (Confiança 95%)")
    print("="*80)
    
    n = len(df)
    z_score = 1.96  # Para 95% de confiança
    
    erro_info = {}
    
    for col in df.columns:
        std = df[col].std()
        se = std / np.sqrt(n)
        me = z_score * se
        
        erro_info[col] = {
            'Desvio Padrão': std,
            'Erro Padrão (SE)': se,
            'Margem de Erro (ME)': me,
            'Intervalo de Confiança Inferior': df[col].mean() - me,
            'Intervalo de Confiança Superior': df[col].mean() + me
        }
        
        print(f"\n📊 {col}:")
        print(f"  • Erro Padrão: {se:.6f}")
        print(f"  • Margem de Erro (95%): ±{me:.6f}")
        print(f"  • IC 95%: [{erro_info[col]['Intervalo de Confiança Inferior']:.6f}, {erro_info[col]['Intervalo de Confiança Superior']:.6f}]")
    
    df_erro = pd.DataFrame(erro_info).T
    return df_erro


def matriz_correlacao_detalhada(df):
    """
    4.5 Matriz de Correlação Detalhada
    """
    print("\n" + "="*80)
    print("  🔗 MATRIZ DE CORRELAÇÃO (Pearson)")
    print("="*80)
    
    # Calcular correlação
    corr_matrix = df.corr()
    
    print("\nMatriz de Correlação:")
    print(corr_matrix.round(4))
    
    # Identificar correlações significativas
    print("\n📌 Correlações Significativas (|r| > 0.5):")
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            corr_val = corr_matrix.iloc[i, j]
            if abs(corr_val) > 0.5:
                var1 = corr_matrix.columns[i]
                var2 = corr_matrix.columns[j]
                print(f"  • {var1} ↔ {var2}: {corr_val:.4f}")
    
    return corr_matrix


def criar_boxplots(df, outliers_info):
    """
    Cria boxplots para visualização de outliers
    """
    print("\n📊 Gerando boxplots...")
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=list(df.columns),
        vertical_spacing=0.15,
        horizontal_spacing=0.12
    )
    
    positions = [(1, 1), (1, 2), (2, 1), (2, 2)]
    
    for idx, col in enumerate(df.columns):
        row, col_pos = positions[idx]
        
        fig.add_trace(
            go.Box(
                y=df[col],
                name=col,
                boxmean='sd',
                marker_color='lightblue'
            ),
            row=row, col=col_pos
        )
    
    fig.update_layout(
        title_text="Boxplots - Identificação de Outliers",
        showlegend=False,
        height=800
    )
    
    fig.write_html('boxplots_outliers.html')
    print("✅ Boxplots salvos em: boxplots_outliers.html")
    
    return fig


def criar_heatmap_correlacao(corr_matrix):
    """
    Cria heatmap da matriz de correlação
    """
    print("\n🎨 Gerando heatmap de correlação...")
    
    fig = px.imshow(
        corr_matrix,
        text_auto='.3f',
        color_continuous_scale='RdBu_r',
        aspect='auto',
        title='Matriz de Correlação de Pearson',
        labels=dict(color="Correlação")
    )
    
    fig.update_layout(
        width=800,
        height=700
    )
    
    fig.write_html('heatmap_correlacao.html')
    print("✅ Heatmap salvo em: heatmap_correlacao.html")
    
    return fig


def regressao_linear_multipla(df):
    """
    4.6 Regressão Linear Múltipla
    
    Modelo 1: retorno_sp500 = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε
    Modelo 2: vix = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε
    """
    print("\n" + "="*80)
    print("  📈 REGRESSÃO LINEAR MÚLTIPLA")
    print("="*80)
    
    resultados = {}
    
    # Modelo 1: Retorno S&P 500
    print("\n📊 MODELO 1: Retorno S&P 500")
    print("  Equação: retorno_sp500 = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε")
    
    modelo1 = ols('retorno_sp500 ~ retorno_bigtech + taxa_juros_10y', data=df).fit()
    
    print(f"\n  Coeficientes:")
    print(f"    β₀ (Intercepto): {modelo1.params['Intercept']:.6f}")
    print(f"    β₁ (retorno_bigtech): {modelo1.params['retorno_bigtech']:.6f}")
    print(f"    β₂ (taxa_juros_10y): {modelo1.params['taxa_juros_10y']:.6f}")
    
    print(f"\n  Erro Padrão:")
    print(f"    SE(β₀): {modelo1.bse['Intercept']:.6f}")
    print(f"    SE(β₁): {modelo1.bse['retorno_bigtech']:.6f}")
    print(f"    SE(β₂): {modelo1.bse['taxa_juros_10y']:.6f}")
    
    print(f"\n  Valor-p:")
    print(f"    p(β₀): {modelo1.pvalues['Intercept']:.6f}")
    print(f"    p(β₁): {modelo1.pvalues['retorno_bigtech']:.6f} {'***' if modelo1.pvalues['retorno_bigtech'] < 0.001 else '**' if modelo1.pvalues['retorno_bigtech'] < 0.01 else '*' if modelo1.pvalues['retorno_bigtech'] < 0.05 else ''}")
    print(f"    p(β₂): {modelo1.pvalues['taxa_juros_10y']:.6f} {'***' if modelo1.pvalues['taxa_juros_10y'] < 0.001 else '**' if modelo1.pvalues['taxa_juros_10y'] < 0.01 else '*' if modelo1.pvalues['taxa_juros_10y'] < 0.05 else ''}")
    
    print(f"\n  Qualidade do Modelo:")
    print(f"    R²: {modelo1.rsquared:.4f}")
    print(f"    R² Ajustado: {modelo1.rsquared_adj:.4f}")
    print(f"    F-statistic: {modelo1.fvalue:.4f}")
    print(f"    Prob(F-statistic): {modelo1.f_pvalue:.6f} {'***' if modelo1.f_pvalue < 0.001 else '**' if modelo1.f_pvalue < 0.01 else '*' if modelo1.f_pvalue < 0.05 else ''}")
    
    resultados['modelo1'] = {
        'modelo': modelo1,
        'nome': 'Retorno S&P 500',
        'formula': 'retorno_sp500 ~ retorno_bigtech + taxa_juros_10y',
        'coeficientes': {
            'Intercepto': modelo1.params['Intercept'],
            'retorno_bigtech': modelo1.params['retorno_bigtech'],
            'taxa_juros_10y': modelo1.params['taxa_juros_10y']
        },
        'erro_padrao': {
            'Intercepto': modelo1.bse['Intercept'],
            'retorno_bigtech': modelo1.bse['retorno_bigtech'],
            'taxa_juros_10y': modelo1.bse['taxa_juros_10y']
        },
        'pvalores': {
            'Intercepto': modelo1.pvalues['Intercept'],
            'retorno_bigtech': modelo1.pvalues['retorno_bigtech'],
            'taxa_juros_10y': modelo1.pvalues['taxa_juros_10y']
        },
        'r2': modelo1.rsquared,
        'r2_adj': modelo1.rsquared_adj,
        'f_statistic': modelo1.fvalue,
        'f_pvalue': modelo1.f_pvalue
    }
    
    # Modelo 2: Volatilidade (VIX)
    print("\n\n📊 MODELO 2: Volatilidade (VIX)")
    print("  Equação: vix = β₀ + β₁*retorno_bigtech + β₂*taxa_juros_10y + ε")
    
    modelo2 = ols('vix ~ retorno_bigtech + taxa_juros_10y', data=df).fit()
    
    print(f"\n  Coeficientes:")
    print(f"    β₀ (Intercepto): {modelo2.params['Intercept']:.6f}")
    print(f"    β₁ (retorno_bigtech): {modelo2.params['retorno_bigtech']:.6f}")
    print(f"    β₂ (taxa_juros_10y): {modelo2.params['taxa_juros_10y']:.6f}")
    
    print(f"\n  Erro Padrão:")
    print(f"    SE(β₀): {modelo2.bse['Intercept']:.6f}")
    print(f"    SE(β₁): {modelo2.bse['retorno_bigtech']:.6f}")
    print(f"    SE(β₂): {modelo2.bse['taxa_juros_10y']:.6f}")
    
    print(f"\n  Valor-p:")
    print(f"    p(β₀): {modelo2.pvalues['Intercept']:.6f}")
    print(f"    p(β₁): {modelo2.pvalues['retorno_bigtech']:.6f} {'***' if modelo2.pvalues['retorno_bigtech'] < 0.001 else '**' if modelo2.pvalues['retorno_bigtech'] < 0.01 else '*' if modelo2.pvalues['retorno_bigtech'] < 0.05 else ''}")
    print(f"    p(β₂): {modelo2.pvalues['taxa_juros_10y']:.6f} {'***' if modelo2.pvalues['taxa_juros_10y'] < 0.001 else '**' if modelo2.pvalues['taxa_juros_10y'] < 0.01 else '*' if modelo2.pvalues['taxa_juros_10y'] < 0.05 else ''}")
    
    print(f"\n  Qualidade do Modelo:")
    print(f"    R²: {modelo2.rsquared:.4f}")
    print(f"    R² Ajustado: {modelo2.rsquared_adj:.4f}")
    print(f"    F-statistic: {modelo2.fvalue:.4f}")
    print(f"    Prob(F-statistic): {modelo2.f_pvalue:.6f} {'***' if modelo2.f_pvalue < 0.001 else '**' if modelo2.f_pvalue < 0.01 else '*' if modelo2.f_pvalue < 0.05 else ''}")
    
    resultados['modelo2'] = {
        'modelo': modelo2,
        'nome': 'Volatilidade (VIX)',
        'formula': 'vix ~ retorno_bigtech + taxa_juros_10y',
        'coeficientes': {
            'Intercepto': modelo2.params['Intercept'],
            'retorno_bigtech': modelo2.params['retorno_bigtech'],
            'taxa_juros_10y': modelo2.params['taxa_juros_10y']
        },
        'erro_padrao': {
            'Intercepto': modelo2.bse['Intercept'],
            'retorno_bigtech': modelo2.bse['retorno_bigtech'],
            'taxa_juros_10y': modelo2.bse['taxa_juros_10y']
        },
        'pvalores': {
            'Intercepto': modelo2.pvalues['Intercept'],
            'retorno_bigtech': modelo2.pvalues['retorno_bigtech'],
            'taxa_juros_10y': modelo2.pvalues['taxa_juros_10y']
        },
        'r2': modelo2.rsquared,
        'r2_adj': modelo2.rsquared_adj,
        'f_statistic': modelo2.fvalue,
        'f_pvalue': modelo2.f_pvalue
    }
    
    # Salvar resultados em CSV
    df_resultados = pd.DataFrame({
        'Modelo 1 (S&P 500)': [
            resultados['modelo1']['coeficientes']['Intercepto'],
            resultados['modelo1']['coeficientes']['retorno_bigtech'],
            resultados['modelo1']['coeficientes']['taxa_juros_10y'],
            resultados['modelo1']['r2'],
            resultados['modelo1']['r2_adj'],
            resultados['modelo1']['f_statistic'],
            resultados['modelo1']['f_pvalue']
        ],
        'Modelo 2 (VIX)': [
            resultados['modelo2']['coeficientes']['Intercepto'],
            resultados['modelo2']['coeficientes']['retorno_bigtech'],
            resultados['modelo2']['coeficientes']['taxa_juros_10y'],
            resultados['modelo2']['r2'],
            resultados['modelo2']['r2_adj'],
            resultados['modelo2']['f_statistic'],
            resultados['modelo2']['f_pvalue']
        ]
    }, index=['β₀ (Intercepto)', 'β₁ (retorno_bigtech)', 'β₂ (taxa_juros_10y)', 
              'R²', 'R² Ajustado', 'F-statistic', 'Prob(F)'])
    
    df_resultados.to_csv('regressao_multipla.csv')
    print("\n💾 Resultados da regressão salvos em: regressao_multipla.csv")
    
    return resultados


def criar_graficos_dispersao(df, resultados_regressao):
    """
    4.7 Gráficos de Dispersão com Linha de Regressão
    """
    print("\n" + "="*80)
    print("  📊 GRÁFICOS DE DISPERSÃO")
    print("="*80)
    
    # Gráfico 1: Retorno S&P 500 vs Retorno Big Tech
    print("\n📈 Gerando gráfico: Retorno S&P 500 vs Retorno Big Tech...")
    
    modelo1 = resultados_regressao['modelo1']['modelo']
    
    fig1 = px.scatter(
        df, 
        x='retorno_bigtech', 
        y='retorno_sp500',
        title='Modelo 1: Retorno S&P 500 vs Retorno Big Tech',
        labels={
            'retorno_bigtech': 'Retorno Big Tech Index',
            'retorno_sp500': 'Retorno S&P 500'
        },
        trendline='ols',
        trendline_color_override='red'
    )
    
    # Adicionar informações do modelo
    r2 = resultados_regressao['modelo1']['r2']
    beta = resultados_regressao['modelo1']['coeficientes']['retorno_bigtech']
    
    fig1.add_annotation(
        text=f"R² = {r2:.4f}<br>β₁ = {beta:.4f}",
        xref="paper", yref="paper",
        x=0.05, y=0.95,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1
    )
    
    fig1.update_layout(width=900, height=600)
    fig1.write_html('scatter_modelo1.html')
    print("✅ Gráfico salvo em: scatter_modelo1.html")
    
    # Gráfico 2: VIX vs Retorno Big Tech
    print("\n📈 Gerando gráfico: VIX vs Retorno Big Tech...")
    
    modelo2 = resultados_regressao['modelo2']['modelo']
    
    fig2 = px.scatter(
        df, 
        x='retorno_bigtech', 
        y='vix',
        title='Modelo 2: Volatilidade (VIX) vs Retorno Big Tech',
        labels={
            'retorno_bigtech': 'Retorno Big Tech Index',
            'vix': 'VIX (Volatilidade)'
        },
        trendline='ols',
        trendline_color_override='red'
    )
    
    # Adicionar informações do modelo
    r2 = resultados_regressao['modelo2']['r2']
    beta = resultados_regressao['modelo2']['coeficientes']['retorno_bigtech']
    
    fig2.add_annotation(
        text=f"R² = {r2:.4f}<br>β₁ = {beta:.4f}",
        xref="paper", yref="paper",
        x=0.05, y=0.95,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1
    )
    
    fig2.update_layout(width=900, height=600)
    fig2.write_html('scatter_modelo2.html')
    print("✅ Gráfico salvo em: scatter_modelo2.html")
    
    # Gráfico 3: VIX vs Taxa de Juros
    print("\n📈 Gerando gráfico: VIX vs Taxa de Juros...")
    
    fig3 = px.scatter(
        df, 
        x='taxa_juros_10y', 
        y='vix',
        title='Volatilidade (VIX) vs Taxa de Juros 10Y',
        labels={
            'taxa_juros_10y': 'Taxa de Juros 10Y (%)',
            'vix': 'VIX (Volatilidade)'
        },
        trendline='ols',
        trendline_color_override='red'
    )
    
    beta = resultados_regressao['modelo2']['coeficientes']['taxa_juros_10y']
    
    fig3.add_annotation(
        text=f"β₂ = {beta:.4f}",
        xref="paper", yref="paper",
        x=0.05, y=0.95,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1
    )
    
    fig3.update_layout(width=900, height=600)
    fig3.write_html('scatter_vix_juros.html')
    print("✅ Gráfico salvo em: scatter_vix_juros.html")
    
    return {'fig1': fig1, 'fig2': fig2, 'fig3': fig3}


def gerar_relatorio_completo():
    """
    Gera relatório completo com todas as análises
    """
    print("\n" + "="*80)
    print("  🎯 RELATÓRIO COMPLETO DE ANÁLISES ESTATÍSTICAS")
    print("="*80)
    
    # Carregar dados
    df = carregar_dados_final()
    if df is None:
        return
    
    print(f"\n📊 Dados carregados: {len(df)} observações")
    print(f"📅 Período: {df.index.min().date()} a {df.index.max().date()}")
    print(f"📋 Variáveis: {list(df.columns)}")
    
    # 4.1 Estatísticas Descritivas
    df_stats = estatisticas_descritivas_completas(df)
    df_stats.to_csv('estatisticas_descritivas.csv')
    print("\n💾 Estatísticas salvas em: estatisticas_descritivas.csv")
    
    # 4.2 Identificação de Outliers
    outliers_info, df_sem_outliers = identificar_outliers(df)
    
    # 4.3 Erro Amostral
    df_erro = calcular_erro_amostral(df)
    df_erro.to_csv('erro_amostral.csv')
    print("\n💾 Erro amostral salvo em: erro_amostral.csv")
    
    # 4.4 Matriz de Correlação
    corr_matrix = matriz_correlacao_detalhada(df)
    corr_matrix.to_csv('matriz_correlacao.csv')
    print("\n💾 Matriz de correlação salva em: matriz_correlacao.csv")
    
    # Gerar visualizações
    criar_boxplots(df, outliers_info)
    criar_heatmap_correlacao(corr_matrix)
    
    # 4.6 Regressão Linear Múltipla
    resultados_regressao = regressao_linear_multipla(df)
    
    # 4.7 Gráficos de Dispersão
    graficos = criar_graficos_dispersao(df, resultados_regressao)
    
    print("\n" + "="*80)
    print("  ✅ RELATÓRIO COMPLETO GERADO COM SUCESSO!")
    print("="*80)
    
    print("\n📁 Arquivos gerados:")
    print("  • estatisticas_descritivas.csv")
    print("  • dados_final_sem_outliers.csv")
    print("  • erro_amostral.csv")
    print("  • matriz_correlacao.csv")
    print("  • regressao_multipla.csv")
    print("  • boxplots_outliers.html")
    print("  • heatmap_correlacao.html")
    print("  • scatter_modelo1.html")
    print("  • scatter_modelo2.html")
    print("  • scatter_vix_juros.html")
    
    return {
        'stats': df_stats,
        'outliers': outliers_info,
        'df_sem_outliers': df_sem_outliers,
        'erro': df_erro,
        'correlacao': corr_matrix,
        'regressao': resultados_regressao,
        'graficos': graficos
    }


if __name__ == "__main__":
    resultados = gerar_relatorio_completo()
