from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)
  
    def __str__(self)->str:
        return str(self.current_balance)

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')))
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"the amount is {self.amount} for the {self.description} which is a {self.expense_type} type transaction"
    
class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length=100)
    request_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)