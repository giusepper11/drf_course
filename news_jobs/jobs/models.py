from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
