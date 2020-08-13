from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename

class Base(models.Model):
    data_cria = models.DateField("Postado", auto_now_add = True)
    data_act = models.DateField("Actualizado", auto_now = True)
    Activ = models.BooleanField("Esta activo?", default = True)
    
    class Meta:
        abstract = True
        
class Lancamentos(Base):
    image = StdImageField("Imagem do filme", upload_to = get_file_path, variations = {"thumb": {"width": 300, "height": 330, "crop":True}})
    nome_film = models.CharField("Nome do filme", max_length = 100)
    genero = models.CharField("Género", max_length = 50)
    link = models.CharField("Link para assistir", max_length = 500, default = "#")
    assistir = models.CharField("Link para baixar", max_length = 500, default = "#")
    descricao = models.TextField("Simpose", max_length = 1000)
    
    class Meta:
        verbose_name = "Lançamento"
        verbose_name_plural = "Lançamentos"
        
    def __str__(self):
        return self.nome_film
        
class Misturados(Base):
    image = StdImageField("Imagem do filme", upload_to = get_file_path, variations = {"thumb": {"width": 270, "height": 300, "crop":True}})
    nome_film = models.CharField("Nome do filme", max_length = 100)
    genero = models.CharField("Género", max_length = 50)
    link = models.CharField("Link para assistir", max_length = 500, default = "#")
    assistir = models.CharField("Link para baixar", max_length = 500, default = "#")
    simpose = models.CharField("Simpose", max_length = 1000)
    
    class Meta:
        verbose_name = "Misturado"
        verbose_name_plural = "Misturados"
        
    def __str__(self):
        return self.nome_film
