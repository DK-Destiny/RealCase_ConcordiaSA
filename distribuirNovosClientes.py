import pandas as pd
import random

df_vendedores = pd.read_excel("vendedores.xlsx")
df_clientes = pd.read_excel("clientesInativos.xlsx")

vendedores_disponiveis = df_vendedores["id"].tolist()

def novo_vendedor(original_id, vendedores):
    vendedores_possiveis = [v for v in vendedores if v != original_id]
    return random.choice(vendedores_possiveis) if vendedores_possiveis else original_id

df_clientes["novo_vendedor_id"] = df_clientes["vendedor_id"].apply(lambda x: novo_vendedor(x, vendedores_disponiveis))

output_file_movidos = "clientes_redistribuidos.xlsx"
df_clientes.to_excel(output_file_movidos, sheet_name="Clientes Redistribuidos", index=False)

print(f"Nova planilha gerada com sucesso: {output_file_movidos}")
