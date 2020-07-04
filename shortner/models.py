from django.db import models
from .utils import code_generator,create_shortcode
from.validators import validate_url,validate_dot_com

# Create your models here.
class rickUrlManager(models.Manager):
    def all(self,*args,**kwargs):
        qs=super(rickUrlManager,self).all(*args,**kwargs)
        qs=qs.filter(active=True)
        return qs
    def refresh_codes(self):
        qs=rickUrlManager.objects.filter(id__gte=1)
        new_code=0
        for q in qs:
            q.shortcode=create_shortcode(q)
            q.save()
            new_code+-1
        return "Codes changed : {i} ".format(i=new_code)

class rickUrl(models.Model):
    url=models.CharField(max_length=220,validators=[validate_url])
    shortcode=models.CharField(max_length=20,unique=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects=rickUrlManager()

    def save(self,*args,**kwargs):
        if self.shortcode=='':
            self.shortcode = create_shortcode(self)
        if "http://" not in self.url and "https://" not in self.url:
            self.url="http://"+self.url
        super(rickUrl,self).save(*args,**kwargs)
    def __str__(self):
        return str(str(self.timestamp)+ "---->" + self.url)