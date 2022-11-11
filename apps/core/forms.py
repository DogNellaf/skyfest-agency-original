from django.forms import ModelForm

from core import models
from snippets.forms.fields import MultipleImageField


class GalleryForm(ModelForm):
    multiupload = MultipleImageField(label='Массовая загрузка фотографий', required=False)

    class Meta:
        model = models.Gallery
        fields = '__all__'
