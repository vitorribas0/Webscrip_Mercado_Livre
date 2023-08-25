import pandas as pd

# Carregar o arquivo JSON em um DataFrame do pandas
json_file = 'pagination.json'
df = pd.read_json(json_file)

# Especificar o nome do arquivo de saída Excel
excel_file = 'Excel.xlsx'

# Salvar o DataFrame como um arquivo Excel
df.to_excel(excel_file, index=False)

print(f'Arquivo Excel "{excel_file}" criado com sucesso!')
