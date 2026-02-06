from django.db import models

class Lead(models.Model):
    email = models.EmailField(unique=True)

    source = models.CharField(
        max_length=100,
        blank=True,
        help_text="Where the lead came from Landing"
    )

    contacted = models.BooleanField(
        default=False,
        help_text="Has Denisa already contacted this lead?"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email