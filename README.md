Спринт 13 YP

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
