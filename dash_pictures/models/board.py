from django.db import models


class BoardQuerySet(models.QuerySet):
    def filter_user_and_predefined(self, user_id):
        return self.filter(
            models.Q(user_id=user_id) |
            models.Q(predefined=True),
        )


class Board(models.Model):

    user = models.ForeignKey(
        'dash_pictures.PinterestUser',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='boards',
    )
    predefined = models.BooleanField(
        default=False,
    )
    pinterest_id = models.CharField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
    )
    deleted = models.BooleanField(
        default=False,
        blank=True,
    )

    objects = BoardQuerySet.as_manager()

    def __str__(self):
        return self.name
