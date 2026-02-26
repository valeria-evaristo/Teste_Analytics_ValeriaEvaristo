-- Para listar o produto, a categoria e o total de vendas, ordenado do maior para o menor, utilizamos esta consulta SQL:

SELECT produto, categoria, SUM(total_vendas) AS total_vendas
FROM read_csv('dados_limpos.csv')
GROUP BY produto, categoria
ORDER BY total_vendas DESC;

-- Para identificar os produtos que menos venderam, podemos usar a seguinte consulta SQL: 

SELECT produto, categoria, SUM(total_vendas) AS total_vendas
FROM read_csv('dados_limpos.csv')   
GROUP BY produto, categoria
ORDER BY total_vendas ASC
LIMIT 10;

