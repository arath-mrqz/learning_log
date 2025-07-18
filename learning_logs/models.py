from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic each user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representing of the model"""
        return self.text


class Entry(models.Model):
    """An entry an user could register about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry"""
        if len(self.text) <= 50:
            return self.text

        return f"{self.text[:50]}..."

