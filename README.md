# Django-Backend-MTV

## Purpose
This Django REST back end models a campus-style library: it keeps track of users, employees, libraries, copies, publications, and the loans that connect them. Each domain entity lives in its own Django app (autor, editora, livro, biblioteca, funcionario, exemplar, usuario, emprestimo) and is exposed through a `ModelViewSet`, so the project can power dashboards, portals, or mobile apps that need CRUD access to the catalog and circulation history.

<img width="1530" height="912" alt="Image" src="https://github.com/user-attachments/assets/4eea1534-1a18-4480-9d09-ca4626a7dad8">


## Requirements
- Python 3.11+ (Django 5.2.8 requires modern Python)
- [`Django==5.2.8`](https://www.djangoproject.com/) for the core framework
- [`djangorestframework`](https://www.django-rest-framework.org/) to expose serializers + viewsets
- [`python-decouple`](https://pypi.org/project/python-decouple/) for `.env`-based configuration
- Oracle client driver (`oracledb` or `cx_Oracle`) because the project uses `django.db.backends.oracle`
- [`Pillow`](https://pypi.org/project/Pillow/) to satisfy the `ImageField` defined on `Exemplar`
- [`django-filter`](https://django-filter.readthedocs.io/) is imported in `livro.views` and should be installed if filtering becomes necessary

## Installation
1. Clone the repository and enter the folder:
   ```bash
   git clone <repo> .
   cd Django-Backend-MTV.priv-main
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install Django==5.2.8 djangorestframework python-decouple oracledb Pillow django-filter
   ```
   Replace `oracledb` with `cx_Oracle` if you prefer that driver and have the Oracle client libraries installed.
4. Prepare the database (see **Configuration** for the expected Oracle environment variables) and run:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create a superuser for the admin:
   ```bash
   python manage.py createsuperuser
   ```

## Configuration (env)
`bibliotecaapp/settings.py` loads the following variables via `python-decouple` from a `.env` file in the project root. Create a file like this:

```
SECRET_KEY=replace-with-a-long-random-string
DEBUG=True  # switch to False in production
DB_NAME=XE
DB_USER=system
DB_PASSWORD=YourOraclePassword
```

- `DEBUG` defaults to `False` when unset because the setting casts to `bool` and uses `False` as the default.
- `DATABASES` uses the Oracle backend, so you must provide credentials and have the Oracle Instant Client installed.
- `ALLOWED_HOSTS` is empty by default; update it before deploying to a hostname.
- `STATIC_URL` is set to `static/`, and because no `MEDIA_ROOT` is defined you must provide one if you plan to upload `Exemplar.foto_capa` images.
- Locale is configured for `pt-br` with the `America/Sao_Paulo` timezone.

## Running
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. The API root is `http://127.0.0.1:8000/`. Each router registers its `ModelViewSet` under a top-level path such as `/livro/`, `/usuario/`, etc.
3. Use the admin dashboard at `http://127.0.0.1:8000/admin/` once you have created a superuser and manually register models if desired.

## Usage
### Available resources
| Resource | Base URL | Description |
| --- | --- | --- |
| Autores | `/autor/` | Manage author metadata (name, nationality, birth date, sex). |
| Editoras | `/editora/` | Publishers with address, CNPJ, and phone. |
| Livros | `/livro/` | Books that reference an `Autor` and an `Editora`, plus ISBN, edition, synopsis, etc. |
| Bibliotecas | `/biblioteca/` | Library branches with name, address, and telephone. |
| Funcionários | `/funcionario/` | Employees tied to a `Biblioteca`. |
| Usuários | `/usuario/` | Patrons with counters for loans, delays, and limits. |
| Exemplares | `/exemplar/` | Physical copies of books, including barcode, acquisition date, condition, location, availability, and optional cover image. |
| Empréstimos | `/emprestimo/` | Loans that bind `Usuario`, `Funcionario`, `Exemplar`, return dates, status, and renewed copies. |

Each resource follows the standard REST pattern (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`) thanks to `DefaultRouter` + `ModelViewSet`. IDs are auto-generated primary keys.

### Example workflow
1. Create an author:
   ```bash
   curl -X POST http://127.0.0.1:8000/autor/ \
     -H "Content-Type: application/json" \
     -d '{"nome": "Clarice Lispector", "nacionalidade": "BR", "data_nascimento": "1920-12-10", "sexo": "F"}'
   ```
2. Create a publisher:
   ```bash
   curl -X POST http://127.0.0.1:8000/editora/ -H "Content-Type: application/json" -d '{"nome": "Editora Record", "cnpj": "64.742.123/0001-21", "endereco": "Av. Paulista, 1234", "telefone": "(11) 4000-0000"}'
   ```
3. Register a book (replace `autor` and `editora` IDs with actual values returned above):
   ```bash
   curl -X POST http://127.0.0.1:8000/livro/ -H "Content-Type: application/json" -d '{"isbn": "9788525447077", "title": "Laços de Família", "ano_publicacao": 1960, "edicao": "1ª", "sinopse": "Coletânea de contos", "autor": 1, "editora": 1}'
   ```
4. Create a library branch and a physical copy:
   ```bash
   curl -X POST http://127.0.0.1:8000/biblioteca/ -H "Content-Type: application/json" -d '{"nome": "Biblioteca Central", "endereco": "Rua das Flores, 100", "telefone": "(11) 3003-3003"}'
   curl -X POST http://127.0.0.1:8000/exemplar/ -H "Content-Type: application/json" -d '{"codigo_de_barras": "EX123456", "data_aquisicao": "2025-01-10", "estado_de_convervacao": "ótimo", "preco_de_compra": "120.50", "localizacao": "Prateleira 4", "biblioteca": 1, "livro": 1}'
   ```
5. Open a loan (this requires existing `usuario` and `funcionario` records):
   ```bash
   curl -X POST http://127.0.0.1:8000/emprestimo/ -H "Content-Type: application/json" -d '{"data_emprestimo": "2026-03-01", "data_devolucao_prevista": "2026-03-15", "data_devolucao": "2026-03-15", "status": "Em dia", "usuario": 1, "exemplar": 1, "funcionario": 1}'
   ```
6. Query loans or users with `GET http://127.0.0.1:8000/emprestimo/` or `GET http://127.0.0.1:8000/usuario/`.

## Architecture
- `bibliotecaapp/` is the Django project; `bibliotecaapp/settings.py` adds `apps/` to `sys.path`, so each domain app can be imported directly.
- Each app (`autor`, `editora`, `livro`, `biblioteca`, `funcionario`, `usuario`, `exemplar`, `emprestimo`) defines a Django model, a `ModelSerializer`, and a `ModelViewSet` registered via a `DefaultRouter` at a subpath (`/autor/`, `/livro/`, etc.).
- Models are interlinked: `Livro` points to `Autor` and `Editora`; `Exemplar` points to `Biblioteca` and `Livro`; `Emprestimo` ties `Usuario`, `Exemplar`, and `Funcionario` together and exposes a `ManyToManyField` for `exemplares_renovados`.
- Serializers use `fields = '__all__'`, so every column is read/writable.
- Middleware is the stock Django stack; no custom auth or permission classes are registered, so all endpoints are currently unauthenticated.
- Locale/timezone are set to Portuguese (Brazil) and `America/Sao_Paulo`, respectively.

## Testing
Run the Django test suite:
```
python manage.py test
```
All apps include the scaffolded `TestCase` import but no assertions yet, so tests currently pass trivially. Extend each `tests.py` when you need to verify business logic.

## Limitations
- The database backend is hardcoded to Oracle; switch `ENGINE`/env vars if you need PostgreSQL, SQLite, etc.
- No authentication, permissions, or throttling are configured—every endpoint is open by default.
- There is no pagination or filter backend in use yet even though `django-filter` is imported in `livro/views.py`.
- Several models (e.g., `Exemplar.__str__`) have placeholders or bugs such as subtracting strings, so rendering those objects in the admin may raise a `TypeError` until `__str__` is fixed.
- `Emprestimo` expects `data_devolucao` on every POST/PATCH call; the project does not auto-calculate due dates or renewals beyond the bare fields.
- Image uploads through `Exemplar.foto_capa` need a configured `MEDIA_ROOT`/`MEDIA_URL` and storage backend.
- Admin modules are empty, so register each model manually if you want admin management.
