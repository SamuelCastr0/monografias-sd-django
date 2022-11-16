from django import forms

from exemplo.models import Author, Advisor, CoAdvisor

class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = '__all__'

class AdvisorForm(forms.ModelForm):
  class Meta:
    model = Advisor
    fields = '__all__'

class CoAdvisorForm(forms.ModelForm):
  class Meta:
    model = CoAdvisor
    fields = '__all__'