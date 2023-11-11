from django.db import models


class SwagAward(models.Model):
    swag = models.ForeignKey('Swag', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.swag.description + ' to ' + self.user.username

    def save(self, *args, **kwargs):
        self.swag.stock -= 1
        self.swag.save()
        super().save(*args, **kwargs)


class Swag(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='swags', blank=True)
    points = models.IntegerField()
    awarded = models.ManyToManyField('auth.User', through=SwagAward, related_name='awarded_swags')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.description
