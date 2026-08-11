# Hapja dhe Ekzekutimi i një Projekti Django nga Repository

## 1. Merrni projektin nga Repository
Hapni repository-n e projektit ne GitHub:  https://github.com/zelina256/projektDjango-11.git.
Kopjoni URL-në e repository-t, tek seksioni Code: https://github.com/zelina256/projektDjango-11.git
Me pas hapni terminalin ne folderin ku deshironi te ruani projektin dhe ekzekutoni: git clone https://github.com/zelina256/projektDjango-11.git

## 2. Hapni projektin në Visual Studio Code dhe sigurohuni qe te kete kete strukture
File → Open Folder -> Pastaj zgjidhni folderin e projektit.
projekt/
│
├── manage.py
├── db.sqlite3
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── aplikacion/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
## 3. Hapni terminalin 
Sigurohuni qe te jeni brenda folderit te projektit
## 4. Krijoni Virtual Environment
Ne Windows:
python -m venv venv
Në macOS/Linux:
python3 -m venv venv
## 5. Aktivizoni Virtual Environment
### Windows – Command Prompt
venv\Scripts\activate
### macOS/Linux
source venv/bin/activate
Nëse virtual environment është aktivizuar me sukses, zakonisht në terminal do të shfaqet:(venv)
## 6. Instaloni django
pip install django
## 7. Hapni Django Server (komanda behet ne terminal)
python manage.py runserver
## 8. Hapni projektin në Browser
http://127.0.0.1:8000/
