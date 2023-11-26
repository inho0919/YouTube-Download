# [Vorbereitende Aufgabe]
# ================================
# * Ausfuehrungsumgebung : Windows 10 und Python 3.10.11
# * pip : pip install pytube
# * pip3 : pip3 install pytube
# ================================
# 
# Ver 1.0.0 : 12. Oktober 2023 von Kapship (Erstellt am Anfang)
# Ver 1.0.1 : 29. Oktober 2023 von Kapship (Wiedergabelistenfunktion hinzufuegen)
# Ver 1.0.2 : 26. November 2023 von Kapship (Zum ersten Mal auf GitHub hochladen)

# Pytube-Bibliothek importieren
from pytube import YouTube as YouTubeObj, Playlist as PlaylistObj

# YouTube-Klasse deklarieren
class YouTube:
    # ========================================================================================
    # Funktion zum Herunterladen einzelner Musikstuecke
    # Parameter: Download-URL und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def singleMusic(url, path):
        try:
            # Ausgabe: Daten im Dictionary-Format
            music = dict()

            # Pytube.YouTube Objekt definieren
            youtubeObject = YouTubeObj(url)

            # YouTube Stream Objekt definieren
            streamObject = youtubeObject.streams.filter(only_audio=True).first()
            streamObject.download(path)

            # Metadaten und Informationen herunterladen
            music['title'] = youtubeObject.title # Titel
            music['length'] = youtubeObject.length # Mediendauer
            music['rating'] = youtubeObject.rating # Bewertung
            music['thumbnailUrl'] = youtubeObject.thumbnail_url # Miniaturbild URL
            music['views'] = youtubeObject.views # Aufrufe
            music['description'] = youtubeObject.description # Beschreibung

            # Gib die Variable zurueck
            return music
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"
    

    
    # ========================================================================================
    # Einzelnes Video-Download-Funktion
    # Parameter: Download-URL und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def singleVideo(url, path):
        try:
            # Ausgabe: Daten im Dictionary-Format
            video = dict()

            # Pytube.YouTube Objekt definieren
            youtubeObject = YouTubeObj(url)

            # Definiere das YouTube-Stream-Objekt
            # Video benoetigt get_highest_resolution()
            streamObject = youtubeObject.streams.filter(mime_type="video/mp4", res="1080p", progressive=True)
            streamObject = youtubeObject.streams.get_highest_resolution()
            streamObject.download(path)

            # Metadaten und Informationen herunterladen
            video['title'] = youtubeObject.title # Titel
            video['length'] = youtubeObject.length # Mediendauer
            video['rating'] = youtubeObject.rating # Bewertung
            video['thumbnailUrl'] = youtubeObject.thumbnail_url # Miniaturbild URL 
            video['views'] = youtubeObject.views # Aufrufe
            video['description'] = youtubeObject.description # Beschreibung

            # Gib die Variable zurueck
            return video
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"



    # ========================================================================================
    # Mehrere Musikdownloads-Funktion
    # Parameter: Download-URL-Liste und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def multiMusic(urlList, path):
        try:
            # Ausgabe: Daten im Dictionary-Format
            musicData = list()

            # For-Schleife fuer die Laenge der URL-Liste ausfuehren
            for i in range(0, len(urlList)):
                fail = dict()

                # Funktion singleMusic ausfuehren
                data = YouTube.singleMusic(urlList[i], path)
                
                # Wenn der Datentyp eine Liste ist, 
                # fuege die von a erhaltenen Daten der 'musicData'-Variablen hinzu
                # Andernfalls die Variable 'fail' einsetzen
                # Schluessel-Wert-Paar ist URL und die Variable 'data' (Die Variable 'data' enthaelt "Failure")
                if type(data) == list:
                    musicData.append(data)
                else:
                    fail[urlList[i]] = data    
                    musicData.append(fail)

            # Gib die Variable zurueck
            return musicData
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"



    # ========================================================================================
    # Funktion zum Herunterladen mehrerer Videos
    # Parameter: Download-URL-Liste und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def multiVideo(urlList, path):
        try:
            # Ausgabe: Daten im List-Format
            videoData = list()
            
            # For-Schleife fuer die Laenge der URL-Liste ausfuehren
            for i in range(0, len(urlList)):
                # Voruebergehend die Variable 'fail' deklarieren
                fail = dict()

                # Funktion singleVideo ausfuehren
                data = YouTube.singleVideo(urlList[i], path)

                # Wenn der Datentyp eine Liste ist, 
                # fuege die von a erhaltenen Daten der 'videoData'-Variablen hinzu
                # Andernfalls die Variable 'fail' einsetzen
                # Schluessel-Wert-Paar ist URL und die Variable 'data' (Die Variable 'data' enthaelt "Failure")
                if type(data) == list:
                    videoData.append(data)
                else:
                    fail[urlList[i]] = data    
                    videoData.append(fail)

            # Gib die Variable zurueck
            return videoData
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"
    


    # ========================================================================================
    # Die Funktion ermoeglicht das gleichzeitige Herunterladen von Musikstuecken aus einer YouTube-Playlist.
    # Parameter: Download-URL und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def playlistMusic(url, path):
        try:
            # Ausgabe: Daten im List-Format
            musicData = list()

            # Pytube.PlaylistObj Objekt definieren
            playlist = PlaylistObj(url)

            # Variablendeklaration fuer URL-Index
            cnt = 0

            # Fuer die Anzahl der Videos in der Playlist wird 'video' als Schluessel festgelegt und eine for-Schleife durchgefuehrt
            for video in playlist.videos:
                # Variablen deklarieren fuer ein Dictionary, das in einer Liste gespeichert wird
                streamData = dict()

                # YouTube Stream Objekt definieren
                stream = video.streams.filter(only_audio=True).first()

                # Wenn 'stream' existiert
                if stream:
                    # Download beginnen
                    stream.download(path)

                    # Metadaten und Informationen herunterladen
                    streamData['title'] = video.title # Titel
                    streamData['length'] = video.length # Mediendauer
                    streamData['rating'] = video.rating # Bewertung
                    streamData['thumbnailUrl'] = video.thumbnail_url # Miniaturbild URL 
                    streamData['views'] = video.views # Aufrufe
                    streamData['description'] = video.description # Beschreibung
                else:
                    # Die URL als Schluessel nehmen und 'Failure' als Variable festlegen
                    streamData[playlist[cnt]] = "Failure"

                # List Indexnummer hinzufuegen
                cnt = cnt + 1
                
                # streamData in 'musicData' einfuegen
                musicData.append(streamData)
        
            # Gib die Variable zurueck
            return musicData
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"
        


    # ========================================================================================
    # Videos aus einer YouTube-Playlist koennen gleichzeitig heruntergeladen werden
    # Parameter: Download-URL und Speicherpfad
    # !!! Jedoch ist das Herunterladen von nicht oeffentlichen oder altersbeschraenkten Inhalten nicht moeglich
    def playlistVideo(url, path):
        try:
            # Ausgabe: Daten im List-Format
            videoData = list()

            # Pytube.PlaylistObj Objekt definieren
            playlist = PlaylistObj(url)

            # Variablendeklaration fuer URL-Index
            cnt = 0

            # Fuer die Anzahl der Videos in der Playlist wird 'video' als Schluessel festgelegt und eine for-Schleife durchgefuehrt
            for video in playlist.videos:
                # Variablen deklarieren fuer ein Dictionary, das in einer Liste gespeichert wird
                streamData = dict()

                # Definiere das YouTube-Stream-Objekt
                # Video benoetigt get_highest_resolution()
                stream = video.streams.filter(mime_type="video/mp4", res="1080p", progressive=True)
                stream = video.streams.get_highest_resolution()

                # Wenn 'stream' existiert
                if stream:
                    # Download beginnen
                    stream.download(path)

                    # Metadaten und Informationen herunterladen
                    streamData['title'] = video.title # Titel
                    streamData['length'] = video.length # Mediendauer
                    streamData['rating'] = video.rating # Bewertung
                    streamData['thumbnailUrl'] = video.thumbnail_url # Miniaturbild URL 
                    streamData['views'] = video.views # Aufrufe
                    streamData['description'] = video.description
                else:
                    # Die URL als Schluessel nehmen und 'Failure' als Variable festlegen
                    streamData[playlist[cnt]] = "Failure"

                # List Indexnummer hinzufuegen
                cnt = cnt + 1

                # streamData in 'videoData' einfuegen
                videoData.append(streamData)

            # Gib die Variable zurueck
            return videoData
        except:
            # Den Ausnahmefall zurueckgeben
            return "Failure"
        

        
    # ========================================================================================
    # * Bitte verwenden Sie es frei
    # * Aber bitte geben Sie nur die Quelle an
    # - Ende -
    # ========================================================================================