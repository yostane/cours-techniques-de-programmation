import random
from typing import List


class Media:
    days_of_rent = 0

    def __init__(self, name, extension, size) -> None:
        self.name = name
        self.extension = extension
        self.size = size
        self.current_rented_days = 0

    def play(self):
        print("playing media")

    def is_rented(self):
        return self.current_rented_days > 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (name={self.name}, en location?={self.is_rented}, a rendre dans {self.current_rented_days} jour(s)"

    def __repr__(self) -> str:
        return self.__str__()


class Video(Media):
    days_of_rent = 2

    def __init__(self, name, extension, size) -> None:
        super().__init__(name, extension, size)


class Audio(Media):
    days_of_rent = 4

    def __init__(self, name, extension, size) -> None:
        super().__init__(name, extension, size)


class Text(Media):
    days_of_rent = 4

    def __init__(self, name, extension, content: str) -> None:
        super().__init__(name, extension, len(content))
        self.content = content

    def get_word_count(self):
        return len(self.content.split(""))

    def get_consonant_count(self):
        count = 0
        for x in self.content:
            if x not in "aiueo":
                count += 1
        return count

    def get_consonant_count_2(self):
        return len([x not in "aiueo" for x in self.content])


class Mediatheque:
    def __init__(self, medias: List[Media]) -> None:
        self.medias = medias

    def show_sorted_medias_by_size(self, descending):
        sorted_list = sorted(self.medias, key=lambda m: m.size, reverse=descending)
        print(sorted_list)

    def show_sorted_medias_by_name(self, descending):
        sorted_list = sorted(self.medias, key=lambda m: m.name, reverse=descending)
        print(sorted_list)


class Person:
    def __init__(self):
        pass

    def perform_random_action(self, mediatheque: Mediatheque):
        action = random.randint(0, 2)
        if action == 0:
            videos = [
                isinstance(x, Video) and not x.is_rented() for x in mediatheque.medias
            ]
            r = random.randint(0, len(videos) - 1)
            videos[r].current_rented_days = Video.days_of_rent
            print("location de la vidéo", videos[r])
        if action == 1:
            audios_texts = [
                (isinstance(x, Audio) or isinstance(x, Text)) and not x.is_rented()
                for x in mediatheque.medias
            ]
            r = random.randint(0, len(audios_texts) - 1)
            audios_texts[r].current_rented_days = Audio.days_of_rent
            print("location du media", audios_texts[r])
        else:
            r = random.randint(0, len(mediatheque.medias) - 1)
            mediatheque.medias[r].play()


class Owner(Person):
    def __init__(self, mediatheque: Mediatheque):
        super().__init__()
        self.mediatheque = mediatheque

    def create_media(self, media):
        self.mediatheque.medias.append(media)

    def read_media(self, index):
        print("lecture du média", self.mediatheque.medias[index])
        return self.mediatheque.medias[index]

    def update_media(self, index, newValues):
        self.mediatheque.medias[index] = newValues

    def delete_media(self, index):
        self.mediatheque.medias.pop(index)


mediatheque = Mediatheque(
    [
        Audio("Grand bleu", "mp3", 3_000_000),
        Audio("Chouzetsu Dynamic", "mp3", 3_000_000),
        Video("naruto last movie", "mp3", 1_000_000_000),
        Text("20000 lieux sous les mers", "epub", "plouf"),
        Text("Les 12 travaux d'Astérix", "epub", "12"),
        Text("Classroom of the elite", "pdf", "Ayanokoji Kyotaka"),
    ]
)

mediatheque.show_sorted_medias_by_name()

owner = Owner(mediatheque)
