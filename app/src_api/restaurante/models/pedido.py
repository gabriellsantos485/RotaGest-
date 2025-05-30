from django.db import models

class Pedido(models.Model):
    
    STATUS_CHOICES = [
        ('A', 'Aberto'),
        ('F', 'Fechado'),
        ('C', 'Cancelado'),
    ]
    
    ped_id = models.AutoField(primary_key=True)
    ped_dataAbertura = models.DateField(auto_now_add=True, verbose_name="Data de Abertura")
    ped_dataFechamento = models.DateField(verbose_name="Data de Fechamento", null=True, blank=True)
    ped_status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="Status do Pedido", default='A', null=False, blank=False)
    ped_valorTotal = models.FloatField(verbose_name="Valor Total", null=True, blank=True)
    
    cli_id = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="Cliente", null=False, blank=False)
    mesa_id = models.ForeignKey('Mesa', on_delete=models.CASCADE, verbose_name="Mesa", null=False, blank=False)
    com_id = models.ForeignKey('Comanda', on_delete=models.CASCADE, verbose_name="Comanda", null=False, blank=False)
    emp_id = models.ForeignKey('Empregado', on_delete=models.CASCADE, verbose_name='Empregado', null=False, blank=False)
    fpa_id = models.ForeignKey('FormaPagamento', on_delete=models.CASCADE, verbose_name='Forma de Pagamento', null=False, blank=False)
    
    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'