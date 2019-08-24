from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from .models import Listing, Event_subscriptions, Unregistered_user
from .forms import Unregistered_user_form


class Events(ListView):
  model = Listing
  template_name = 'events/events.html'
  context_object_name = 'events'
  ordering = ['date']


class FullInformation(DetailView):
  model = Listing
  context_object_name = 'event'
  template_name = 'events/fullInformation.html'

  def get_context_data(self, **kwargs):
    context = super(FullInformation, self).get_context_data(**kwargs)
    context['form'] = Unregistered_user_form()
    return context

  def post(self,  request, pk):
    form = Unregistered_user_form(request.POST)
    if form.is_valid():
      form.save()
      last_user = Unregistered_user.objects.last()
      listing = Listing.objects.only('id').get(id=pk)
      new_subscription = Event_subscriptions(event_id=listing, unregistered_user_id=last_user)
      new_subscription.save()
      return redirect('events/registered.html')