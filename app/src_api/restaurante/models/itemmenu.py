from django.db import models

class ItemMenu(models.Model):
    
    ite_id = models.AutoField(primary_key=True)
    ite_qtde = models.IntegerField(verbose_name="Quantidade de Itens")
    ite_valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor das unidades")
    
    ped_id = models.ForeignKey('Pedido', on_delete=models.CASCADE, verbose_name='Pedido', blank=False, null=False)
    car_id = models.ForeignKey('Cardapio', on_delete=models.CASCADE, verbose_name='Cardapio', blank=False, null=False)
    
    class Meta: 
        db_table = 'item_menu'
        verbose_name = 'Item do Menu'
        verbose_name_plural = 'Itens do Menu'
    