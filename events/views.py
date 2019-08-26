from django.shortcuts import HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, FormView
from .models import Listing, Event_subscriptions, Unregistered_user, Comments
from .forms import Unregistered_user_form, Comments_form
from django.contrib import messages


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
    '''
    This takes in self and kwargs which is an object here.
    It sets context to have a an instance of the unregistered_user_form
    class and a comments_form class. It then returns the context.
    '''
    context = super(FullInformation, self).get_context_data(**kwargs)
    context['user_form'] = Unregistered_user_form()
    context['comments_form'] = Comments_form()
    return context

  def post(self,  request, pk):
    '''
    This takes in self, the request from post and the primary key, pk,
    of the event listing. It checks if the user form is valid and saves
    it if it is but if it is invalid e.g. the user already exists it will pass.
    Then it checks the comments form is valid and if it passes then it checks 
    the user hasn't already signed up to this event, if they haven't then
    it stores their info in the comments table and event subscription table
    and redirects to the home page. If they have then it redirects to the current
    page with a message.
    '''
    user_form = Unregistered_user_form(request.POST, 'user_form')
    comments_form = Comments_form(request.POST, 'comments_form')
    listing = Listing.objects.only('id').get(id=pk)
    if user_form.is_valid():
      user_form.save()
    if comments_form.is_valid():
      user = Unregistered_user.objects.filter(email=request.POST['email']).first()
      if Event_subscriptions.objects.filter(event_id=listing, unregistered_user_id=user).count() == 0:
        comments = comments_form.save(commit=False)
        comments.unregistered_user_id = user
        comments.event_id = listing
        comments.save()
        new_comment = Comments.objects.latest('id')
        new_subscription = Event_subscriptions(
          event_id=listing,
          unregistered_user_id=user,
          user_comments=new_comment
        )
        new_subscription.save()
        messages.success(request, "You are attending" + " " + listing.title)
        return redirect('events-home')
      else:
        messages.error(request, "You are already attending this event.")
        return HttpResponseRedirect(self.request.path_info)
    else:    
      messages.error(request, "Invalid input")
      return HttpResponseRedirect(self.request.path_info)     