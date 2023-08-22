from django.db import models


class Expense(models.Model):
    user_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Expense {self.amount} by user {self.user_id}"
