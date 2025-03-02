from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta
from .models import Posts, Comments
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    # print(
    #     "hello i ma registration modeule----------------------------------------------------------------------------------------------------------------------------"
    # )
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        user_data_error = False
        if User.objects.filter(username=username).exists():
            messages = "username already exists"
            user_data_error = True
        if User.objects.filter(email=email).exists():
            messages = "Email already exists"
            user_data_error = True
        if user_data_error:
            return render(request, "register.html", {"messages": messages})

        if not user_data_error:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            messages = f"Sucessfully registered {first_name}"
            return redirect("login_view")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("Home")
        else:
            messages = "Invalid Login Credentials"
            return render(request, "login.html", {"messages": messages})

    return render(request, "login.html")


@login_required
def Home(request):
    posts = Posts.objects.all().order_by("-date_added")

    return render(request, "Home.html", {"posts": posts})


def Logout_view(request):
    logout(request)
    return redirect("login_view")


@login_required
def view_post(request, post_id):

    post = Posts.objects.get(id=post_id)
    comments = Comments.objects.filter(post_name=post).order_by("-date_added")
    comment_count = comments.count()
    return render(
        request,
        "post_details.html",
        {"post": post, "comments": comments, "comment_count": comment_count},
    )


@login_required
def search_post(request):
    if request.method == "POST":
        search = request.POST["search"]
        posts = Posts.objects.filter(title__icontains=search)
        return render(request, "search_posts.html", {"posts": posts})

    return render(request, "search_posts.html")


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        photo = request.FILES.get("photo")
        post = Posts(title=title, body=body, author=request.user, photo=photo)
        post.save()
        return redirect("Home")

    return render(request, "post_create.html")


@login_required
def edit_post(request, post_id):
    posti = get_object_or_404(Posts, pk=post_id, author=request.user)
    if request.method == "POST":
        posti.title = request.POST["title"]
        posti.body = request.POST["body"]
        if "photo" in request.FILES:
            posti.photo = request.FILES["photo"]

        # post = Posts(title=title, body=body, author=request.user, photo=photo)
        posti.save()
        return redirect("Home")

    return render(request, "post_create.html", {"post": posti})


@login_required
def delete_post(request, post_id):
    posti = get_object_or_404(Posts, pk=post_id, author=request.user)
    posti.delete()
    return redirect("Home")


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    if request.method == "POST":
        comment_body = request.POST["comment"]
        new_comment = Comments(
            name=request.user, post_name=post, comment_body=comment_body
        )
        new_comment.save()
        return redirect("view_post", post_id=post_id)  # Fix redirection

    comments = Comments.objects.filter(post_name=post).order_by("-date_added")
    comment_count = comments.count()
    # Fix to retrieve multiple comments
    return render(
        request,
        "post_details.html",
        {"post": post, "comments": comments, "comment_count": comment_count},
    )
