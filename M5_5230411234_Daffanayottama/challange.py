class Music:
    def __init__(self, Judul, artist, genre):
        self.Judul = Judul
        self.artist = artist
        self.genre = genre

    def display(self):
        print(f"Judul: {self.Judul}, Penyanyi: {self.artist}, Genre: {self.genre}")


class RockMusic(Music):
    def __init__(self, Judul, artist):
        super().__init__(Judul, artist, "Rock")


class PopMusic(Music):
    def __init__(self, Judul, artist):
        super().__init__(Judul, artist, "Pop")


class JazzMusic(Music):
    def __init__(self, Judul, artist):
        super().__init__(Judul, artist, "Jazz")


class MusicCollection:
    def __init__(self):
        self.collection = []

    def add_music(self, music):
        self.collection.append(music)

    def delete_music(self, Judul):
        self.collection = [music for music in self.collection if music.Judul != Judul]
        print(f"Musik '{Judul}' berhasil dihapus!")

    def display_all(self):
        if len(self.collection) == 0:
            print("Koleksi musik kosong.")
        else:
            sorted_collection = sorted(self.collection, key=lambda music: music.Judul)
            for music in sorted_collection:
                music.display()

    def display_by_genre(self, genre):
        filtered_songs = [music for music in self.collection if music.genre == genre]
        if filtered_songs:
            for song in filtered_songs:
                song.display()
        else:
            print(f"Tidak ada musik di genre {genre}.")

    def search_by_artist(self, artist):
        found_songs = [music for music in self.collection if music.artist.lower() == artist.lower()]
        if found_songs:
            for song in found_songs:
                song.display()
        else:
            print(f"Tidak ada musik yang ditemukan untuk artis: {artist}")


music_collection = MusicCollection()
music_collection.add_music(RockMusic("Back in Black", "AC/DC"))
music_collection.add_music(RockMusic("Bohemian Rhapsody", "Queen"))
music_collection.add_music(RockMusic("Satisfaction", "The Rolling Stones"))
music_collection.add_music(RockMusic("Light My Fire", "The Doors"))
music_collection.add_music(RockMusic("Lullaby", "The Beatles"))
music_collection.add_music(PopMusic("Tentang Dirimu", "Raisa"))
music_collection.add_music(PopMusic("Ingkar", "Tulus"))
music_collection.add_music(PopMusic("Tenang", "Yura Yunita"))
music_collection.add_music(PopMusic("Mesin Waktu", "Budi Doremi"))
music_collection.add_music(PopMusic("Orang Yang Sama", "Virgoun"))
music_collection.add_music(JazzMusic("Nurlela", "Bing Slamet"))
music_collection.add_music(JazzMusic("Di Wajah Mu Kulihat Bulan", "Sam Saimun"))
music_collection.add_music(JazzMusic("Aku Ingin", "Indra Lesmana"))
music_collection.add_music(JazzMusic("Januari", "Glenn Fredly"))
music_collection.add_music(JazzMusic("Remember", "Mocca"))

while True:
    print("=== Playlist Music === ")
    print("1. Musik Rock")
    print("2. Musik Pop")
    print("3. Musik Jazz")
    print("4. Display All")
    print("5. Search Music")
    print("0. Exit")

    menu = input("Pilih menu yang anda inginkan: ")

    if menu == "1":
        print("=== MUSIC ROCK ===")
        print("1. Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

        menu = input("Pilih menu Rock: ")

        if menu == "1":
            print("=== Display Song ===")
            music_collection.display_by_genre("Rock") 

        elif menu == "2":
            Judul = input("Judul: ")
            artist = input("Penyanyi: ")
            music_collection.add_music(RockMusic(Judul, artist))

        elif menu == "3":
            Judul = input("Judul: ")
            music_collection.delete_music(Judul)

        elif menu == "0":
            continue

    elif menu == "2":
        print("=== MUSIC POP ===")
        print("1. Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

        menu = input("Pilih menu Pop: ")

        if menu == "1":
            music_collection.display_by_genre("Pop") 

        elif menu == "2":
            Judul = input("Judul: ")
            artist = input("Penyanyi: ")
            music_collection.add_music(PopMusic(Judul, artist))

        elif menu == "3":
            Judul = input("Judul: ")
            music_collection.delete_music(Judul)

        elif menu == "0":
            continue

    elif menu == "3":
        print("=== MUSIC JAZZ ===")
        print("1. Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

        menu = input("Pilih menu Jazz: ")

        if menu == "1":
            music_collection.display_by_genre("Jazz") 

        elif menu == "2":
            Judul = input("Judul: ")
            artist = input("Penyanyi: ")
            music_collection.add_music(JazzMusic(Judul, artist))

        elif menu == "3":
            Judul = input("Judul: ")
            music_collection.delete_music(Judul)

        elif menu == "0":
            continue

    elif menu == "4":
        print("=== Display All ===")
        music_collection.display_all()  

    elif menu == "5":
        artist = input("Masukkan penyanyi: ")
        music_collection.search_by_artist(artist)  

    elif menu == "0":
        break

    else:
        print("Menu tidak tersedia")
