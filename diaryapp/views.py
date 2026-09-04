from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

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

            messages.success(
                request,
                'Your account has been created successfully!'
            )

            return redirect('dashboard')

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

            messages.success(
                request,
                f'Welcome back, {user.username}!'
            )

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'diaryapp/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out successfully.'
    )

    return redirect('home')


@login_required
def dashboard(request):

    entries = DiaryEntry.objects.filter(
        user=request.user
    )

    total_entries = entries.count()

    pinned_entries = entries.filter(
        is_pinned=True
    ).count()

    category_count = entries.values(
        'category'
    ).distinct().count()

    current_month_entries = entries.filter(
        created_at__month=__import__('datetime').date.today().month,
        created_at__year=__import__('datetime').date.today().year
    ).count()

    recent_entries = entries[:5]

    context = {
        'total_entries': total_entries,
        'pinned_entries': pinned_entries,
        'category_count': category_count,
        'current_month_entries': current_month_entries,
        'recent_entries': recent_entries,
    }

    return render(
        request,
        'diaryapp/dashboard.html',
        context
    )


@login_required
def diary_list(request):

    entries = DiaryEntry.objects.filter(
        user=request.user
    )

    search_query = request.GET.get(
        'q',
        ''
    ).strip()

    category = request.GET.get(
        'category',
        ''
    )

    if search_query:

        entries = entries.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    if category:

        entries = entries.filter(
            category=category
        )

    categories = DiaryEntry.CATEGORY_CHOICES

    return render(
        request,
        'diaryapp/diary_list.html',
        {
            'entries': entries,
            'search_query': search_query,
            'selected_category': category,
            'categories': categories,
        }
    )


@login_required
def create_entry(request):

    if request.method == 'POST':

        form = DiaryEntryForm(
            request.POST
        )

        if form.is_valid():

            entry = form.save(
                commit=False
            )

            entry.user = request.user

            entry.save()

            messages.success(
                request,
                'Diary entry created successfully!'
            )

            return redirect(
                'diary_detail',
                entry_id=entry.id
            )

    else:

        form = DiaryEntryForm()

    return render(
        request,
        'diaryapp/diary_form.html',
        {
            'form': form,
            'entry': None
        }
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
        {
            'entry': entry
        }
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

            messages.success(
                request,
                'Diary entry updated successfully!'
            )

            return redirect(
                'diary_detail',
                entry_id=entry.id
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

        messages.success(
            request,
            'Diary entry deleted.'
        )

        return redirect(
            'diary_list'
        )

    return render(
        request,
        'diaryapp/confirm_delete.html',
        {
            'entry': entry
        }
    )


@login_required
def profile(request):

    user = request.user

    entry_count = DiaryEntry.objects.filter(
        user=user
    ).count()

    return render(
        request,
        'diaryapp/profile.html',
        {
            'profile_user': user,
            'entry_count': entry_count,
        }
    )