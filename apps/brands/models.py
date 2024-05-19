from django.db import models

from apps.common import models as base_models


class Brand(base_models.BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
