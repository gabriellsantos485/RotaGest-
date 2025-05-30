from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password

class UsuarioManager(BaseUserManager):
    """Gerenciador de usuários para criar usuários e superusuários corretamente."""

    def create_user(self, usu_username, usu_email, usu_password=None, **extra_fields):
        if not usu_email:
            raise ValueError("O email é obrigatório!")

        user = self.model(
            usu_username=usu_username,
            usu_email=self.normalize_email(usu_email),
            **extra_fields
        )
        user.set_password(usu_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usu_username, usu_email, usu_password=None, **extra_fields):
        extra_fields.setdefault("usu_isAdmin", True)
        return self.create_user(usu_username, usu_email, usu_password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    usu_id = models.AutoField(primary_key=True)
    usu_telefone = models.CharField(verbose_name="Telefone", max_length=16)
    usu_email = models.EmailField(verbose_name="Email", max_length=120, unique=True)
    usu_password = models.CharField(verbose_name="Senha", max_length=255)  # Agora usa hash maior
    usu_username = models.CharField(verbose_name="Nome de Usuário", max_length=18, unique=True)
    usu_isAdmin = models.BooleanField(verbose_name="Administrador", default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "usu_username"
    REQUIRED_FIELDS = ["usu_email"]

    class Meta:
        db_table = "usuario"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def set_password(self, raw_password):
        """Criptografa a senha antes de salvar no banco."""
        self.usu_password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Verifica se a senha informada corresponde ao hash armazenado."""
        return check_password(raw_password, self.usu_password)
