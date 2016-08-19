from django.db import models

class Feedback(models.Model):
    view_only = True

    class Meta:
        verbose_name = 'Feedback Submission'
        verbose_name_plural = 'Feedback Submissions'

    # Attributes
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class KitForm(models.Model):
    view_only = True

    class Meta:
        verbose_name = 'Missing / Broken Kit'
        verbose_name_plural = 'Missing Kit Reports'

    # Attributes
    problem = models.CharField(max_length=500)
    area = models.CharField(
        max_length=50,
        choices=(
            ('sailing', "The problem is to do with Sailing / Boat kit \n"),
            ('windsurfing', "The problem is to do with  Windsurfing kit \n"),
            ('clothing', "The problem is to do with items of clothing \n"),
        ),
    )
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.area + " - " + self.problem


