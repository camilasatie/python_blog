from django.db import models
from django.db.models.deletion import DO_NOTHING
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(
        User, on_delete=DO_NOTHING, verbose_name='Usuário')
    data_comentario = models.DateField(
        default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario
