from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.description} - {self.amount} - {self.category} - {self.datetime.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-datetime']