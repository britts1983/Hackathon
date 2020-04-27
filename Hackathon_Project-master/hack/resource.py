from import_export import resources
from .models import user

class PersonResource(resources.ModelResource):
    class Meta:
        model = user