from django.shortcuts import render , redirect
from django.http import HttpResponse , request
from django.template import loader
import openai
from tinymce.models import HTMLField
from .models import help_db , review_db
# Create your views here.




def index(request):
    if request.method == "POST":
        userQuery = request.POST.get("query")
        print(userQuery)

        # openai code for get answer
        try:
            openai.api_key = "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"
            messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
            message = userQuery
            messages.append({"role": "user", "content": message},)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            message = ""
            return render(request , "index.html" , {"queryReply" : reply})
        except:
            print("error....")

    else:
        print("nothing....")

    return render(request , "index.html")
    
    # render(request , "index.html")

def about(request):
    return render(request , "about.html")

def contact(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phonenum = request.POST.get("phone")
        message = request.POST.get("message")
        # print(fname,lname,email,message,phonenum)
        data = help_db(first_name=fname , last_name=lname , e_mail=email , phone_num=phonenum , message_query=message)
        data.save()

    return render(request , "contact.html")

def review(request):
    try:
        if request.method == "GET":
            reviewer_Name = request.GET.get("reviewerName")
            reviewer_Message = request.GET.get("reviewerMessage")

            if request.GET.get("star1"):
                reviewer_Star = 1
                data_review = review_db(name = reviewer_Name , message = reviewer_Message , star_rating = reviewer_Star)
                data_review.save()
            elif request.GET.get("star2"):
                reviewer_Star = 2
                data_review = review_db(name = reviewer_Name , message = reviewer_Message , star_rating = reviewer_Star)
                data_review.save()
            elif request.GET.get("star3"):
                reviewer_Star = 3
                data_review = review_db(name = reviewer_Name , message = reviewer_Message , star_rating = reviewer_Star)
                data_review.save()
            elif request.GET.get("star4"):
                reviewer_Star = 4
                data_review = review_db(name = reviewer_Name , message = reviewer_Message , star_rating = reviewer_Star)
                data_review.save()
            elif request.GET.get("star5"):
                reviewer_Star = 5
                data_review = review_db(name = reviewer_Name , message = reviewer_Message , star_rating = reviewer_Star)
                data_review.save()
            else:
                print("no data review page found")       
    except:
        print("error in reviewer")

    review = review_db.objects.all()
    review_ = {
        "review_data" : review
    }
        
    return render(request , "review.html" , review_)