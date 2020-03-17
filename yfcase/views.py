from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Case

class CaseListView(LoginRequiredMixin,ListView):
	model = Case
	template_name = 'case_list.html'
	login_url = 'login'

class CaseDetailView(LoginRequiredMixin,DetailView):
	model = Case
	template_name = 'case_detail.html'
	login_url = 'login'

class CaseUpdateView(LoginRequiredMixin,UpdateView):
	model = Case
	fields = ['casenumber','city', 'township','section','small_section',]
	template_name = 'case_edit.html'

class CaseCreateView(LoginRequiredMixin,CreateView):
	model = Case
	template_name = 'case_new.html'
	fields = ['casenumber','city', 'township','section','small_section',]
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class CaseDeleteView(LoginRequiredMixin,DeleteView):
	model = Case
	template_name = 'case_delete.html'
	success_url = reverse_lazy('case_list')
	login_url = 'login'

