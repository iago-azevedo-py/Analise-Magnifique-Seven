"""
Script de inicialização completa do projeto
Coleta dados e inicia o dashboard Streamlit
"""

import subprocess
import sys
import os

def print_header(text):
    """Imprime cabeçalho formatado"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80 + "\n")

def executar_comando(comando, descricao):
    """Executa comando e retorna resultado"""
    print(f"🔄 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"✅ {descricao} - Concluído!")
            return True
        else:
            print(f"❌ {descricao} - Erro!")
            print(resultado.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro ao executar: {e}")
        return False

def verificar_arquivos_dados():
    """Verifica se os arquivos de dados existem"""
    arquivos = ['dados_precos.csv', 'dados_retornos.csv', 'dados_pesos_bigtech.csv']
    existem = all(os.path.exists(arquivo) for arquivo in arquivos)
    return existem

def main():
    print_header("INICIALIZAÇÃO DO PROJETO - MAGNIFICENT SEVEN & S&P 500")
    
    # Verificar se os dados já foram coletados
    if verificar_arquivos_dados():
        print("ℹ️  Dados já coletados anteriormente.")
        resposta = input("Deseja recoletar os dados? (s/n): ").lower()
        
        if resposta == 's':
            print_header("ETAPA 1: COLETA E PROCESSAMENTO DE DADOS")
            if not executar_comando(
                f'"{sys.executable}" coletar_dados.py',
                "Coletando e processando dados"
            ):
                print("\n⚠️  Aviso: Falha na coleta de dados, mas continuando...")
    else:
        print("📊 Nenhum dado encontrado. Iniciando coleta...")
        print_header("ETAPA 1: COLETA E PROCESSAMENTO DE DADOS")
        
        if not executar_comando(
            f'"{sys.executable}" coletar_dados.py',
            "Coletando e processando dados"
        ):
            print("\n❌ Erro crítico na coleta de dados.")
            print("Por favor, execute manualmente: python coletar_dados.py")
            return
    
    # Iniciar Streamlit
    print_header("ETAPA 2: INICIANDO DASHBOARD STREAMLIT")
    print("🚀 Abrindo dashboard interativo...")
    print("📍 URL: http://localhost:8501")
    print("\n💡 Dica: Pressione Ctrl+C para encerrar o servidor\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n\n👋 Encerrando servidor Streamlit...")
        print("✅ Projeto finalizado com sucesso!")

if __name__ == "__main__":
    main()
