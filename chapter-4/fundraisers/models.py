from django.db import models
from django.db.models import Sum


class Fundraiser(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    target = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def total_paid(self):
        result = Payment.objects.filter(pledge__fundraiser=self).aggregate(total=Sum("amount"))
        return result["total"] or 0

    def percent(self):
        if self.target == 0:
            return 0
        return min(100, self.total_paid() * 100 // self.target)


class Pledge(models.Model):
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE, related_name="pledges")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} pledged {self.amount}"

    def paid(self):
        result = self.payments.aggregate(total=Sum("amount"))
        return result["total"] or 0

    def balance(self):
        return self.amount - self.paid()


class Payment(models.Model):
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE, related_name="payments")
    amount = models.PositiveIntegerField()
    reference = models.CharField(max_length=20, unique=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference}: {self.amount}"
