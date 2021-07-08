from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import GaokaoSchool


@login_required
def schooltop(request):
    #采集时间选项
    updatedts = GaokaoSchool.objects.values('updatedt').order_by(
        '-updatedt').distinct()
    schools = GaokaoSchool.objects.all()
    schools = schools.filter(updatedt__exact=updatedts[0]['updatedt']).order_by(
        "-star", "name")[:50]
    page_info = {
        'title': '阳光高考-院校库top',
        'html': 'schooltop.html',
    }
    return render(request, 'frame.html', locals())


@login_required
def schoollist(request):
    #采集时间选项
    updatedts = GaokaoSchool.objects.values('updatedt').order_by(
        '-updatedt').distinct()
    page_info = {
        'title': '阳光高考-院校库all',
        'html': 'schoollist.html',
        'script': 'schoollist.js',
    }
    return render(request, 'frame.html', locals())