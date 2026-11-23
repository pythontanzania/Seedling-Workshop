# Seedling: PyCon Tanzania 2026 Django workshop

Seedling is a fundraiser tracker: fundraisers, pledges, pretend mobile-money
payments and an organiser login. It's built step by step in the workshop
handout.

Each `chapter-N/` folder is the project as it stands **at the end of chapter N**
of the handout. `chapter-7/` is the finished app, with tests.

| Folder | Handout chapter |
|---|---|
| `chapter-1/` | 1. Setting up your laptop |
| `chapter-2/` | 2. Python warm-up (`warmup.py`) |
| `chapter-3/` | 3. Models, migrations and the admin |
| `chapter-4/` | 4. The public page and progress bar |
| `chapter-5/` | 5. The pledge form |
| `chapter-6/` | 6. The pretend Lipa payment |
| `chapter-7/` | 7. Organiser login (finished app) |

## Run a chapter

You need Python 3.14. On Windows, use `python`; on Mac or Linux, use `python3`
until the virtual environment is switched on.

```
cd chapter-7
python -m venv venv
venv\Scripts\activate
pip install -r ../requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

On Mac or Linux, activate with `source venv/bin/activate` instead.
Then open http://127.0.0.1:8000. Run the finished app's tests with
`python manage.py test`.

The `SECRET_KEY` in `settings.py` is for learning on your own laptop only.
Before putting a project on the internet, see Extra A in the handout.
