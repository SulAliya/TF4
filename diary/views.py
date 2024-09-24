from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import DiaryForm
from diary.models import DiaryEntry


class DiaryListView(ListView):
    model = DiaryEntry


class DiaryDetailView(DetailView):
    model = DiaryEntry


class DiaryCreateView(CreateView, LoginRequiredMixin):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiaryUpdateView(UpdateView):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')


class DiaryDeleteView(DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diary:diaryentry_list')
