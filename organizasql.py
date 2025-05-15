import os
import shutil
from datetime import datetime
import calendar

# Caminho da pasta onde estão os arquivos SQL salvos com nomes aleatórios
origem = r'C:\Test\Test'

# Caminho base da estrutura organizada por ano e mês
destino_base = r'C:\Test\Test'

# Função para obter a data de criação do arquivo
def get_data_criacao(caminho_arquivo):
    timestamp = os.path.getctime(caminho_arquivo)
    return datetime.fromtimestamp(timestamp)

# Função para organizar arquivos
def organizar_arquivos():
    for arquivo in os.listdir(origem):
        if arquivo.endswith('.sql'):
            caminho_arquivo = os.path.join(origem, arquivo)
            data_criacao = get_data_criacao(caminho_arquivo)

            # Extrair dia, mês e ano
            dia = data_criacao.day
            mes = data_criacao.month
            ano = data_criacao.year

            # Nome do mês por extenso, ex: "Março"
            nome_mes = calendar.month_name[mes].capitalize()

            # Formatar nome novo do arquivo
            novo_nome = f"{dia:02d}-{mes:02d}-{ano}.sql"

            # Pasta destino: ANO/MÊS
            pasta_destino = os.path.join(destino_base, str(ano), nome_mes)

            # Criar pastas se não existirem
            os.makedirs(pasta_destino, exist_ok=True)

            # Caminho final do arquivo
            novo_caminho = os.path.join(pasta_destino, novo_nome)

            # Se já existir, renomeia com sufixo
            contador = 1
            while os.path.exists(novo_caminho):
                novo_nome = f"{dia:02d}-{mes:02d}-{ano}_{contador}.sql"
                novo_caminho = os.path.join(pasta_destino, novo_nome)
                contador += 1

            # Mover e renomear
            shutil.move(caminho_arquivo, novo_caminho)
            print(f"Arquivo '{arquivo}' movido para '{novo_caminho}'")

# Executar função
organizar_arquivos()