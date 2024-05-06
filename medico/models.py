from django.db import models

# Criando os modelos
class Especialidade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class Medico(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    telefone = models.CharField(max_length=30)
    email = models.EmailField()
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=30)
    id_especialidade = models.ForeignKey("Especialidade", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome