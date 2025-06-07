
banco_de_dados = {
    'Murilo': '1234@senha',
    'Enzo': 'kazoperdido5',
    'Suricato': 'ohomemperdido39'
}

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
        else:
            print("Erro! Usuário ou senha incorretos. Tente novamente.\n")


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
        resposta = input("\nDeseja adicionar outra área? (sim/não): ").strip().lower()
        if resposta == "sim":
            nova = input("Digite o nome da nova área: ").strip()
            cadastro_area(banco_de_dados_areas_cadastradas, nova)
        elif resposta == "não":
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
            else:
                print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def classificar_risco(volume, saturacao):
    """
    Classifica o risco de enchente com base na média de volume e saturação.
    Parâmetros:
      volume (int): percentual de volume de água.
      saturacao (int): percentual de saturação do solo.
    Retorna:
      risco (str): 'Baixo', 'Médio' ou 'Alto'.
    """
    media = (volume + saturacao) / 2
    if media >= 70:
        return "Alto"
    elif media >= 40:
        return "Médio"
    else:
        return "Baixo"


def coletar_dados_enchente(area):
    """
    Coleta os dados de enchente para uma área específica.
    Parâmetros:
      area (str): nome da área.
    Retorna:
      dict: {'volume': int, 'saturacao': int, 'risco': str}
    """
    print(f"\n--- Coleta de dados para área: {area} ---")
    vol = coleta_numero("Informe o volume de água (%)")
    sat = coleta_numero("Informe a saturação do solo (%)")
    risco = classificar_risco(vol, sat)
    return {'volume': vol, 'saturacao': sat, 'risco': risco}


def exibir_relatorio(area, dados):
    """
    Exibe um relatório claro sobre os dados de enchente de uma área.
    Parâmetros:
      area (str): nome da área.
      dados (dict): saída de coletar_dados_enchente.
    """
    print(f"\n===== Relatório de Enchentes: {area.upper()} =====")
    print(f"Volume de água:       {dados['volume']}%")
    print(f"Saturação do solo:    {dados['saturacao']}%")
    print(f"Classificação de risco: {dados['risco']}")
    print("=" * 40)


def main():
    checa_credenciais(banco_de_dados)

    cadastro_area(banco_de_dados_areas_cadastradas,
                  input("Digite uma nova área para cadastrar: ").strip())
    loop_cadastro_areas()

    if input("Deseja remover alguma área? (sim/não): ").strip().lower() == "sim":
        remover_area(banco_de_dados_areas_cadastradas)

    dados_enchentes = {}
    for area in banco_de_dados_areas_cadastradas:
        dados_enchentes[area] = coletar_dados_enchente(area)

    for area, dados in dados_enchentes.items():
        exibir_relatorio(area, dados)


if __name__ == "__main__":
    main()