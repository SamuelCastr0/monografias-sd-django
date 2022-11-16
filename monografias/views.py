from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

from django.urls import reverse_lazy

from .models import Monography, Advisor, CoAdvisor, Author

from django.views.generic import ListView, UpdateView, DeleteView

from django.views import View

# Create your views here.
class AdvisorView(View):
  def get(self, request):
    return render(request, 'monografias/create-advisor.html')
  
  def post(self, request):
    data = request.POST
    Advisor.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    return redirect('index')

class CoAdvisorView(View):
  def get(self, request):
    return render(request, 'monografias/create-co-advisor.html')
  
  def post(self, request):
    data = request.POST
    CoAdvisor.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    return redirect('index')

class AuthorView(View):
  def get(self, request):
    return render(request, 'monografias/create-author.html')
  
  def post(self, request):
    data = request.POST
    Author.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    return redirect('index')

class MonographyView(View):
  def get(self, request):
    advisors = Advisor.objects.all()
    co_advisors = CoAdvisor.objects.all()
    monographys = Monography.objects.all()
    authors = Author.objects.filter()

    authors_with_monographys = []
    filtered_authors = []

    for monography in monographys:
      if monography.author:
        authors_with_monographys.append(monography.author)

    for author in authors:
      if not author in authors_with_monographys:
        filtered_authors.append(author)

    return render(request, 'monografias/create-monography.html', {
      'authors': filtered_authors, 'advisors': advisors, 'co_advisors': co_advisors
    })

  def post(self, request):
    data = request.POST
    advisor = Advisor.objects.get(pk=data['advisor'])
    co_advisor = CoAdvisor.objects.get(pk=data['co_advisor'])
    author = Author.objects.get(pk=data['author'])

    print(co_advisor)

    Monography.objects.create(
      title=data['title'], 
      author=author,
      advisor=advisor,
      co_advisor=co_advisor,
      date=data['date'],
      summary=data['summary'], 
      key_words=data['key_words'], 
      university=data['university'], 
      course=data['course'],
      monography=data['monography']
    )
    return redirect('index')

class SearchMonographyView(View):
  def get(self, request):
    return render(request, 'monografias/index.html')

  def post(self, request):
    search = request.POST['search']
    monographys = Monography.objects.filter(Q(title__icontains=search) | Q(university__icontains=search) | Q(summary__icontains=search))

    return render(request, 'monografias/index.html', { "monographys": monographys })

class MonographysList(ListView):
  model = Monography
  queryset = Monography.objects.all()

class MonographyEdit(UpdateView):
  model = Monography
  fields = '__all__'
  success_url = "/"

class MonographyDelete(DeleteView):
  queryset = Monography.objects.all()
  success_url = "/"

class AuthorsList(ListView):
  model = Author
  queryset = Author.objects.all()

class AuthorEdit(UpdateView):
  model = Author
  fields = ['name','course','university','email','lattes','google_scholar','linkedin','research_gate','orcid','github']
  success_url = "/"

class AuthorDelete(DeleteView):
  queryset = Author.objects.all()
  success_url = "/"
  
class AdvisorList(ListView):
  model = Advisor
  queryset = Advisor.objects.all()

class AdvisorEdit(UpdateView):
  model = Advisor
  fields = ['name','course','university','email','lattes','google_scholar','linkedin','research_gate','orcid','github']
  success_url = "/"

class AdvisorDelete(DeleteView):
  queryset = Advisor.objects.all()
  success_url = "/"

class CoAdvisorList(ListView):
  model = CoAdvisor
  queryset = CoAdvisor.objects.all()

class CoAdvisorEdit(UpdateView):
  model = CoAdvisor
  fields = ['name','course','university','email','lattes','google_scholar','linkedin','research_gate','orcid','github']
  success_url = "/"

class CoAdvisoDelete(DeleteView):
  queryset = CoAdvisor.objects.all()
  success_url = "/"