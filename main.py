# Дополнительное практическое задание по модулю: "Классы и объекты."

import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # В добавление, можно сделать метод для проверки пароля
    def check_password(self, password):
        return self.password == self.hash_password(password)

    def __str__(self):
        return f'User (nickname={self.nickname}, age={self.age})'


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Пользователь {nickname} вошел в аккаунт.')
                return
        print('Неверный логин или пароль.')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и автоматически вошел в аккаунт.')

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта.')

    def add(self, *videos):
        for video in videos:
            if all(existing_video.title != video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f'Воспроизведение видео: {video.title}')
                while video.time_now < video.duration:
                    print(video.time_now + 1)
                    time.sleep(1)
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено.")

# Пример использования

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('Vitaliy_Karyakin', 'Fessk220F///";', 17)  # Регистрация
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация совершеннолетнего
ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение

# Проверка входа в другой аккаунт
ur.register('Kirill_Krivoi', 'F8098FM8fjm9jmi', 55)  # Попытка регистрации уже существующего пользователя
print(ur.current_user)  # Проверка текущего пользователя

# Пример использования

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация совершеннолетнего
ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Попытка регистрации уже существующего пользователя
print(ur.current_user)  # Проверка текущего пользователя

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2023 года!')  # Видео не найдено.




