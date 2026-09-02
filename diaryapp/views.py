from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import DiaryEntry
from .forms import DiaryEntryForm, RegisterForm


def home(request):
    return render(request, 'diaryapp/home.html')


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('diary_list')

    else:
        form = RegisterForm()

    return render(
        request,
        'diaryapp/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('diary_list')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'diaryapp/login.html',
        {'form': form}
    )


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def diary_list(request):

    entries = DiaryEntry.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'diaryapp/diary_list.html',
        {'entries': entries}
    )


@login_required
def create_entry(request):

    if request.method == 'POST':

        form = DiaryEntryForm(request.POST)

        if form.is_valid():

            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect(
                'diary_detail',
                entry.id
            )

    else:
        form = DiaryEntryForm()

    return render(
        request,
        'diaryapp/diary_form.html',
        {'form': form}
    )


@login_required
def diary_detail(request, entry_id):

    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    return render(
        request,
        'diaryapp/diary_detail.html',
        {'entry': entry}
    )


@login_required
def edit_entry(request, entry_id):

    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':

        form = DiaryEntryForm(
            request.POST,
            instance=entry
        )

        if form.is_valid():
            form.save()

            return redirect(
                'diary_detail',
                entry.id
            )

    else:

        form = DiaryEntryForm(
            instance=entry
        )

    return render(
        request,
        'diaryapp/diary_form.html',
        {
            'form': form,
            'entry': entry
        }
    )


@login_required
def delete_entry(request, entry_id):

    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':

        entry.delete()

        return redirect('diary_list')

    return render(
        request,
        'diaryapp/confirm_delete.html',
        {'entry': entry}
    )