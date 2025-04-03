Este é um caso real da empresa que trabalho atualmente, que foi resolvido de maneira simples com dois códigos em Python.

### Overview sobre o problema.

  Cada vendedor possui um portifólio de clientes, porém existem clientes que não são recorrentes, ou seja, fizeram apenas uma compra ou compraram há muito tempo.

  Na tentativa de trazer esses clientes de volta às compras, o time responsável bolou a seguinte estratégia:

  * Classificar os clientes inativos(última compra há mais de 3 meses).
  * Realocar estes clientes para o portifólio de outro vendedor.

### Colocando em prática.

  * Comecei separando os vendedores e clientes em uma tabela, que extraí do banco de dados do nosso ERP/CRM.
  * Depois, fiz um pequeno código em Python(listaVendedoresEClientes.py) que lista os vendedores e mostra o portifólio de clientes atual.
  * Após, classifiquei os clientes inativos com base nos critérios que foram passados pelo time responsável.
  * Por fim, fiz outro pequeno código em Python(distribuirNovosClientes.py) utilizando apenas as bibliotecas PANDA e RANDOM.

### Conclusão.

  Com códigos simples, podemos fazer grande diferença no resultado da empresa, com adição de tecnologia aos processos e procedimentos internos.
