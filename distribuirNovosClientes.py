import pandas as pd
import random

# Carregar os dados dos vendedores e clientes antigos
df_vendedores = pd.read_excel("vendedores.xlsx")
df_clientes = pd.read_excel("clientesInativos.xlsx")

# Lista de vendedores disponíveis
vendedores_disponiveis = df_vendedores["id"].tolist()

# Função para selecionar um novo vendedor diferente do original
def novo_vendedor(original_id, vendedores):
    vendedores_possiveis = [v for v in vendedores if v != original_id]
    return random.choice(vendedores_possiveis) if vendedores_possiveis else original_id

# Aplicar a mudança de vendedor
df_clientes["novo_vendedor_id"] = df_clientes["vendedor_id"].apply(lambda x: novo_vendedor(x, vendedores_disponiveis))

# Exportar os dados atualizados para um novo arquivo Excel
output_file_movidos = "clientes_redistribuidos.xlsx"
df_clientes.to_excel(output_file_movidos, sheet_name="Clientes Redistribuidos", index=False)

# Mensagem de confirmação
print(f"Nova planilha gerada com sucesso: {output_file_movidos}")
