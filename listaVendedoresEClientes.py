import pandas as pd

# Carregar os dados dos vendedores e clientes
df_vendedores = pd.read_excel("vendedores.xlsx")
df_clientes = pd.read_excel("clientes.xlsx")

# Criar um dicionário relacionando vendedores a seus clientes
vendedores_dict = {}
for vendedor_id in df_vendedores["id"].unique():
    nome_vendedor = df_vendedores[df_vendedores["id"] == vendedor_id]["razao_social"].values[0]
    clientes_vendedor = df_clientes[df_clientes["vendedor_id"] == vendedor_id]["razao_social"].tolist()
    vendedores_dict[vendedor_id] = {"nome": nome_vendedor, "clientes": clientes_vendedor}

# Exibir lista de vendedores
def listar_vendedores():
    print("Vendedores disponíveis:")
    for v_id, v_info in vendedores_dict.items():
        print(f"ID: {v_id} - Nome: {v_info['nome']}")
    print("\nDigite o código do vendedor para ver os clientes.")

# Exibir clientes de um vendedor
def mostrar_clientes(vendedor_id):
    if vendedor_id in vendedores_dict:
        print(f"\nClientes do vendedor {vendedores_dict[vendedor_id]['nome']}:")
        for cliente in vendedores_dict[vendedor_id]["clientes"]:
            print(f"- {cliente}")
    else:
        print("Código de vendedor não encontrado.")

# Console interativo
def main():
    listar_vendedores()
    while True:
        try:
            vendedor_id = int(input("Digite o código do vendedor (ou 0 para sair): "))
            if vendedor_id == 0:
                break
            mostrar_clientes(vendedor_id)
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
    