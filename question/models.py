from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Question(models.Model):
    question_text = models.TextField(blank=True)
    question_picture = models.ImageField(upload_to='questions/', blank=True)

    def __str__(self):
        return f"{self.id}"


class Option(models.Model):
    option_text = models.TextField(blank=True)
    option_picture = models.ImageField(upload_to='options/', blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.id}"
