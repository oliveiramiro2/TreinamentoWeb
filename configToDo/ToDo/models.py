from django.db import models

class Task(models.Model):
    
    STATUS = (
        ("1", 'Doing'),
        ("2", 'Done'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=8,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
