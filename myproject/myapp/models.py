from django.db import models
from django.utils import timezone


# Create your models here.
status_choices = [
    (0, 'Inactive'),
    (1, 'Active'),
    (5, 'Delete')
]
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    status = models.IntegerField(choices = status_choices, default = 1)

    class Meta:
        db_table = 'user_table'
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    stock = models.IntegerField()

    def available_books(self):
        from .models import Record

        borrowed_count = Record.objects.filter(
            book=self,
            return_date__isnull=True   # only open records
        ).count()

        return self.stock - borrowed_count

    class Meta:
        db_table = 'book_table'

    def __str__(self):
        return self.title

class Record(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    status = models.CharField(max_length=10, default='open')  
    # values: 'open' (not returned), 'closed' (returned)

    issue_date = models.DateField(default=timezone.now)
    # can be selected while borrowing; defaults to now if omitted

    return_date = models.DateField(null=True, blank=True)  
    # null = not returned yet 

    class Meta:
        db_table = 'record_table'

    def calculate_fine(self):
        if self.status == 'open':
            end_date = timezone.now().date()
        else:
            end_date = self.return_date or timezone.now().date()

        end_date = end_date.date() if hasattr(end_date, 'date') else end_date

        issue_date = self.issue_date.date() if hasattr(self.issue_date, 'date') else self.issue_date
        days_passed = (end_date - issue_date).days

        if days_passed < 0:
            return 0

        # First 7 days free
        if days_passed <= 7:
            return 0
        
        fine = (days_passed - 7) * 2
        return fine

    @property
    def fine(self):
        return self.calculate_fine()
    

    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"



     
