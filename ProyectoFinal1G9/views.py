from django.shortcuts import render

def Base(request):

	return render(request,'base.html')

def Index(request):

    return render(request,'index.html')

def Anime_Details(request):

    return render(request,'anime-details.html')

def Anime_Watching(request):

    return render(request,'anime-watching.html')

def Login(request):

    return render(request,'login.html')

def SignUp(request):

    return render(request,'signup.html')

def Category(request):

    return render(request,'categories.html')

def Blog(request):

    return render(request,'blog.html')

def Blog_Details(request):

    return render(request,'blog-details.html')

def Search_Result(request):

    return render(request,'search-result.html')

def Main(request):

    return render(request,'main.html')