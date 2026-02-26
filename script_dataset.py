import pandas as pd
import random
from datetime import datetime, timedelta

#Lista básica de categorias e produtos
categoria = {
    "Eletrônicos": ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Câmera", "Microfone", "Monitor"],
    "Vestuário": ["Camiseta", "Calça Jeans", "Tênis", "Jaqueta", "Vestido", "Saia", "Blusa", "Shorts"],
    "Alimentos": ["Arroz", "Feijão", "Chocolate", "Café", "Leite", "Pão", "Frutas", "Legumes"]
}

dados = []

for i in range (1, 51):
    #Produto e categoria aleatórios
    categoria_escolhida = random.choice(list(categoria.keys())) 
    produto = random.choice(categoria[categoria_escolhida])
    quantidade = random.randint(1, 10)
    preco = round(random.uniform(10, 1000), 2)

    #Gerar data 
    inicio = datetime(2023, 1, 1)
    dias = random.randint(1, 365)
    data = inicio + timedelta(days=dias)

    dados.append({
        "ID": i, 
        "Data": data.strftime('%Y-%m-%d'),
        "Produto": produto,
        "Categoria": categoria_escolhida,
        "Quantidade": quantidade,
        "Preço": preco

    })

    #Criar DataFrame
    df = pd.DataFrame(dados, columns=["ID", "Data", "Produto", "Categoria", "Quantidade", "Preço"])
    
    #Exibe
    print (df)

    #Salva o arquivo CSV
    df.to_csv("vendas_teste.csv", index=False)
