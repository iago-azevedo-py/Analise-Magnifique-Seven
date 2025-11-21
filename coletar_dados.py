import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

def coletar_dados():
    """
    Coleta dados diários do mercado financeiro de 01/01/2022 a 31/12/2024
    """
    print("🚀 Iniciando coleta de dados...")
    
    # Definir período
    data_inicio = "2022-01-01"
    data_fim = "2024-12-31"
    
    # Tickers a serem coletados
    tickers_acoes = {
        'SP500': '^GSPC',
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Alphabet': 'GOOGL',
        'Amazon': 'AMZN',
        'Nvidia': 'NVDA',
        'Tesla': 'TSLA',
        'Meta': 'META'
    }
    
    tickers_indices = {
        'VIX': '^VIX',
        'Taxa_Juros_10Y': '^TNX'
    }
    
    # Coletar preços de fechamento ajustados
    print("\n📊 Coletando preços de fechamento ajustados...")
    dados_precos = {}
    
    for nome, ticker in tickers_acoes.items():
        print(f"  • {nome} ({ticker})...", end=" ")
        try:
            dados = yf.download(ticker, start=data_inicio, end=data_fim, progress=False, auto_adjust=False)
            if isinstance(dados.columns, pd.MultiIndex):
                dados_precos[nome] = dados['Adj Close'].iloc[:, 0]
            else:
                dados_precos[nome] = dados['Adj Close']
            print("✓")
        except Exception as e:
            print(f"✗ Erro: {e}")
    
    # Coletar VIX e Taxa de Juros
    print("\n📉 Coletando índices adicionais...")
    for nome, ticker in tickers_indices.items():
        print(f"  • {nome} ({ticker})...", end=" ")
        try:
            dados = yf.download(ticker, start=data_inicio, end=data_fim, progress=False, auto_adjust=False)
            if isinstance(dados.columns, pd.MultiIndex):
                dados_precos[nome] = dados['Close'].iloc[:, 0]
            else:
                dados_precos[nome] = dados['Close']
            print("✓")
        except Exception as e:
            print(f"✗ Erro: {e}")
    
    # Criar DataFrame consolidado
    df_precos = pd.DataFrame(dados_precos)
    df_precos.index.name = 'Data'
    
    # Remover linhas com valores ausentes
    df_precos = df_precos.dropna()
    
    print(f"\n✅ Dados coletados: {len(df_precos)} dias de negociação")
    print(f"📅 Período: {df_precos.index.min().date()} a {df_precos.index.max().date()}")
    
    return df_precos


def calcular_retornos_logaritmicos(df_precos):
    """
    Calcula retornos logarítmicos para todas as séries de preços
    """
    print("\n🔢 Calculando retornos logarítmicos...")
    
    colunas_acoes = ['SP500', 'Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Nvidia', 'Tesla', 'Meta']
    
    df_retornos = pd.DataFrame(index=df_precos.index)
    
    for coluna in colunas_acoes:
        if coluna in df_precos.columns:
            df_retornos[f'Retorno_{coluna}'] = np.log(df_precos[coluna] / df_precos[coluna].shift(1))
            print(f"  ✓ {coluna}")
    
    # Manter VIX e Taxa de Juros como valores absolutos
    df_retornos['VIX'] = df_precos['VIX']
    df_retornos['Taxa_Juros_10Y'] = df_precos['Taxa_Juros_10Y']
    
    # Remover primeira linha (NaN devido ao shift)
    df_retornos = df_retornos.dropna()
    
    print(f"✅ Retornos calculados para {len(df_retornos)} observações")
    
    return df_retornos


def coletar_market_cap():
    """
    Coleta dados de market cap das Magnificent Seven
    """
    print("\n💰 Coletando dados de capitalização de mercado...")
    
    tickers_mag7 = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META']
    nomes_mag7 = ['Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Nvidia', 'Tesla', 'Meta']
    
    data_inicio = "2022-01-01"
    data_fim = "2024-12-31"
    
    market_caps = {}
    
    for nome, ticker in zip(nomes_mag7, tickers_mag7):
        print(f"  • {nome} ({ticker})...", end=" ")
        try:
            dados = yf.download(ticker, start=data_inicio, end=data_fim, progress=False)
            # Market Cap = Preço * Shares Outstanding
            # Vamos usar o preço de fechamento ajustado como proxy
            market_caps[nome] = dados['Adj Close'] * dados['Volume']
            print("✓")
        except Exception as e:
            print(f"✗ Erro: {e}")
    
    df_market_cap = pd.DataFrame(market_caps)
    df_market_cap = df_market_cap.dropna()
    
    print(f"✅ Market caps coletados para {len(df_market_cap)} dias")
    
    return df_market_cap


def construir_big_tech_index(df_precos, df_retornos):
    """
    Constrói o Big Tech Index ponderado por capitalização de mercado
    """
    print("\n🏗️ Construindo Big Tech Index...")
    
    mag7_empresas = ['Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Nvidia', 'Tesla', 'Meta']
    
    # Método simplificado: usar preços como proxy para market cap
    # Em produção, seria necessário dados de shares outstanding
    print("  ℹ️ Usando preços como proxy para capitalização de mercado")
    
    # Calcular pesos diários baseados nos preços
    df_pesos = pd.DataFrame(index=df_precos.index)
    
    for empresa in mag7_empresas:
        if empresa in df_precos.columns:
            df_pesos[empresa] = df_precos[empresa]
    
    # Normalizar pesos (soma = 1 para cada dia)
    df_pesos = df_pesos.div(df_pesos.sum(axis=1), axis=0)
    
    # Calcular retorno ponderado do Big Tech Index
    retornos_mag7 = []
    for empresa in mag7_empresas:
        col_retorno = f'Retorno_{empresa}'
        if col_retorno in df_retornos.columns:
            retornos_mag7.append(col_retorno)
    
    # Alinhar índices
    df_pesos_alinhado = df_pesos.loc[df_retornos.index]
    
    # Calcular retorno ponderado
    retorno_bigtech = pd.Series(0.0, index=df_retornos.index)
    
    for i, empresa in enumerate(mag7_empresas):
        col_retorno = f'Retorno_{empresa}'
        if col_retorno in df_retornos.columns and empresa in df_pesos_alinhado.columns:
            retorno_bigtech += df_pesos_alinhado[empresa] * df_retornos[col_retorno]
    
    df_retornos['Retorno_BigTech_Index'] = retorno_bigtech
    
    print(f"✅ Big Tech Index construído com sucesso")
    print(f"  📊 Retorno médio diário: {retorno_bigtech.mean():.6f}")
    print(f"  📊 Volatilidade: {retorno_bigtech.std():.6f}")
    
    return df_retornos, df_pesos


def preparar_dataframe_final(df_retornos):
    """
    Prepara DataFrame final com nomenclatura padronizada
    """
    print("\n📋 Preparando DataFrame Final...")
    
    df_final = pd.DataFrame({
        'data': df_retornos.index,
        'retorno_sp500': df_retornos['Retorno_SP500'],
        'retorno_bigtech': df_retornos['Retorno_BigTech_Index'],
        'vix': df_retornos['VIX'],
        'taxa_juros_10y': df_retornos['Taxa_Juros_10Y']
    })
    
    df_final.set_index('data', inplace=True)
    
    print(f"✅ DataFrame final preparado com {len(df_final)} observações")
    print(f"  Colunas: {list(df_final.columns)}")
    
    return df_final


def gerar_estatisticas_descritivas(df_retornos):
    """
    Gera estatísticas descritivas dos dados
    """
    print("\n📈 Estatísticas Descritivas:")
    print("="*80)
    
    colunas_principais = ['Retorno_SP500', 'Retorno_BigTech_Index', 'VIX', 'Taxa_Juros_10Y']
    
    stats = df_retornos[colunas_principais].describe()
    print(stats)
    
    print("\n📊 Correlações:")
    print("="*80)
    corr = df_retornos[colunas_principais].corr()
    print(corr)
    
    return stats, corr


def salvar_dados(df_precos, df_retornos, df_pesos, df_final):
    """
    Salva os dados processados em arquivos CSV
    """
    print("\n💾 Salvando dados processados...")
    
    df_precos.to_csv('dados_precos.csv')
    print("  ✓ dados_precos.csv")
    
    df_retornos.to_csv('dados_retornos.csv')
    print("  ✓ dados_retornos.csv")
    
    df_pesos.to_csv('dados_pesos_bigtech.csv')
    print("  ✓ dados_pesos_bigtech.csv")
    
    df_final.to_csv('dados_final.csv')
    print("  ✓ dados_final.csv")
    
    print("\n✅ Todos os dados foram salvos com sucesso!")


def main():
    """
    Função principal para executar todo o pipeline de coleta e processamento
    """
    print("="*80)
    print("  COLETA E PROCESSAMENTO DE DADOS - MAGNIFICENT SEVEN")
    print("="*80)
    
    # Passo 1: Coletar dados
    df_precos = coletar_dados()
    
    # Passo 2: Calcular retornos logarítmicos
    df_retornos = calcular_retornos_logaritmicos(df_precos)
    
    # Passo 3: Construir Big Tech Index
    df_retornos, df_pesos = construir_big_tech_index(df_precos, df_retornos)
    
    # Passo 4: Preparar DataFrame final
    df_final = preparar_dataframe_final(df_retornos)
    
    # Passo 5: Gerar estatísticas descritivas
    stats, corr = gerar_estatisticas_descritivas(df_retornos)
    
    # Passo 6: Salvar dados
    salvar_dados(df_precos, df_retornos, df_pesos, df_final)
    
    print("\n" + "="*80)
    print("  ✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO!")
    print("="*80)
    
    return df_precos, df_retornos, df_pesos, df_final, stats, corr


if __name__ == "__main__":
    df_precos, df_retornos, df_pesos, df_final, stats, corr = main()
