# SISTEMA DE FATURAÇÃO PARA FARMÁCIA
# Criado por Emanuel Dias (Cacau Styles)

produtos = {
    "1": {"nome": "Paracetamol", "preco": 500},
    "2": {"nome": "Amoxicilina", "preco": 1200},
    "3": {"nome": "Vitamina C", "preco": 800},
    "4": {"nome": "Ibuprofeno", "preco": 650}
}

carrinho = []

print("--- SISTEMA DE VENDAS B2B - FARMÁCIA ---")
print("ID | PRODUTO | PREÇO")
for id, info in produtos.items():
    print(f"{id}  | {info['nome']} | {info['preco']} Kz")

while True:
    escolha = input("\nDigite o ID do produto para vender (ou '0' para fechar fatura): ")
    
    if escolha == '0':
        break
    
    if escolha in produtos:
        item = produtos[escolha]
        carrinho.append(item)
        print(f"-> {item['nome']} adicionado ao carrinho.")
    else:
        print("ID inválido!")

# GERAÇÃO DA FATURA
print("\n" + "="*30)
print("       FATURA DE VENDA")
print("="*30)
total = 0
for item in carrinho:
    print(f"{item['nome']}: {item['preco']} Kz")
    total += item['preco']

print("-" * 30)
print(f"TOTAL A PAGAR: {total} Kz")
print("="*30)
print("Venda finalizada com sucesso!")
