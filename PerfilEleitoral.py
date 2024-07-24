import mysql.connector;
import pandas as pd;
import matplotlib.pyplot as plt;

Tabelas = {
  "estadocivil": ["CodEstadoCivil"],
  "faixaetaria": ["CodFaixaEtaria"],
  "genero": ["CodGenero"],
  "grauescolaridade": ["CodGrau"],
  "identidadegenero": ["CodIdentidadeGenero"],
  "interpretelibras": ["CodInterprete"],
  "quilombola": ["CodQuilombola"],
  "raca": ["CodRaca"],
  "votacao": ["QtdEleitoresPerfil", "QtdEleitoresBiometria", "QtdEleitoresDeficiencia", "QtdEleitoresNomeSocial"],
};

OpcoesCamposQualitativos = {0: "CodEstadoCivil", 1: "CodFaixaEtaria", 2: "CodGenero", 3: "CodGrau", 4: "CodIdentidadeGenero", 5: "CodInterprete", 6: "CodQuilombola", 7: "CodRaca"};
OpcoesQuantidade = {0: "QtdEleitoresPerfil", 1: "QtdEleitoresBiometria", 2: "QtdEleitoresDeficiencia", 3: "QtdEleitoresNomeSocial"};

def EstabelecerConexao(pHost, pUsuario, pSenha, pBaseDados):
    conexao = mysql.connector.connect(
        host=pHost,
        user=pUsuario,
        password=pSenha,
        database=pBaseDados,
    )
    cursor = conexao.cursor()
    return conexao, cursor

def GerarConsulta(CampoLinha, CampoColuna, Cursor, QtdRequisitada = "QtdEleitoresPerfil"):
    Campos = list(Tabelas.values());
    TabelasPesquisa = [];
    i = 0;

    while (i < len(Campos)):
        if (CampoLinha in Campos[i]):
            TabelasPesquisa.insert(0, list(Tabelas.keys())[i]);

        if (CampoColuna in Campos[i]):
            TabelasPesquisa.append(list(Tabelas.keys())[i]);

        i += 1;

    ListaDict = [];

    for i, Tabela in enumerate(TabelasPesquisa):
        Dicionario = {};
        consulta1 = f"SELECT * FROM {Tabela}";
        Cursor.execute(consulta1);
        Entradas = Cursor.fetchall();

        for Entrada in Entradas:
            Dicionario[Entrada[0]] = Entrada[1];

        ListaDict.append(Dicionario);

    consulta2 = f"SELECT p.{CampoLinha}, p.{CampoColuna}, SUM({QtdRequisitada}) FROM votacao NATURAL JOIN perfil as p, {TabelasPesquisa[0]}";

    if (TabelasPesquisa[0] != TabelasPesquisa[1]):
        consulta2 += f", {TabelasPesquisa[1]} GROUP BY p.{CampoLinha}, p.{CampoColuna}";

    Cursor.execute(consulta2);
    Resultados = {CampoLinha: [], CampoColuna: [], QtdRequisitada: []};

    for Resultado in Cursor.fetchall():
        Resultados[CampoLinha].append(ListaDict[0][Resultado[0]]);
        Resultados[CampoColuna].append(ListaDict[1][Resultado[1]]);
        Resultados[QtdRequisitada].append(Resultado[2]);

    return Resultados;

def GerarGrafico(Dados, CampoLinha, CampoColuna, Valores):
    df = pd.DataFrame(Dados);
    crosstab = pd.crosstab(index = df[CampoLinha], columns = df[CampoColuna], values = df[Valores], aggfunc = "sum", margins = True, margins_name = "Total");
    print("\nTabela crosstab gerada:");
    print(crosstab.head(len(crosstab)), end = "\n\n");
    crosstab = crosstab.apply(pd.to_numeric, errors = "coerce");
    crosstab.plot.bar();
    plt.show();

if(__name__ == "__main__"):
    Conexao, Cursor = EstabelecerConexao(pHost = "127.0.0.1", pUsuario = "root", pSenha = "", pBaseDados = "perfileleitoral");  # Conexão local usando o usuário raiz, coloque a sua senha para continuar
    key = "";

    while (key != "1"):
        print("[0] Realizar Consulta");
        print("[1] Sair");
        key = input("Escolha o que quer fazer: ");

        if (key == "0"):
            for Opcao, Valor in list(OpcoesCamposQualitativos.items()):
                print(f"[{Opcao}] {Valor}");

            print("");
            CampoLinha = OpcoesCamposQualitativos[int(input("Digite o Código do Campo-Linha: "))];
            CampoColuna = OpcoesCamposQualitativos[int(input("Digite o Código do Campo-Coluna: "))];

            while(CampoColuna == CampoLinha):
                print("Valor Repetido.");
                CampoColuna = OpcoesCamposQualitativos[int(input("Digite o Código do Campo-Coluna: "))];

            print("");

            for Opcao, Valor in list(OpcoesQuantidade.items()):
                print(f"[{Opcao}] {Valor}");

            QtdRequisitada = OpcoesQuantidade[int(input("Digite o Código da Quantidade Desejada: "))];
            print("Processando...");
            Resultado = GerarConsulta(CampoLinha, CampoColuna, Cursor, QtdRequisitada);
            GerarGrafico(Resultado, CampoLinha, CampoColuna, QtdRequisitada);

        else:
            key = "1";
            continue;

    Cursor.close();
    Conexao.close();