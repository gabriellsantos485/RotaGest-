from django.db import models

class Mesa(models.Model):
    
    mesa_id = models.IntegerField(primary_key=True)
    mesa_status = models.BooleanField(default=False, verbose_name="Status da Comanda", null=False, blank=False)
    
    class Meta:
        db_table = 'mesa'
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'