from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Plan
from .generate.plan import generate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def detail(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)

    context = {'plan': plan}
    return render(request, 'plan.html', context)

def new(request):
    text = generate()
    plan = Plan(text=text)
    plan.save()
    return redirect(detail, plan.pk)