import tkinter
import pygame
import pydub
import os

os.environ["PATH"] += os.pathsep + "/opt/homebrew/Cellar/ffmpeg/6.0_2/bin/"


pydub.AudioSegment.ffmpeg = "/opt/homebrew/Cellar/ffmpeg/6.0_2/bin/ffmpeg"
pydub.AudioSegment.ffprobe = "/opt/homebrew/Cellar/ffmpeg/6.0_2/bin/ffprobe"

# Starting the mixer
pygame.mixer.init()

# Creating playlists
playlist_1 = []
playlist_2 = []

# Loading songs into playlists
for filename in os.listdir("/Applications/MAMP/htdocs/work/Python/PlayerMusic/songs"):
    if filename.endswith(".mp3"):
        song = pydub.AudioSegment.from_file(f"/Applications/MAMP/htdocs/work/Python/PlayerMusic/songs/{filename}")
        if filename.startswith("playlist1"):
            playlist_1.append(song)
        elif filename.startswith("playlist2"):
            playlist_2.append(song)

# Adding your playlists
playlist_1.append(pydub.AudioSegment.from_file("/Applications/MAMP/htdocs/work/Python/PlayerMusic/songs//Applications/MAMP/htdocs/work/Python/PlayerMusic/Indila - Dernière Danse (Clip Officiel) (2).mp3"))
playlist_2.append(pydub.AudioSegment.from_file("/Applications/MAMP/htdocs/work/Python/PlayerMusic/songs/Zaho - Roi 2 cœur ft. Indila (Paroles) [مترجمة].mp3"))

try:
    song = pydub.AudioSegment.from_file("/Applications/MAMP/htdocs/work/Python/PlayerMusic/PlayerMusic/songs/Indila - Dernière Danse (Clip Officiel) (2).mp3")
    playlist_1.append(song)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Creating window
root = tkinter.Tk()
root.title("Player Music")

# Creating listboxes for playlists
listbox_playlist_1 = tkinter.Listbox(root)
for song in playlist_1:
    listbox_playlist_1.insert(tkinter.END, song.filename)
listbox_playlist_1.pack()

listbox_playlist_2 = tkinter.Listbox(root)
for song in playlist_2:
    listbox_playlist_2.insert(tkinter.END, song.filename)
listbox_playlist_2.pack()

# Buttons for playing songs
button_play_playlist_1 = tkinter.Button(root, text="Play Playlist 1", command=lambda: play_playlist(playlist_1))
button_play_playlist_1.pack()

button_play_playlist_2 = tkinter.Button(root, text="Play Playlist 2", command=lambda: play_playlist(playlist_2))
button_play_playlist_2.pack()

# Functions for playing playlists
def play_playlist(playlist):
    # Clearing current music
    pygame.mixer.music.stop()

    # Setting the volume
    pygame.mixer.music.set_volume(0.7)

# Lire la piste de lecture "piste1.wav"
import pygame

def mixer():
    # Crée le mixer
    mixer = pygame.mixer.init()

    return mixer
def lire_piste(nom_piste):
    # Ouvre la piste de lecture
    piste = pygame.mixer.Sound(nom_piste)

    # Joue la piste de lecture
    piste.play()

def playlist():
    # Liste des pistes de lecture
    piste = ["piste1.wav", "piste2.wav", "piste3.wav"]

    return piste


if __name__ == "__main__":
    # Lire la piste de lecture "piste1.wav"
    lire_piste("piste1.wav")

    # Playing the playlist
    for song in playlist:
        mixer.music.load(song.filename)
        mixer.music.play()

        # Infinite loop for handling playback
        while True:
            print("Press 'p' to pause, 'r' to resume, 'n' for next song, 'b' for previous song, or 'e' to exit")
            query = input(" ")

            if query == 'p':
                mixer.music.pause()
                break
            elif query == 'r':
                mixer.music.unpause()
                break
            elif query == 'n':
                if song != playlist[-1]:
                    song = playlist[playlist.index(song) + 1]
                    mixer.music.load(song.filename)
                    mixer.music.play()
            elif query == 'b':
                if song != playlist[0]:
                    song = playlist[playlist.index(song) - 1]
                    mixer.music.load(song.filename)
                    mixer.music.play()
            elif query == 'e':
                mixer.music.stop()
                break

# Main loop
root.mainloop()
