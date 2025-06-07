# -*- coding: utf-8 -*-
"""
Script de avaliação de riscos e efeitos de enchentes no Brasil,
coleção de dados, classificação de risco, impactos e sugestões de soluções.

Autores:
 - Murilo Mendes Marques (RM: 564193)
 - Enzo Ramos Condomitti (RM: 565832)
 - Lucca Santos (RM: 563961)
"""

# Banco de usuários (usuário: senha)
banco_de_dados = {
    'Murilo': '1234@senha',
    'Enzo': 'kazoperdido5',
    'Suricato': 'ohomemperdido39'
}

# Lista de áreas cadastradas
banco_de_dados_areas_cadastradas = ['paulista']


def checa_credenciais(dados):
    """
    Valida usuário e senha.
    Parâmetros:
      dados (dict): mapeia nome de usuário para senha.
    Retorna:
      usuario (str) logado com sucesso.
    """
    while True:
        usuario = input("Coloque o seu usuário: ")
        senha = input("Coloque a sua senha: ")
        if usuario in dados and dados[usuario] == senha:
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario}.\n")
            return usuario
        print("Erro! Usuário ou senha incorretos. Tente novamente.\n")


def coleta_texto_nao_vazio(prompt):
    """
    Solicita uma string não vazia.
    """
    while True:
        texto = input(f"{prompt}: ").strip()
        if texto:
            return texto
        print("Entrada inválida. Não pode ser vazio.")


def cadastro_area(dados, nova_area):
    """
    Adiciona uma nova área à lista, se não existir.
    Parâmetros:
      dados (list): lista de áreas cadastradas.
      nova_area (str): nome da área a adicionar.
    """
    if nova_area not in dados:
        dados.append(nova_area)
        print(f"A área '{nova_area}' foi adicionada com sucesso.")
    else:
        print(f"A área '{nova_area}' já está cadastrada.")


def loop_cadastro_areas():
    """
    Permite ao usuário cadastrar várias áreas em sequência.
    """
    while True:
        resp = input("\nDeseja adicionar outra área? (sim/não): ").strip().lower()
        if resp == "sim":
            nova = coleta_texto_nao_vazio("Digite o nome da nova área")
            cadastro_area(banco_de_dados_areas_cadastradas, nova)
        elif resp == "não":
            print("Encerrando cadastro de áreas.\n")
            break
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")


def remover_area(dados):
    """
    Remove uma área existente da lista, se existir.
    Parâmetros:
      dados (list): lista de áreas cadastradas.
    """
    if not dados:
        print("Não há áreas cadastradas para remover.")
        return
    print("Áreas cadastradas:", ", ".join(dados))
    alvo = input("Digite o nome da área que deseja remover: ").strip()
    if alvo in dados:
        dados.remove(alvo)
        print(f"A área '{alvo}' foi removida com sucesso.\n")
    else:
        print(f"A área '{alvo}' não está cadastrada.\n")


def coleta_numero(prompt, minimo=0, maximo=100):
    """
    Solicita ao usuário um número inteiro dentro de um intervalo e valida.
    Parâmetros:
      prompt (str): texto a exibir.
      minimo (int): valor mínimo aceitável.
      maximo (int): valor máximo aceitável.
    Retorna:
      valor (int) válido.
    """
    while True:
        try:
            valor = int(input(f"{prompt} ({minimo}-{maximo}): "))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def classificar_risco(volume, saturacao):
    """
    Classifica o risco de enchente com base na média de volume e saturação.
    Retorna: 'Baixo', 'Médio' ou 'Alto'.
    """
    media = (volume + saturacao) / 2
    if media >= 70:
        return "Alto"
    if media >= 40:
        return "Médio"
    return "Baixo"


def coletar_dados_enchente(area):
    """
    Coleta os dados de enchente para uma área específica.
    Retorna: dict com volume, saturação e risco.
    """
    print(f"\n--- Coleta de dados para área: {area} ---")
    vol = coleta_numero("Informe o volume de água (%)")
    sat = coleta_numero("Informe a saturação do solo (%)")
    risco = classificar_risco(vol, sat)
    return {'volume': vol, 'saturacao': sat, 'risco': risco}


def coletar_efeitos_enchente(area):
    """
    Coleta dados sobre os efeitos da enchente em uma área.
    Retorna: dict com residências afetadas, desalojados e perdas estimadas.
    """
    print(f"\n--- Coleta de efeitos para área: {area} ---")
    residencias = coleta_numero("Residências afetadas", 0, 10000)
    desalojados = coleta_numero("Pessoas desalojadas", 0, 10000)
    perdas = coleta_numero("Perdas financeiras estimadas (em mil R$)", 0, 100000)
    return {
        'residencias': residencias,
        'desalojados': desalojados,
        'perdas_estimadas': perdas
    }


def sugerir_medidas(risco):
    """
    Sugere medidas de mitigação com base no nível de risco.
    Retorna: lista de strings.
    """
    if risco == "Alto":
        return [
            "Evacuar imediatamente as áreas de maior risco.",
            "Instalar barreiras temporárias (sacos de areia).",
            "Desobstruir bueiros e valetas."
        ]
    if risco == "Médio":
        return [
            "Manter vigilância constante e equipe de prontidão.",
            "Distribuir sacos de areia nas áreas críticas.",
            "Monitorar boletins meteorológicos."
        ]
    return [
        "Continuar o monitoramento regular.",
        "Realizar manutenção preventiva em sistemas de drenagem.",
        "Educar a comunidade sobre sinais de alerta."
    ]


def exibir_relatorio(area, dados, efeitos, medidas):
    """
    Exibe um relatório claro sobre os dados e efeitos da enchente, mais as medidas sugeridas.
    """
    print(f"\n===== Relatório: {area.upper()} =====")
    print(f"Volume de água:       {dados['volume']}%")
    print(f"Saturação do solo:    {dados['saturacao']}%")
    print(f"Classificação de risco: {dados['risco']}")
    print("\n-- Efeitos Observados --")
    print(f"Residências afetadas:  {efeitos['residencias']}")
    print(f"Pessoas desalojadas:   {efeitos['desalojados']}")
    print(f"Perdas financeiras:    R$ {efeitos['perdas_estimadas']*1000:.2f}")
    print("\n-- Medidas Sugeridas --")
    for m in medidas:
        print(f"• {m}")
    print("=" * 40)


def main():
    # 1. Autenticação
    checa_credenciais(banco_de_dados)

    # 2. Cadastro de áreas
    primeira = coleta_texto_nao_vazio("Digite uma nova área para cadastrar")
    cadastro_area(banco_de_dados_areas_cadastradas, primeira)
    loop_cadastro_areas()
    if input("Deseja remover alguma área? (sim/não): ").strip().lower() == "sim":
        remover_area(banco_de_dados_areas_cadastradas)

    # 3. Coleta e relatório
    dados_enchentes = {}
    for area in banco_de_dados_areas_cadastradas:
        dados = coletar_dados_enchente(area)
        efeitos = coletar_efeitos_enchente(area)
        medidas = sugerir_medidas(dados['risco'])
        exibir_relatorio(area, dados, efeitos, medidas)


if __name__ == "__main__":
    main()