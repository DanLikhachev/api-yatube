Спринт 13 YP - CRUD для Yatube

Бэкенд для практической работы 'Api Yatube': формирование эндпоинтов и базовые операции с БД.

Подготовка:
1) Клонируйте репозиторий
2) Установите зависимости (pip install -r requirements.txt)
3) Примените миграции (python yatube_api/manage.py migrate)
4) Запустите сервер (python yatube_api/manage.py runserver (на данный момент в режиме отладки))

Вьюсеты:
    'PostViewSet' - операции с постами (CRUD)
    'GroupViewSet' - просмотр групп(ы)
    'CommentViewSet' - операции с комментариями (CRUD)

Эндпоинты:
    Аутификация:
    'api/v1/api-token-auth/'

    Операции с постами:
    'api/v1/posts/'
    'api/v1/posts/{post_id}/'

    Просмотр групп(ы)
    'api/v1/groups/'

    Операции с комментариями:
    'api/v1/posts/{post_id}/comments/'
    'api/v1/posts/{post_id}/comments/{comment_id}/'

Библитотеки (requirements.txt):
    asgiref==3.8.1
    attrs==24.2.0
    certifi==2026.1.4
    cffi==2.0.0
    charset-normalizer==3.4.4
    colorama==0.4.6
    cryptography==46.0.3
    defusedxml==0.7.1
    Django==5.1.1
    djangorestframework==3.15.2
    djangorestframework_simplejwt==5.5.1
    djoser==2.3.3
    flake8==7.1.1
    idna==3.11
    iniconfig==2.0.0
    mccabe==0.7.0
    oauthlib==3.3.1
    packaging==24.2
    pillow==11.0.0
    pluggy==1.5.0
    py==1.11.0
    pycodestyle==2.12.1
    pycparser==2.23
    pyflakes==3.2.0
    PyJWT==2.10.1
    pyparsing==3.2.1
    pytest==8.3.3
    pytest-django==4.9.0
    python3-openid==3.2.0
    pytz==2024.2
    requests==2.32.5
    requests-oauthlib==2.0.0
    social-auth-app-django==5.7.0
    social-auth-core==4.8.3
    sqlparse==0.5.2
    toml==0.10.2
    tzdata==2025.3
    urllib3==2.6.3


