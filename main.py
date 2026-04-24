import csv
with open("product_catalog.csv", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    gross_inventory = list(reader)

def process_inventory(list_products):
    for product in list_products:
        product['sku'] = product['sku'].upper()
        product['sale_price'] = float(product['cost_price']) * 1.30
        print(f'O product {product["name"]}, de SKU {product["sku"]} custa R${product["cost_price"]} mas é vendido por R${product["sale_price"]:.2f} com 30% de lucro')
    return list_products

clean_inventory = process_inventory(gross_inventory)

with open("priced_inventory.csv", mode = "w", encoding="utf-8", newline="") as output_file:
    columns=['name', 'sku','category','cost_price','sale_price']
    writer = csv.DictWriter(output_file, fieldnames=columns)
    
    writer.writeheader()
    writer.writerows(clean_inventory)

total_products = len(clean_inventory)

print("--------------------------------------------------")
print(f"SUCESSO: Processamento concluído!")
print(f"Total de itens atualizados: {total_products}")
print(f"Arquivo 'priced_inventory.csv' gerado com sucesso.")
print("--------------------------------------------------")
