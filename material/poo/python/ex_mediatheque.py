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
        print("Ledcture de", self)

    def is_rented(self):
        return self.current_rented_days > 0

    def __str__(self) -> str:
        if self.is_rented():
            return f"{self.__class__.__name__} (name={self.name}, sera rendu dans {self.current_rented_days} jour(s)))"
        else:
            return f"{self.__class__.__name__} (name={self.name}, non loué)"

    def __repr__(self) -> str:
        return self.__str__()


class Video(Media):
    days_of_rent = 10

    def __init__(self, name, extension, size) -> None:
        super().__init__(name, extension, size)


class Audio(Media):
    days_of_rent = 5

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


class MediaLibrary:
    def __init__(self, medias: List[Media]) -> None:
        self.medias = medias

    def show_sorted_medias_by_size(self, descending=False):
        sorted_list = sorted(self.medias, key=lambda m: m.size, reverse=descending)
        print(f"tris par espace (décroissant {descending})", sorted_list)

    def show_sorted_medias_by_name(self, descending=False):
        sorted_list = sorted(self.medias, key=lambda m: m.name, reverse=descending)
        names = [x.name for x in sorted_list]
        print("noms triés (ordre décroissant {descending})", names)

    def __str__(self) -> str:
        return f"Contenu de la médiathèque: {self.medias}"

    def advance_rental(self):
        for media in self.medias:
            media.current_rented_days = max(media.current_rented_days - 1, 0)

    def get_all_consonant_count(self):
        counts = [x.get_consonant_count() for x in self.medias if isinstance(x, Text)]
        return sum(counts)


class Person:
    def __init__(self):
        pass

    def perform_random_action(self, mediatheque: MediaLibrary):
        action = random.randint(0, 2)
        if action == 0:
            videos = [
                x
                for x in mediatheque.medias
                if isinstance(x, Video) and not x.is_rented()
            ]
            if len(videos) == 0:
                print("Aucune vidéo disponible à la location")
                return
            r = random.randint(0, len(videos) - 1)
            videos[r].current_rented_days = Video.days_of_rent
            print("location de la vidéo", videos[r])
        if action == 1:
            audios_texts = [
                x
                for x in mediatheque.medias
                if (isinstance(x, Audio) or isinstance(x, Text)) and not x.is_rented()
            ]
            if len(audios_texts) == 0:
                print("Aucun media disponible à la location")
                return
            r = random.randint(0, len(audios_texts) - 1)
            audios_texts[r].current_rented_days = Audio.days_of_rent
            print("location du media", audios_texts[r])
        else:
            available_medias = [x for x in mediatheque.medias if not x.is_rented()]
            if len(available_medias) == 0:
                print("Auncun média disponible à la lecture")
                return
            r = random.randint(0, len(available_medias) - 1)
            available_medias[r].play()


class Owner(Person):
    def __init__(self, mediatheque: MediaLibrary):
        super().__init__()
        self.media_library = mediatheque

    def create_media(self, media):
        self.media_library.medias.append(media)

    def read_media(self, index):
        print("lecture du média", self.media_library.medias[index])
        return self.media_library.medias[index]

    def update_media(self, index, newValues):
        self.media_library.medias[index] = newValues

    def delete_media(self, index):
        self.media_library.medias.pop(index)


livre = Text("20000 lieux sous les mers", "epub", "plouf dans l'eau")

media_library = MediaLibrary(
    [
        Audio("Grand bleu", "mp3", 3_000_000),
        Audio("Chouzetsu Dynamic", "mp3", 3_000_000),
        Video("naruto last movie", "mp3", 1_000_000_000),
        livre,
        Text("Les 12 travaux d'Astérix", "epub", "12"),
        Text("Classroom of the elite", "pdf", "Ayanokoji Kyotaka"),
    ]
)

media_library.show_sorted_medias_by_name()
media_library.show_sorted_medias_by_size(True)

print("nombre de consonnes de", livre, "est", livre.get_consonant_count_2())
print(
    "nombre de consonnes dans la médiathèqye", media_library.get_all_consonant_count()
)

owner = Owner(media_library)
owner.create_media(Video("Spy x familiy code white", "mov", 2_000_000_000))
print(owner.media_library)
owner.delete_media(0)
print(owner.media_library)
owner.read_media(2)


for day in range(30):
    media_library.advance_rental()
    print("nouvelle journée")
    person = Person()
    person.perform_random_action(media_library)

print(media_library)
