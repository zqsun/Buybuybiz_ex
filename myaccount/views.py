from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
	projectsCount = bizProject.objects.filter(sold_by=request.user).count()
	context = {'projectsCount': projectsCount}
	return render(request, 'myaccount/index.html', context)