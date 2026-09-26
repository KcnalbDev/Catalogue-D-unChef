Título do projeto: Restaurante com Ítens de Alimentação em um Menu criados por um Chef

Entidades
	• Restaurante : Restaurantes
	• Chef : Chefs
	• ItemAlimentação : ItensAlimentação
	• ItemCarne : ItensCarne
	• ItemMassa : ItensMassa
	• Menu : Menus

Relacionamentos
	• Sem Referências : ItemAlimentação, Chef
	• Relacionamento Múltiplo : Menu [n:n] ItemAlimentação
	• Associação : Restaurante [Menu, Chef]
	• Herança : ItemAlimentação [ItemCarne, ItemMassa]

Atributos e referências
	• Restaurante : local, menu, chef
	• Chef : nome, anos_experiência, estrangeiro, data_nascimento
	• ItemAlimentação : nome, preço, avaliação, nivel_popularidade
	• ItemCarne : tipo_carne, tempero
	• ItemMassa : tipo_massa, tipo_molho
	• Menu : título, tipo, armazenamento, itens_alimentação

Enumerados
	•avaliação : ruim, médio, bom, ótimo
	• tipo_carne : frango, peixe, bovino, suíno
	• tipo_massa : espaguete, fettuccini, semôla, gnocci
	• tipo_molho : molho_branco, molho_vermelho, molho_madeiro, molho_barbecue
