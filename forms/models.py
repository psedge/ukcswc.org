from django.db import models

class Feedback(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class KitForm(models.Model):
    problem = models.CharField(max_length=500)
    area = models.CharField(
        max_length=50,
        choices=(
            ('sailing', "The problem is to do with Sailing / Boat kit \n"),
            ('windsurfing', "The problem is to do with  Windsurfing kit \n"),
            ('clothing', "The problem is to do with items of clothing \n"),
        ),
    )

    def __str__(self):
        return self.area + " - " + self.problem


