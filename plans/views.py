from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Plan
from .generate.plan import generate

# Create your views here.

def index(request):
    context = {
        'top': Plan.objects.all().order_by('-views')[:10],
        'recent': Plan.objects.all().order_by('-pk')[:10]
    }
    return render(request, 'index.html', context)

def detail(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)

    if isinstance(plan, Plan):
        plan.views += 1
        plan.save()

    context = { 'plan': plan }
    return render(request, 'detail.html', context)

def new(request):
    text = generate()
    plan, _ = Plan.objects.get_or_create(text=text)
    return redirect(detail, plan.pk)

# def latest(request):
#     plans = Plan.objects.all().order_by('-pk')[:10]
#     context = {'plans': plans}
#     return render(request, 'latest.html', context)

# def top(request):
#     plans = Plan.objects.all().order_by('-views')[:10]
#     context = {'plans': plans}
#     return render(request, 'top.html', context)
