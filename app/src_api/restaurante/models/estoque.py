from django.db import models

class Estoque(models.Model):
    
    est_id  = models.AutoField(primary_key=True)
    est_qtde = models.IntegerField(verbose_name="Quantidade", null=False, blank=False)
    est_validade = models.DateField(verbose_name="Validade", null=False, blank=False)
    est_dataAtual = models.DateField(verbose_name="Data Atual", auto_now_add=True)
    ing_id = models.ForeignKey('Ingrediente', on_delete=models.CASCADE, verbose_name="Ingrediente", blank=False, null=False )
    car_id = models.ForeignKey('Cardapio', on_delete=models.CASCADE, verbose_name="Cardapio", blank=False, null=False)
    
    class Meta:
        db_table = 'estoque'
        verbose_name = 'Estoque'