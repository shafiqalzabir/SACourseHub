from django.shortcuts import render, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from django.conf import settings
from django.contrib import messages
# Create your views here.

def get_google_sheet_user_data():
    
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    json_path = os.path.join(settings.BASE_DIR, 'credentials.json')
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
    client = gspread.authorize(creds)
    return client.open("SACourseHub_user_data").sheet1


def index(request):
    return render(request, 'index.html')


def my_courses(request):
    return render(request, 'my_courses.html')


def registration(request):
    if request.method == "POST":
        # HTML এর 'name' অনুযায়ী ডাটা রিসিভ করা
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')
        
        try:
            # গুগল শিটের সাথে কানেক্ট হওয়া
            sheet = get_google_sheet_user_data()

            # ২ নম্বর কলাম থেকে সব ফোন নম্বর নেওয়া (যেহেতু ফোন আমাদের ইউনিক আইডি)
            existing_phones = sheet.col_values(2)

            if user_phone in existing_phones:
                # যদি ফোন নম্বর আগে থেকেই থাকে
                messages.error(request, f"ফোন নম্বর {user_phone} দিয়ে আগেই রেজিস্ট্রেশন করা আছে। দয়া করে লগইন করুন!")
            else:
                # যদি নতুন ইউজার হয়, শিটে ডাটা অ্যাড করা
                new_data = [user_name, user_phone, user_email]
                sheet.append_row(new_data)
                messages.success(request, "অভিনন্দন! আপনার রেজিস্ট্রেশন সফলভাবে সম্পন্ন হয়েছে।")
        
        except Exception as e:
            # কোনো এরর হলে (যেমন ইন্টারনেট সমস্যা বা ফাইল পাথ ভুল হলে)
            print(f"Error: {e}")
            messages.error(request, "সার্ভারে সমস্যা হয়েছে। দয়া করে কিছুক্ষণ পর আবার চেষ্টা করুন।")

        # কাজ শেষ হলে একই পেজে রিডাইরেক্ট করবে
        return redirect('/login')
    
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def creator_registration(request):
    return render(request, 'creator_registration.html')


def math_foundation_course(request):
    return render(request, 'math_foundation_course.html')


def math_foundation_class(request):
    return render(request, 'math_foundation_class.html')
