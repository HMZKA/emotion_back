from django.db import models

from company.models import Company
from user.models import User
from django.core.exceptions import ValidationError


class Job(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    company_id = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    count_applicants = models.IntegerField(null=False)
    applicants=models.ManyToManyField(User)
    
    def apply(self, user):
        if not self.applicants.filter(pk=user.pk).exists():
            self.applicants.add(user)
            self.count_applicants += 1
            self.save()
        else:
            raise ValidationError("User has already applied to this job.")