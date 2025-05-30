from django.db import models

class Cliente(models.Model):
    
    cli_id = models.AutoField(primary_key=True)
    cli_nome = models.CharField(verbose_name= "Nome do Cliente", max_length=28, null=False, blank=False)
    cli_sobrenome = models.CharField(verbose_name= "Sobrenome do Cliente", max_length=60, null=False, blank=False)
    cli_telefone = models.CharField(verbose_name= "Telefone do Cliente", max_length=16, null=False, blank=False) 
    cli_email = models.EmailField(verbose_name="Email", max_length=120, unique=True)
    cli_dataNascimento = models.DateField(verbose_name="Data de Nascimento", blank=False, null=False)
    cli_rua = models.CharField(verbose_name= "Rua do Cliente", max_length=60)
    cli_numeroCasa = models.CharField(verbose_name= "Numero da Casa", max_length=6, )
    cli_bairro = models.CharField(verbose_name= "Bairro do Cliente", max_length=28)
    cli_cidade = models.CharField(verbose_name= "Cidade do Cliente", max_length=28)
    cli_estado = models.CharField(verbose_name= "Estado do Cliente", max_length=28)
    cli_complemento = models.CharField(verbose_name= "Complemento do Endereço", max_length=120)
    
    class Meta:
        db_table = 'cliente'
        unique_together = ('cli_email', 'cli_telefone')
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'