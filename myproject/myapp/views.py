from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, BookForm, RecordForm, ReturnRecordForm
from .models import User, Book, Record
from django.utils import timezone
from django.contrib import messages


# Dashboard
def dashboard(request):
    context = {
        'users_count': User.objects.count(),
        'books_count': Book.objects.count(),
        'open_records_count': Record.objects.filter(status='open').count(),
        'closed_records_count': Record.objects.filter(status='closed').count(),
    }
    return render(request, 'dashboard.html', context)

# Users

def users(request):
    users = User.objects.all()
    locked_user_ids = set(
        Record.objects.filter(status='open').values_list('user_id', flat=True)
    )
    return render(
        request,
        'users.html',
        {
            'users': users,
            'locked_user_ids': locked_user_ids,
        }
    )


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        # Status is assigned internally when creating a user!!!
        form.fields['status'].required = False
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 1     # Active User (newly added!!)
            user.save()
            return redirect('users')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def edit_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        form.fields['status'].required = False
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users')
    else:
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form})


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    has_open_record = Record.objects.filter(user=user, status='open').exists()
    if has_open_record:
        messages.error(
            request,
            'This user cannot be deleted because they have an active borrowed book.'
        )
        return redirect('users')

    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('users')


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_detail.html', {'user': user})


# Books

def books(request):
    books = Book.objects.all()
    locked_book_ids = set(
        Record.objects.filter(status='open').values_list('book_id', flat=True)
    )
    return render(
        request,
        'books.html',
        {
            'books': books,
            'locked_book_ids': locked_book_ids,
        }
    )


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']
            stock = form.cleaned_data['stock']

            # Checking if book already exists...
            existing_book = Book.objects.filter(
                title=title,
                author=author,
                genre=genre
            ).first()

            if existing_book:
                # Update stock instead of creating new entry of BOOK!!!
                existing_book.stock += stock
                existing_book.save()
            else:
                form.save()

            return redirect('books')

    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']
            stock = form.cleaned_data['stock']

            if stock == 0:
                # Check if the book is borrowed...
                has_open_record = Record.objects.filter(book=book, status='open').exists()
                if has_open_record:
                    messages.error(
                        request,
                        'This book cannot be deleted because it is currently borrowed.'
                    )
                    return render(request, 'edit_book.html', {'form': form})
                else:
                    # Safe to delete
                    book.delete()
                    messages.success(request, 'Book deleted successfully.')
                    return redirect('books')

            # Checking if book already exists...
            existing_book = Book.objects.filter(
                title=title,
                author=author,
                genre=genre
            ).exclude(id=book.id).first()

            if existing_book:
                # Update stock instead of creating new entry of BOOK!!!
                existing_book.stock += stock
                existing_book.save()
                book.delete()
            else:
                form.save()

            return redirect('books')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    has_open_record = Record.objects.filter(book=book, status='open').exists()
    if has_open_record:
        messages.error(
            request,
            'This book cannot be deleted because it is currently borrowed.'
        )
        return redirect('books')

    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('books')


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_details.html', {'book': book})


# Records

def borrow_book(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['user']
            selected_book = form.cleaned_data['book']

            if Record.objects.filter(user=selected_user, status='open').exists():
                form.add_error('user', 'This user already has an active borrowed book and cannot borrow another one.')

            if selected_book.available_books() <= 0:
                form.add_error('book', 'This book is currently unavailable.')

            if form.errors:
                return render(request, 'borrow_book.html', {'form': form})

            form.save()
            messages.success(request, 'Book borrowed successfully.')
            return redirect('open_records')
    else:
        form = RecordForm()

    return render(request, 'borrow_book.html', {'form': form})


def open_records(request):
    records = Record.objects.filter(status='open')
    context = {
        'open_records': records,

        'return_form': ReturnRecordForm(),
    }
    return render(request, 'open_records.html', context)


def return_book(request, id):
    record = get_object_or_404(Record, id=id)

    record.return_date = timezone.now().date() 
    record.status = 'closed'                     
    record.save()

    return redirect('open_records')

def closed_records(request):
    records = Record.objects.filter(status='closed')
    return render(request, 'closed_records.html', {'closed_records': records})


def record_detail(request, id):
    record = Record.objects.get(id=id)
    return render(request, 'record_details.html', {'record': record})