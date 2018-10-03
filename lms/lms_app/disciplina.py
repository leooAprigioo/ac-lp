from django.db import models

class Disciplina(models.Model):
    
    def save(self):
        if (len(Disciplina.objects.filter(nome=self.nome)) > 0):
            raise Exception("Disciplina ja cadastrada")
        super(Disciplina, self).save()

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)
