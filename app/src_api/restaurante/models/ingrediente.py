from django.db import models

class Ingrediente(models.Model):
    
    ing_id = models.AutoField(primary_key=True)
    ing_nome = models.CharField(verbose_name="Nome", max_length=28, blank=False, null=False)

    
    class Meta:
        db_table = 'ingrediente'
        verbose_name = 'ingrediente'
        verbose_name_plural = 'Ingredientes'