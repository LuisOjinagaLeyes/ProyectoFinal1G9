from django.shortcuts import render

def Base(request):

	return render(request,'base.html')

def Index(request):

    return render(request,'index.html')

def Anime_Details(request):

    return render(request,'anime-details.html')

# def About(request):

#     return render(request,'about.html')

def Categories(request):

    return render(request,'categories.html')

# def Blog(request):

#     return render(request,'blog.html')

# def Search_Result(request):

#     return render(request,'search-result.html')

# def Single(request):

#     return render(request,'single.html')

