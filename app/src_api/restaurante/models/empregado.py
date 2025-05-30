from django.db import models
from .usuario import Usuario

class Empregado(models.Model):
    
    emp_id = models.AutoField(primary_key=True)
    emp_nome = models.CharField(max_length=18, verbose_name="Nome do Empregado", null=False, blank=False)
    emp_sobrenome = models.CharField(max_length=60, verbose_name="Sobrenome do Empregado", null=False, blank=False)
    emp_horarioTrabalho = models.CharField(max_length=13, verbose_name="Horario de Trabalho", null=False, blank=False)
    emp_rua = models.CharField(max_length=60, verbose_name="Endereço da Rua", null=True, blank=True) 
    emp_bairro = models.CharField(verbose_name="Bairro", unique=False, null=True, blank=True, max_length=28)
    emp_cidade = models.CharField(max_length=28, verbose_name="Cidade", null=True, blank=True)
    emp_estado = models.CharField(max_length=28, verbose_name="Estado", null=True, blank=False )
    emp_salario = models.DecimalField(verbose_name="Salario", max_digits=6, decimal_places=2)
    emp_dataAniversario = models.DateField(verbose_name="Data do Aniversário", blank=False, null=False)
    usu_id = models.ForeignKey('Usuario', verbose_name="Usuario", on_delete=models.CASCADE)


    class Meta:
        db_table = 'empregado'
        #unique_together = ('fun_telefone')
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        
        
    def cadastrar_cliente(self, Cliente):
        cliente = Cliente.objects.create()
        
    def realizar_pedido(self):
        pass
    
    
        

        
    
     