# 2022-django4-clone-airbnb
CLONE AIRBNB MENGGUNAKAN DJANGO VERSI 4

Github repository: https://github.com/gurnitha/2022-django4-clone-airbnb


### 1. DJANGO PROJECT
---------------------

#### 1.1 Membuat proyek django dengan nama 'config'

        modified:   .gitignore
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


### 2. SETUP DATABASE
---------------------

#### 2.1 Setting up database menggunakan Postgres

        modified:   README.md
        modified:   config/settings.py


### 3. MEMBUAT ROOMS APP
------------------------

#### 3.1 Create django app dengan nama 'apps/rooms'

        modified:   README.md
        new file:   app/rooms/__init__.py
        new file:   app/rooms/admin.py
        new file:   app/rooms/apps.py
        new file:   app/rooms/migrations/__init__.py
        new file:   app/rooms/models.py
        new file:   app/rooms/tests.py
        new file:   app/rooms/views.py
        modified:   config/settings.py

#### 3.2 Membuat models: RoomType, Amenity, Facility, HouseRule, Room, Photo 

        modified:   README.md
        modified:   app/rooms/admin.py
        modified:   app/rooms/models.py


### 4. MEMBUAT USERS APP
------------------------

#### 4.1 Create django app dengan nama 'apps/users'

        modified:   README.md
        new file:   app/users/__init__.py
        new file:   app/users/admin.py
        new file:   app/users/apps.py
        new file:   app/users/migrations/__init__.py
        new file:   app/users/models.py
        new file:   app/users/tests.py
        new file:   app/users/views.py
        modified:   config/settings.py

#### 4.2 Membuat model: MyCustomUser dan jalankan migrasi

        modified:   README.md
        new file:   app/rooms/migrations/0001_initial.py
        new file:   app/rooms/migrations/0002_initial.py
        new file:   app/rooms/migrations/0003_alter_amenity_options_alter_facility_options_and_more.py
        modified:   app/rooms/models.py
        modified:   app/users/admin.py
        new file:   app/users/migrations/0001_initial.py
        modified:   app/users/models.py
        modified:   config/settings.py


### 5. MEMBUAT REVIEWS APP
--------------------------

#### 5.1 Create a new app 'app/reviews' dan  Review model

        modified:   README.md
        new file:   app/reviews/__init__.py
        new file:   app/reviews/admin.py
        new file:   app/reviews/apps.py
        new file:   app/reviews/migrations/0001_initial.py
        new file:   app/reviews/migrations/0002_alter_review_accuracy_alter_review_check_in_and_more.py
        new file:   app/reviews/migrations/__init__.py
        new file:   app/reviews/models.py
        new file:   app/reviews/tests.py
        new file:   app/reviews/views.py
        modified:   config/settings.py


### 6. MEMBUAT RESERVATIONS APP
-------------------------------

#### 6.1 Create a new app 'app/reservations' dan Reservation model

        modified:   README.md
        new file:   app/reservations/__init__.py
        new file:   app/reservations/admin.py
        new file:   app/reservations/apps.py
        new file:   app/reservations/migrations/0001_initial.py
        new file:   app/reservations/migrations/__init__.py
        new file:   app/reservations/models.py
        new file:   app/reservations/tests.py
        new file:   app/reservations/views.py
        modified:   config/settings.py


### 7. MEMBUAT LISTS APP
------------------------

#### 7.1 Create a new app 'app/lists' dan List model

        modified:   README.md
        new file:   app/lists/__init__.py
        new file:   app/lists/admin.py
        new file:   app/lists/apps.py
        new file:   app/lists/migrations/0001_initial.py
        new file:   app/lists/migrations/0002_remove_list_room_list_room.py
        new file:   app/lists/migrations/__init__.py
        new file:   app/lists/models.py
        new file:   app/lists/tests.py
        new file:   app/lists/views.py
        modified:   config/settings.py


### 8. MEMBUAT CONVERSATIONS APP
--------------------------------

#### 8.1 Create a new app 'app/conversations', Conversation model dan Message model

        new file:   app/conversations/__init__.py
        new file:   app/conversations/admin.py
        new file:   app/conversations/apps.py
        new file:   app/conversations/migrations/0001_initial.py
        new file:   app/conversations/migrations/__init__.py
        new file:   app/conversations/models.py
        new file:   app/conversations/tests.py
        new file:   app/conversations/views.py
        modified:   config/settings.py