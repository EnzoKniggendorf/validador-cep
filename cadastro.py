import pandas as pd
import unicodedata

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def carregar_faixas_cep(arquivo_excel):
    df = pd.read_excel(arquivo_excel)
    faixas_cep = {}

    for _, row in df.iterrows():
        cidade = remover_acentos(row["LOCALIDADE_SEM_ACENTOS"])
        cep_inicial = int(str(row["CEP_INICIAL"]).replace("-", "").replace(".", ""))
        cep_final = int(str(row["CEP_FINAL"]).replace("-", "").replace(".", ""))
        faixas_cep[cidade] = (cep_inicial, cep_final)

    return faixas_cep

def validar_cep(cep, cidade, faixas_cep):
    cep_numerico = int(cep.replace("-", "").replace(".", ""))
    cidade_normalizada = remover_acentos(cidade)

    if cidade_normalizada in faixas_cep:
        faixa_min, faixa_max = faixas_cep[cidade_normalizada]
        return faixa_min <= cep_numerico <= faixa_max

    return False

if __name__ == "__main__":
    arquivo_excel = "ceps.xlsx"
    faixas_cep = carregar_faixas_cep(arquivo_excel)

    cep = input("Digite o CEP: ")
    cidade = input("Digite a cidade: ")

    if validar_cep(cep, cidade, faixas_cep):
        print("CEP válido para a cidade informada.")
    else:
        print("CEP inválido para a cidade informada.")
