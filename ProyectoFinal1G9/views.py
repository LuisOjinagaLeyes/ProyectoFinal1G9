from django.shortcuts import render

def Base(request):

	return render(request,'base.html')

def Index(request):

    return render(request,'index.html')

def Anime_Details(request):

    return render(request,'anime-details.html')

#borrar luego de verificar que es el correcto
# def Anime_Watching(request):

#     return render(request,'anime-watching.html')

#Muy posible borrar lo de abajo comentado.

# def Login(request):

#     return render(request,'login.html')

# def Registro(request):

#     return render(request,'registro.html')

# def Categoria(request):

#     return render(request,'categoria.html')

def Blog(request):

    return render(request,'blog.html')

def Blog_Details(request):

    return render(request,'blog-details.html')

def Search_Result(request):

    return render(request,'search-result.html')

