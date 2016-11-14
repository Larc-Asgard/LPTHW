class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
#upon constructing the class Song, it will store the variable as lyrics
    def sing_a_song(self):
        for line in self.lyrics:#for every line stored in variable lyrics
            print line

happy_bday = Song ([
"It's your birthday",
"We gon' party like it's yo birthday",
"We gon' sip Bacardi like it's your birthday"
])

rocks = Song (["Buddy you're a boy make a big noise",
"Playin' in the street gonna be a big man some day",
"You got mud on yo' face",
"You big disgrace",
"Kickin' your can all over the place"
])
#() is for the function, [] is here because of the string/lyrics
happy_bday.sing_a_song()
rocks.sing_a_song()
