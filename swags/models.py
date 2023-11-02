from django.db import models


class SwagAward(models.Model):
    swag = models.ForeignKey('Swag', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.swag.description + ' to ' + self.user.username


class Swag(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='swags', blank=True)
    points = models.IntegerField(blank=True, null=True)
    awarded = models.ManyToManyField('auth.User', through=SwagAward, related_name='awarded_swags')

    def __str__(self):
        return self.description
