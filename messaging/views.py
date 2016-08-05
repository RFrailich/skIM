from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import MessageForm


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'messaging/detail.html'


def convo(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    curr_user = request.user

    # Will eventually support group conversations, for now we'll just get the one
    conversation = user.conversation_set.get(pk__in=curr_user.conversation_set.all())
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sent_date = timezone.now()
            message.conversation_id = conversation.id
            message.save()
    return render(request, 'conversations/detail.html', {'form': form, 'user': user_id,
      'conversation': conversation})  



class UserIndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/messaging/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'messaging/list.html'
    context_object_name = 'users'


def search(request):
    query = request.GET.get('query')
    qset = Q()
    if query:
        qset |= Q(username__contains=query)
    results = User.objects.filter(qset)
    return render(request, 'messaging/results.html', {'results': results, 'query': query})