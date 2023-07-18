from django.forms import ModelForm
from .models import Stage

class StageForm(ModelForm):
  class Meta:
    model = Stage
    fields = '__all__'