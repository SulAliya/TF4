from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import DiaryForm
from diary.models import DiaryEntry


class DiaryListView(ListView):
    model = DiaryEntry


class DiaryDetailView(DetailView):
    model = DiaryEntry


class DiaryCreateView(CreateView):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')


class DiaryUpdateView(UpdateView):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')


class DiaryDeleteView(DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diary:diaryentry_list')
