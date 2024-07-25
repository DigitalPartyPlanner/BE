from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import date

@login_required
def myroom_own (request,user_id):
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    birthday = owner.birthday

    if birthday:
        today = date.today()
        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday < today:
            next_year_birthday = birthday.replace(year=today.year+1)
            d_day = (next_year_birthday - today).days
        else:
            d_day = (this_year_birthday - today).days
        
        birthday = birthday.strftime('%m월 %d일')
    else:
        d_day = None
        birthday = birthday.strftime('%m월 %d일')

    context={
        'owner':owner, 
        'birthday':birthday,
        'd_day':d_day,
        }
    return render (request,'myroom/room_own.html',context)

def cake_custom (request):
    return render (request,'myroom/cakemaker.html')