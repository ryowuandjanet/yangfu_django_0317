from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LandFormSet
from .models import Case

class CaseListView(LoginRequiredMixin,ListView):
	model = Case
	template_name = 'case_list.html'
	login_url = 'login'

class CaseDetailView(LoginRequiredMixin,DetailView):
	model = Case
	template_name = 'case_detail.html'
	login_url = 'login'

class CaseCreateView(LoginRequiredMixin,CreateView):
	model = Case
	template_name = 'case_new.html'
	fields = ('__all__')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class CaseFamilyCreateView(LoginRequiredMixin,CreateView):
    model = Case
    template_name = 'case_new.html'
    # fields = ['casenumber','city','township','section','small_section',]
    fields = ('__all__')
    login_url = 'login'
    success_url = reverse_lazy('case_list')

    def get_context_data(self, **kwargs):
        data = super(CaseFamilyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lands'] = LandFormSet(self.request.POST)
        else:
            data['lands'] = LandFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lands = context['lands']
        with transaction.atomic():
            self.object = form.save()

            if lands.is_valid():
                lands.instance = self.object
                lands.save()
        return super(CaseFamilyCreateView, self).form_valid(form)

class CaseUpdateView(LoginRequiredMixin,UpdateView):
	model = Case
	fields = ['casenumber','city', 'township','section','small_section',]
	template_name = 'case_edit.html'
	login_url = 'login'

class CaseFamilyUpdateView(UpdateView):
    model = Case
    template_name = 'case_edit.html'
    # fields = ['casenumber','city','township','section','small_section',]
    fields = ('__all__')
    login_url = 'login'
    success_url = reverse_lazy('case_list')

    def get_context_data(self, **kwargs):
        data = super(CaseFamilyUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lands'] = LandFormSet(self.request.POST, instance=self.object)
        else:
            data['lands'] = LandFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lands = context['lands']
        with transaction.atomic():
            self.object = form.save()

            if lands.is_valid():
                lands.instance = self.object
                lands.save()
        return super(CaseFamilyUpdateView, self).form_valid(form)

class CaseDeleteView(LoginRequiredMixin,DeleteView):
	model = Case
	template_name = 'case_delete.html'
	success_url = reverse_lazy('case_list')
	login_url = 'login'
