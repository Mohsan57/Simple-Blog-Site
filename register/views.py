from django.shortcuts import render, HttpResponse
from register.form import Registration_form, login_form, user_image, Article
from register.models import Register, User_Image, Articles
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path

# Create your views here.


def index(request):
    blogs = Articles.objects.all()
    return render(request, 'html/home.html', {
        'blogs': blogs,
    })


def success_message(request, user_slug):
    user = Register.objects.get(slug=user_slug)
    return render(request, 'html/Message Card/success.html', {
        'user': user,
    })


def failed_message(request):
    return render(request, 'html/Message Card/failed.html')


def user_detail(request, user_slug):
    try:
        find_slug = Register.objects.get(slug=user_slug)
        link2 = find_slug.user_photo.photo
        blogs_post = False
        try:
            blogs = Articles.objects.filter(writer__slug=find_slug.slug).all()
            blogs_post = True
        except:
            blogs_post = False
        print(blogs_post)
        return render(request, 'html/profile/profile.html', {
            'found': True,
            'user_detail': find_slug,
            'photo_link': link2,
            'found_blog': blogs_post,
            'blogs': blogs,
        })
    except:
        return render(request, 'html/profile/profile.html', {
            'found': False,
        })


def login_user(request):
    if(request.method == 'POST'):
        form = login_form(request.POST)
        if(form.is_valid()):
            try:
                u_name = form.cleaned_data.get('user_name')
                u_password = form.cleaned_data.get('password')
                user = Register.objects.get(user_name=u_name)
                if(user.user_name == u_name and user.password == u_password):
                    return redirect('profile', user_slug=user.slug)
                else:
                    return render(request, 'html/login.html', {
                        'try': True,
                        'form': form,
                    })
            except:
                return render(request, 'html/login.html', {
                    'try': True,
                    'form': form,
                })
    else:
        form = login_form()
        return render(request, 'html/login.html', {
            'try': False,
            'form': form,
        })


def blog_post(request, user_slug):
    try:
        selected_user = Register.objects.get(slug=user_slug)
        if (request.method == "POST"):
            form = Article(request.POST, request.FILES)
            if(form.is_valid()):
                title = form.cleaned_data.get('title')
                cover_photo = form.cleaned_data.get('cover_photo')
                content = form.cleaned_data.get('content')
                tag = form.cleaned_data.get('tag')
                blog = Articles.objects.create(
                    writer=selected_user, title=title, cover_photo=cover_photo, content=content, tag=tag)
                blog.save()
                return redirect('profile', user_slug=selected_user.slug)
        else:
            form = Article
        return render(request, 'html/profile/blog/new_blog.html', {
            'found': True,
            'form': form,
            'user': selected_user,
        })
    except:
        return render(request, 'html/profile/blog/new_blog.html', {
            'found': False,
        })


def Register_user(request):
    if(request.method == 'POST'):
        forms = Registration_form(request.POST)
        user_form = user_image(request.POST, request.FILES)
        if(forms.is_valid() and user_form.is_valid()):
            try:
                u_name = forms.cleaned_data.get('user_name')
                f_name = forms.cleaned_data.get('first_name')
                l_name = forms.cleaned_data.get('last_name')
                dob = forms.cleaned_data.get('date_of_birth')
                mail = forms.cleaned_data.get('email')
                passwd = forms.cleaned_data.get('password')
                con_password = forms.cleaned_data.get('confirm_password')
                photo = user_form.cleaned_data.get('photo')
                if(passwd == con_password):
                    u_photo, _ = User_Image.objects.get_or_create(photo=photo)
                    user = Register.objects.create(
                        first_name=f_name, user_name=u_name, last_name=l_name, date_of_birth=dob, email=mail, password=passwd, user_photo=u_photo)
                    user.save()
                    user_slug = Register.objects.get(user_name=u_name)
                    return redirect('success_message', user_slug.slug)
                else:
                    return render(request, 'html/registration.html', {
                        'form': forms,
                        'user_photo_form': user_form,
                        'pass_equal': True,
                    })

            except:
                return redirect('failed_message')
    else:
        forms = Registration_form
        user_form = user_image
    return render(request, 'html/registration.html', {
        'form': forms,
        'pass_equal': False,
        'user_photo_form': user_form,
    })


def blog(request, blog_slug):
    try:
        blog = Articles.objects.get(slug=blog_slug)
        return render(request, 'html/blog/blogs.html', {
            'found': True,
            'blog': blog
        })
    except:
        return render(request, 'html/blog/blogs.html', {
            'found': False,
        })


def user_blogs(request, user_slug):
    try:
        selected_user = Register.objects.get(slug=user_slug)
        try:
            blogs = Articles.objects.filter(writer__slug=selected_user.slug)
            return render(request, 'html/blog/user_blogs.html', {
                'user_found': True,
                'selected_user': selected_user,
                'blogs': blogs,
                'blog_found': True
            })
        except:
            print("blog not ok")
            return render(request, 'html/blog/user_blogs.html', {
                'selected_user': selected_user,
                'user_found': True,
            })
    except:
        return render(request, 'html/blog/user_blogs.html', {
            'user_found': False,
        })


def page_not_found_view(request, exception):
    return render(request, 'html/error_msg.html', status=404)
