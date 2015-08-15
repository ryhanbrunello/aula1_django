from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True)
    idade = models.IntegerField()

    def __unicode__(self):
        return self.nome+' - '+str(self.idade)+' Anos '


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    telefone = models.CharField(max_length=9)