from django.db import models

class FormaPagamento(models.Model):
    
    fpa_id = models.AutoField(primary_key=True)
    fpa_forma = models.CharField(verbose_name="Forma de Pagamento", max_length=42, null=False, blank=False)
    
    class Meta:
        db_table = 'formapagamento'
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'
        