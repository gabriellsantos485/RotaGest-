from django.db import models

class Categoria(models.Model):
    
    cat_id = models.AutoField(primary_key=True)
    cat_nome = models.CharField(unique=True, blank=False, null=False, max_length=28)
    
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'