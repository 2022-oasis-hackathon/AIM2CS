from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from .models import honam
import os

# Create your views here.
def main(request):
	return render(request, 'Aim2cs_app/main.html')

def upload(request):
	return render(request, 'Aim2cs_app/upload.html')

def upload_confirm(request):
	if request.method == 'POST':

		#업로드 이미지 저장
		f = request.FILES['file']
		cnt = len(os.listdir('media/')) + 1
		f.name = ('%.6d%s' %(cnt, f.name[-4:]))
		print(f.name)

		category = request.POST.get('category')
		season = request.POST.get('season')
		weather = request.POST.get('weather')
		nature = request.POST.get('nature')
		place = request.POST.get('place')

		Honam = honam()
		Honam.uploadedFile = f
		Honam.category = category
		Honam.dir_name = f.name
		Honam.season = season
		Honam.weather = weather
		Honam.nature = nature
		Honam.place = place
		Honam.save()

		return render(request, 'Aim2cs_app/upload_confirm.html', context={"files": Honam})

def select_view(request):
	if request.method == 'POST':
		honam_condition= Q()
		category_list = request.POST.getlist('category')
		season_list = request.POST.getlist('season')
		weather_list = request.POST.getlist('weather')
		nature_list = request.POST.getlist('nature')
		place_list = request.POST.getlist('place')

		if category_list:
            honam_condition.add(Q(category__in=category_list), Q.AND)
            honam_db = honam.objects.filter(category__in=category_list).distinct()

        if season_list:
            honam_condition.add(Q(season__in=season_list), Q.AND)
            honam_db = honam.objects.filter(season__in=season_list).distinct()

        if weather_list:
            honam_condition.add(Q(weather__in=weather_list), Q.AND)
            honam_db = honam.objects.filter(weather__in=weather_list).distinct()

        if nature_list:
            honam_condition.add(Q(nature__in=nature_list), Q.AND)
            honam_db = honam.objects.filter(nature__in=weather_list).distinct()

        if place_list:
            honam_condition.add(Q(place__in=place_list), Q.AND)
            honam_db = honam.objects.filter(place__in=place_list).distinct()

        return render(request, 'Aim2cs_app/select_view.html', context={"honam_db": honam_db})