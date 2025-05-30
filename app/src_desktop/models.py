# from django.db import models

# class Empregado(models.Model):
#     emp_id = models.AutoField(primary_key=True)
#     emp_nome = models.CharField(max_length=18, verbose_name="Nome do Empregado", null=False, blank=False)
#     emp_sobrenome = models.CharField(max_length=60, verbose_name="Sobrenome do Empregado", null=False, blank=False)
#     emp_horarioTrabalho = models.CharField(max_length=13, verbose_name="Horario de Trabalho", null=False, blank=False)
#     emp_rua = models.CharField(max_length=60, verbose_name="Endereço da Rua", null=True, blank=True) 
#     emp_bairro = models.CharField(verbose_name="Bairro", unique=False, null=True, blank=True)
#     emp_cidade = models.CharField(max_length=28, verbose_name="Cidade", null=True, blank=True)
#     emp_estado = models.CharField(max_length=28, verbose_name="Estado", null=True, blank=False )
#     emp_salario = models.DecimalField(verbose_name="Salario", max_digits=6, decimal_places=2)
#     emp_dataAniversario = models.DateField(verbose_name="Data do Aniversário", blank=False, null=False)


#     class Meta:
#         db_table = 'empregado'
#         #unique_together = ('fun_telefone')
#         verbose_name = 'Empregado'
#         verbose_name_plural = 'Empregados'
        
#     def cadastrar_cliente(self, nome, email):
#         cliente = Cliente.objects.create(nome=nome, email=email)

#     def __str__(self):
#         return self.fun_nome


# class Cliente(models.Model):
#     cli_id = models.AutoField(primary_key=True)
#     cli_nome = models.CharField(max_length=28, verbose_name="Nome do Cliente", null=False, blank=False)
#     cli_sobrenome = models.CharField(max_length=28, verbose_name="Sobrenome do Cliente", null=True, blank=False)
#     cli_aniversario = models.DateField(verbose_name="Data de Aniversário", null=True, blank=True)
#     cli_isActive = models.BooleanField(default=True, verbose_name="Ativo")
#     cli_telefone = models.CharField(max_length=20, verbose_name="Telefone", null=True, blank=True)
#     cli_email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
#     cli_cidade = models.CharField(max_length=255, verbose_name="Cidade", null=True, blank=True)
#     cli_bairro = models.CharField(max_length=255, verbose_name="Bairro", null=True, blank=True)
#     cli_rua = models.CharField(max_length=255, verbose_name="Rua", null=True, blank=True)
#     cli_complemento = models.CharField(max_length=255, verbose_name="Complemento", null=True, blank=True)

#     class Meta:
#         db_table = 'cliente'
#         unique_together = ('cli_email', 'cli_telefone')
#         verbose_name = 'Cliente'
#         verbose_name_plural = 'Clientes'

#     def __str__(self):
#         return f"{self.cli_nome} {self.cli_sobrenome}"


# class Comanda(models.Model):
#     com_id = models.AutoField(primary_key=True)
#     com_status = models.BooleanField(default=False, verbose_name="Status da Comanda", null=False, blank=False)

#     class Meta:
#         db_table = 'comanda'
#         verbose_name = 'Comanda'
#         verbose_name_plural = 'Comandas'

#     def __str__(self):
#         return f"Comanda {self.com_id}"


# class Pedido(models.Model):
#     STATUS_CHOICES = [
#         ('A', 'Aberto'),
#         ('F', 'Fechado'),
#         ('C', 'Cancelado'),
#     ]

#     ped_id = models.AutoField(primary_key=True)
#     ped_abertura = models.DateTimeField(verbose_name="Abertura", null=True, blank=False)
#     ped_fechamento = models.DateTimeField(verbose_name="Fechamento", null=True, blank=True)
#     ped_status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="Status do Pedido", default='A', null=False, blank=False)
#     ped_valorTotal = models.FloatField(verbose_name="Valor Total", null=True, blank=True)
#     cli_id = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='pedidos', verbose_name="Cliente", null=False, blank=False)
#     com_id = models.ForeignKey('Comanda', on_delete=models.CASCADE, related_name='pedidos', verbose_name="Comanda", null=True, blank=False)
#     fpa_id = models.ForeignKey('FormaPagamento', on_delete=models.CASCADE, related_name='pedidos', verbose_name="FormaPagamento", null=True, blank=False)
    
#     class Meta:
#         db_table = 'pedido'
#         verbose_name = 'Pedido'
#         verbose_name_plural = 'Pedidos'

#     def __str__(self):
#         return f"Pedido {self.ped_id} - Status: {self.get_ped_status_display()} - Valor: {self.ped_valorTotal}"


# class FormaPagamento(models.Model):
#     fpa_id = models.AutoField(primary_key=True)
#     fpa_tipo = models.CharField(max_length=60, unique=True, verbose_name="Tipo de Pagamento", null=False, blank=False)

#     class Meta:
#         db_table = 'forma_pagamento'
#         verbose_name = 'Forma de Pagamento'
#         verbose_name_plural = 'Formas de Pagamento'

#     def __str__(self):
#         return self.fpa_tipo


# class ItemMenu(models.Model):
#     ime_id = models.AutoField(primary_key=True)
#     ime_valorUnitario = models.FloatField(verbose_name="Valor Unitário", null=False, blank=False)
#     ime_qtde = models.IntegerField(verbose_name="Quantidade", null=False, blank=False)
#     ped_id = models.ForeignKey('Pedido', on_delete=models.CASCADE, related_name='itens', verbose_name="Pedido")
#     menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='itens', verbose_name="Menu")

#     class Meta:
#         db_table = 'item_menu'
#         verbose_name = 'Item do Menu'
#         verbose_name_plural = 'Itens do Menu'

#     def __str__(self):
#         return f"Item {self.ime_id} - Pedido {self.ped_id.ped_id}"


# class Categoria(models.Model):
#     cat_id = models.AutoField(primary_key=True)
#     cat_nome = models.CharField(max_length=255, unique=True, verbose_name="Nome da Categoria", null=False, blank=False)

#     class Meta:
#         db_table = 'categoria'
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'

#     def __str__(self):
#         return self.cat_nome


# class Menu(models.Model):
#     menu_id = models.AutoField(primary_key=True)
#     menu_nome = models.CharField(max_length=255, verbose_name="Nome do Menu", unique=True, null=False, blank=False)
#     menu_valor = models.FloatField(verbose_name="Valor do Menu", null=False, blank=False)
#     menu_status = models.BooleanField(default=True, verbose_name="Status do Menu")
#     menu_descricao = models.TextField(null=True, blank=True, verbose_name="Descrição do Menu")
#     menu_imagem = models.CharField(max_length=255, verbose_name="Imagem do Menu", null=True, blank=True)
#     cat_id = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='menus', verbose_name="Categoria")

#     class Meta:
#         db_table = 'menu'
#         unique_together = ('menu_nome', 'menu_imagem')
#         verbose_name = 'Menu'
#         verbose_name_plural = 'Menus'

#     def __str__(self):
#         return self.menu_nome
