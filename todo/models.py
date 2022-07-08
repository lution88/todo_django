from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField("제목", max_length=100)
    description = models.TextField("내용")
    dt_created = models.DateTimeField("생성일", auto_now_add=True)
    complete = models.BooleanField("완료 여부", default=False)
    important = models.BooleanField("중요도", default=False)

    def __str__(self):
        return self.title