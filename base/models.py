from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todo'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
