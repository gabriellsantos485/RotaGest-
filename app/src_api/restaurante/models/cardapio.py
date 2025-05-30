from django.db import models

class Cardapio(models.Model):
    
    car_id = models.AutoField(primary_key=True)
    car_nome = models.CharField(verbose_name="Nome", blank=False, null=False, max_length=60)
    car_valor = models.DecimalField(verbose_name="Valor", blank=False, null=False, max_digits=6, decimal_places=2)
    car_status = models.BooleanField(verbose_name="Status", blank=False, null=False, default=True)
    cat_id = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name="Categoria", null=False, blank=False)
    
    class Meta:
        db_table = 'cardapio'
        verbose_name = 'Cardapio'
        
        
        
    