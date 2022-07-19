from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib import messages

from .models import honam
from .models import users
import os

# Create your views here.
def main(request):
	if request.method == 'POST':
		uname = request.POST.get('userid')
		upasswd = request.POST.get('userpasswd')

		all_user = users.objects.all()
		if not all_user.filter(username=uname, userpasswd=upasswd).exists(): #아이디 혹은 비밀번호가 틀렸을 때 
			messages.warning(request, '아이디 혹은 비밀번호가 틀렸습니다')
			return render(request, 'Aim2cs_app/sign_in.html')

		else:
			session_id = request.session.get('userid', uname)

	return render(request, 'Aim2cs_app/main.html')

def upload(request):
	return render(request, 'Aim2cs_app/upload.html')

def upload_confirm(request):
	if request.method == 'POST':

		#업로드 이미지 저장
		f = request.FILES['file']
		cnt = len(os.listdir('media/')) + 1
		f.name = ('%.6d%s' %(cnt, f.name[-4:]))

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

		if category_list: #카테고리 
			honam_condition.add(Q(category__in=category_list), Q.AND)

		if season_list:	#계절
			honam_condition.add(Q(season__in=season_list), Q.AND)

		if weather_list: #날씨
			honam_condition.add(Q(weather__in=weather_list), Q.AND)

		if nature_list: #자연 
			honam_condition.add(Q(nature__in=nature_list), Q.AND)

		if place_list: #장소 
			honam_condition.add(Q(place__in=place_list), Q.AND)
		
		honam_db = honam.objects.filter(honam_condition).distinct()

		return render(request, 'Aim2cs_app/select_view.html', context={"honam_db": honam_db})

def sign_up(request):
	return render(request, 'Aim2cs_app/sign_up.html')

def sign_in(request):

	#sign up에서 넘어오는 로그인 페이지일 때 
	if request.method == 'POST':
		all_user = users.objects.all()

		uname = request.POST.get('userid')
		if all_user.count() != 0:
			if all_user.filter(username=uname).exists(): #해당 아이디는 존재하는 아이디임 
				return render(request, 'Aim2cs_app/sign_up.html', context={"sign_alert": "nop"})

		upasswd = request.POST.get('passwd')
		newface = users()
		newface.username = uname
		newface.userpasswd = upasswd
		newface.save()

	return render(request, 'Aim2cs_app/sign_in.html', context={"sign_alert": "good"})

