from django.db import models

class Comanda(models.Model):
    
    com_id = models.IntegerField(primary_key=True)
    com_status = models.BooleanField(default=False, verbose_name="Status da Comanda", null=False, blank=False)
    
    
    class Meta:
        db_table = 'comanda'
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'

    def __str__(self):
        return f"Comanda {self.com_id}"
    
