# -*- coding: utf-8 -*-
"""
Script de avaliação de riscos e efeitos de enchentes no Brasil,
coleção de dados, classificação de risco, impactos e sugestões de soluções.

Autores:
 - Murilo Mendes Marques (RM: 564193)
 - Enzo Ramos Condomitti (RM: 565832)
 - Lucca Santos (RM: 563961)
"""

# banco de usuários, acho que é pra garantir que só quem tem login acessa
banco_de_dados = {
    'Murilo': '1234@senha',  # usuário Murilo com senha simples
    'Enzo': 'kazoperdido5',   # senha meio perdida
    'Suricato': 'ohomemperdido39'  # não lembro de onde veio esse nome
}

# lista das áreas que a gente vai monitorar, por enquanto só paulista
banco_de_dados_areas_cadastradas = ['paulista']


def checa_credenciais(dados):
    """
    Valida usuário e senha.
    """
    # começo do loop infinito até acertar
    while True:
        usuario = input("Coloque o seu usuário: ")  # pede o nome
        senha = input("Coloque a sua senha: ")        # pede a senha
        # verifica se o par usuário:senha está no banco
        if usuario in dados and dados[usuario] == senha:
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario}.\n")
            return usuario  # sai quando estiver certo
        # se não passar, mostra erro e repete
        print("Erro! Usuário ou senha incorretos. Tente novamente.\n")


def coleta_texto_nao_vazio(prompt):
    """
    Solicita uma string não vazia.
    """
    # loop até usuário digitar algo que não seja vazio
    while True:
        texto = input(f"{prompt}: ").strip()  # tira espaço
        if texto:
            return texto  # retorna texto válido
        # aviso simples sobre erro de vazio
        print("Entrada inválida. Não pode ser vazio.")


def cadastro_area(dados, nova_area):
    """
    Adiciona uma nova área à lista, se não existir.
    """
    # verifica se área já existe antes de adicionar
    if nova_area not in dados:
        dados.append(nova_area)
        print(f"A área '{nova_area}' foi adicionada com sucesso.")
    else:
        # se já tiver, avisa pro usuário
        print(f"A área '{nova_area}' já está cadastrada.")


def loop_cadastro_areas():
    """
    Permite ao usuário cadastrar várias áreas em sequência.
    """
    # entra em loop perguntando se quer cadastrar mais
    while True:
        resp = input("\nDeseja adicionar outra área? (sim/não): ").strip().lower()
        if resp == "sim":
            # coleta texto não vazio para a nova área
            nova = coleta_texto_nao_vazio("Digite o nome da nova área")
            cadastro_area(banco_de_dados_areas_cadastradas, nova)
        elif resp == "não":
            # encerra o loop de cadastro
            print("Encerrando cadastro de áreas.\n")
            break
        else:
            # qualquer outra resposta é inválida
            print("Resposta inválida. Digite 'sim' ou 'não'.")


def remover_area(dados):
    """
    Remove uma área existente da lista, se existir.
    """
    # se não houver nada, avisa e sai
    if not dados:
        print("Não há áreas cadastradas para remover.")
        return
    # mostra as áreas atuais
    print("Áreas cadastradas:", ", ".join(dados))
    alvo = input("Digite o nome da área que deseja remover: ").strip()
    # checa se a área está na lista
    if alvo in dados:
        dados.remove(alvo)
        print(f"A área '{alvo}' foi removida com sucesso.\n")
    else:
        # avisa que não encontrou
        print(f"A área '{alvo}' não está cadastrada.\n")


def coleta_numero(prompt, minimo=0, maximo=100):
    """
    Solicita um número inteiro dentro de um intervalo e valida.
    """
    # loop até pegar número válido
    while True:
        try:
            valor = int(input(f"{prompt} ({minimo}-{maximo}): "))  # converte pra int
            if minimo <= valor <= maximo:
                return valor  # retorna se ok
            # se estiver fora do intervalo, avisa
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            # se não for número, informa
            print("Entrada inválida. Digite um número inteiro.")


def classificar_risco(volume, saturacao):
    """
    Classifica o risco de enchente com base na média de volume e saturação.
    """
    # calcula média meio tosca
    media = (volume + saturacao) / 2
    # decide o nível de risco
    if media >= 70:
        return "Alto"
    if media >= 40:
        return "Médio"
    return "Baixo"


def coletar_dados_enchente(area):
    """
    Coleta os dados de enchente para uma área específica.
    """
    print(f"\n--- Coleta de dados para área: {area} ---")
    vol = coleta_numero("Informe o volume de água (%)")  # volume em %
    sat = coleta_numero("Informe a saturação do solo (%)")  # saturação em %
    risco = classificar_risco(vol, sat)  # chama classificação
    return {'volume': vol, 'saturacao': sat, 'risco': risco}


def coletar_efeitos_enchente(area):
    """
    Coleta dados sobre os efeitos da enchente em uma área.
    """
    print(f"\n--- Coleta de efeitos para área: {area} ---")
    residencias = coleta_numero("Residências afetadas", 0, 10000)  # casas
    desalojados = coleta_numero("Pessoas desalojadas", 0, 10000)  # pessoas
    perdas = coleta_numero("Perdas financeiras estimadas (em mil R$)", 0, 100000)  # valor em mil
    return {
        'residencias': residencias,
        'desalojados': desalojados,
        'perdas_estimadas': perdas
    }


def sugerir_medidas(risco):
    """
    Sugere medidas de mitigação com base no nível de risco.
    """
    # retorna lista de ações dependendo do risco
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
    # risco baixo
    return [
        "Continuar o monitoramento regular.",
        "Realizar manutenção preventiva em sistemas de drenagem.",
        "Educar a comunidade sobre sinais de alerta."
    ]


def exibir_relatorio(area, dados, efeitos, medidas):
    """
    Exibe relatório claro sobre dados, efeitos e medidas.
    """
    print(f"\n===== Relatório: {area.upper()} =====")
    # mostra dados básicos
    print(f"Volume de água:       {dados['volume']}%")
    print(f"Saturação do solo:    {dados['saturacao']}%")
    print(f"Classificação de risco: {dados['risco']}")
    print("\n-- Efeitos Observados --")
    # efeitos da enchente
    print(f"Residências afetadas:  {efeitos['residencias']}")
    print(f"Pessoas desalojadas:   {efeitos['desalojados']}")
    # converte mil R$ pra R$
    print(f"Perdas financeiras:    R$ {efeitos['perdas_estimadas']*1000:.2f}")
    print("\n-- Medidas Sugeridas --")
    for m in medidas:
        # lista de sugestões
        print(f"• {m}")
    print("=" * 40)


def main():
    # 1. Autenticação do usuário
    checa_credenciais(banco_de_dados)

    # 2. Cadastro de áreas iniciais
    primeira = coleta_texto_nao_vazio("Digite uma nova área para cadastrar")
    cadastro_area(banco_de_dados_areas_cadastradas, primeira)
    loop_cadastro_areas()
    # opção de remoção
    if input("Deseja remover alguma área? (sim/não): ").strip().lower() == "sim":
        remover_area(banco_de_dados_areas_cadastradas)

    # 3. Coleta de dados e geração de relatórios
    dados_enchentes = {}
    for area in banco_de_dados_areas_cadastradas:
        # coleta cada parte e depois exibe
        dados = coletar_dados_enchente(area)
        efeitos = coletar_efeitos_enchente(area)
        medidas = sugerir_medidas(dados['risco'])
        exibir_relatorio(area, dados, efeitos, medidas)


if __name__ == "__main__":
    # executa tudo
    main()