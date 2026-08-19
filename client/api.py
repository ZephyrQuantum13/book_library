import requests
import os

BASE_URL = os.getenv("BASE_URL")

# CRUD operations for books for the client

def get_books():
    r = requests.get(f"{BASE_URL}/books", timeout=5)
    r.raise_for_status()
    return r.json()

def get_book(book_id):
    r = requests.get(f"{BASE_URL}/books/{book_id}", timeout=5)
    r.raise_for_status()
    return r.json()

def create_book(book):
    r = requests.post(f"{BASE_URL}/books", json=book, timeout=5)
    r.raise_for_status()
    return r.json()

def update_book(book_id, book):
    r = requests.put(f"{BASE_URL}/books/{book_id}", json=book, timeout=5)
    r.raise_for_status()
    return r.json()

def delete_book(book_id):
    r = requests.delete(f"{BASE_URL}/books/{book_id}", timeout=5)
    r.raise_for_status()
    return r.json()