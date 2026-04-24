stock = [{
            'name' : 'Playstation 5',
            'sku' : 'PS5elet',
            'category' : 'Eletronics',
            'cost_price' : 2000},
           {
            'name' : 'Iphone 17',
            'sku' : 'IP17elet',
            'category' : 'Eletronics',
            'cost_price' : 1000},
            {
            'name' : 'MacBook',
            'sku' : 'MCelet',
            'category' : 'Eletronics',
            'cost_price' : 4000}]

#LOOP PARA PERCORRER O ESTOQUE
for produto in stock:
    produto['sku'] = produto['sku'].upper()
    produto['sale_price'] = produto['cost_price'] * 1.30
    print(f'O produto {produto["name"]}, de SKU {produto["sku"]} custa R${produto["cost_price"]} mas é vendido por R${produto["sale_price"]:.2f} com 30% de lucro')

