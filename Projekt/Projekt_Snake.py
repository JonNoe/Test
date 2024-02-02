import pygame, sys, random, time
from pygame.math import Vector2

class Schlange:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #Kreiert Schlangenkörper
        self.Richtung = Vector2(0,0)
        self.Verlängerung = False
        
        self.Kopf_links = pygame.image.load('Körper_Schlange\Kopf_links.png').convert_alpha()        #kreiert die Kopfanimation
        self.Kopf_rechts = pygame.image.load('Körper_Schlange\Kopf_rechts.png').convert_alpha()
        self.Kopf_oben = pygame.image.load('Körper_Schlange\Kopf_unten.png').convert_alpha()
        self.Kopf_unten = pygame.image.load('Körper_Schlange\Kopf_oben.png').convert_alpha()

        self.Körper_LO = pygame.image.load('Körper_Schlange\LO.png').convert_alpha()                 # kreiert die Körperanimation
        self.Körper_RO = pygame.image.load('Körper_Schlange\RO.png').convert_alpha()
        self.Körper_LU = pygame.image.load('Körper_Schlange\LU.png').convert_alpha()
        self.Körper_RU = pygame.image.load('Körper_Schlange\RU.png').convert_alpha()

        self.Schwanz_rechts = pygame.image.load('Körper_Schlange\Schwanz_links.png').convert_alpha()  # kreiert die Schwanzanimation
        self.Schwanz_links = pygame.image.load('Körper_Schlange\Schwanz_rechts.png').convert_alpha()
        self.Schwanz_unten = pygame.image.load('Körper_Schlange\Schwanz_unten.png').convert_alpha()
        self.Schwanz_oben = pygame.image.load('Körper_Schlange\Schwanz_oben.png').convert_alpha()

        self.Körper_links = pygame.image.load('Körper_Schlange\Korper_links.png').convert_alpha()    # kreiert die Körperanimation
        self.Körper_rechts = pygame.image.load('Körper_Schlange\\Korper_rechts.png').convert_alpha()
        self.Körper_unten = pygame.image.load('Körper_Schlange\Korper_unten.png').convert_alpha()
        self.Körper_oben = pygame.image.load('Körper_Schlange\Korper_oben.png').convert_alpha()

        self.oneup = pygame.mixer.Sound('Sounds\Sound_crunch.wav')

 
    def Schlange_bewegen(self):
        if self.Verlängerung == True:
            Körper_copy = self.body[:] #Kopiert alle Körperteile
            Körper_copy.insert(0,Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            self.Verlängerung = False
            
        else:
            Körper_copy = self.body[:-1] #Kopiert alle außer den letzten Wert
            Körper_copy.insert(0,Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            

    def Schlange_malen(self):
        self.update_Kopf_Grafiken()
        self.update_Schwanz_Grafiken()

        for index, Körperteil in enumerate(self.body):
            x_pos = int(Körperteil.x) * Zellengroesse #Positionierung x-Achse Schlange
            y_pos = int(Körperteil.y) * Zellengroesse #Positionierung y-Achse Schlange
            Körperteil_rect = pygame.Rect(x_pos, y_pos, Zellengroesse, Zellengroesse)

            if index == 0:
                screen.blit(self.Kopf,Körperteil_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.Schwanz,Körperteil_rect)
            else:
                vorgänger = self.body[index + 1] - Körperteil
                folgender = self.body[index - 1] - Körperteil
                if vorgänger.x == folgender.x:
                    screen.blit(self.Körper_oben,Körperteil_rect) #macht bei hortizontal nur Körper unten
                elif vorgänger.y == folgender.y:
                    screen.blit(self.Körper_rechts,Körperteil_rect) #macht bei vertikal nur Körper unten
                else: #Ecken, wie hängen benachbarte Körperteile von dem Aktuellen ab
                    if vorgänger.x == -1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == -1:
                        screen.blit(self.Körper_RU, Körperteil_rect)
                    elif vorgänger.x == -1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == -1:
                        screen.blit(self.Körper_RO, Körperteil_rect)
                    elif vorgänger.x == 1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == 1:
                        screen.blit(self.Körper_LO, Körperteil_rect)
                    elif vorgänger.x == 1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == 1:
                        screen.blit(self.Körper_LU, Körperteil_rect)

        
    def update_Kopf_Grafiken(self):
        Kopf_abhängigkeiten = self.body[1] -self.body[0] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Kopf_abhängigkeiten == Vector2(1,0):
            self.Kopf = self.Kopf_links
        elif Kopf_abhängigkeiten == Vector2(-1,0):
            self.Kopf = self.Kopf_rechts
        elif Kopf_abhängigkeiten == Vector2(0,-1):
            self.Kopf = self.Kopf_oben
        elif Kopf_abhängigkeiten == Vector2(0,1):
            self.Kopf = self.Kopf_unten
    
    def update_Schwanz_Grafiken(self):
        Schwanz_abhängigkeiten = self.body[-2] -self.body[-1] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Schwanz_abhängigkeiten == Vector2(1,0):
            self.Schwanz = self.Schwanz_links
        elif Schwanz_abhängigkeiten == Vector2(-1,0):
            self.Schwanz = self.Schwanz_rechts
        elif Schwanz_abhängigkeiten == Vector2(0,-1):
            self.Schwanz = self.Schwanz_oben
        elif Schwanz_abhängigkeiten == Vector2(0,1):
            self.Schwanz = self.Schwanz_unten

    def Schlange_verlängern(self):
        self.Verlängerung = True
    
    def play(self):
        self.oneup.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] 
        self.Richtung = Vector2(0,0)

            
class Frucht: 
    def __init__(self):
        self.random_fruit()
    
    def Frucht_malen(self):
        frucht_rect = pygame.Rect(int(self.pos.x * Zellengroesse), int((self.pos.y) * Zellengroesse ), Zellengroesse, Zellengroesse) #!!! Rect wird großgeschrieben
        #pygame.draw.rect(screen,pygame.Color('red'),frucht_rect)
        screen.blit(komische_frucht,frucht_rect)

    def random_fruit(self):
        self.x = random.randint(0, Anzahl_Zellen - 1)
        self.y = random.randint(3, Anzahl_Zellen - 1 )
        self.pos = Vector2(self.x,self.y)
        print(self.pos)

class MAIN:
    def __init__(self):
        self.schlange = Schlange()
        self.frucht = Frucht ()


    def Update(self):
        self.schlange.Schlange_bewegen()
        self.Kollisionen()
        self.check_fail()
        
    
    def Malen(self):
        global alive
        self.Gras_Feld()
        self.Score()
        main_game.frucht.Frucht_malen()
        main_game.schlange.Schlange_malen()
        if self.check_fail() == True:
            self.death_screen()
        
    
    def Kollisionen(self):
        if self.frucht.pos == self.schlange.body[0]:
            self.frucht.random_fruit()
            self.schlange.Schlange_verlängern()
            self.schlange.play()
        
        for Körperteil in self.schlange.body[1:]: #Wenn Frucht Position in Körper der Schlange, dann erneut random -> falls die Frucht in der Schlange spawnt
            if Körperteil == self.frucht.pos:
                self.frucht.random_fruit()

    def check_fail(self):
        # Schlange trifft sich selbst oder rand, Spiel wird beendet
        if not 0 <= self.schlange.body[0].x < Anzahl_Zellen or not 3 <= self.schlange.body[0].y < Anzahl_Zellen:
            self.game_over()
            self.death_screen()
            return True

        
        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0]:
                self.game_over()
                self.death_screen()
                return True

    def game_over(self):
        #neustart = input('neustart ').lower()
        dead = True
        game_over_text = FONT.render(f'GAME OVER', True, (200,200,200))
        game_over_rect = game_over_text.get_rect()
        score_text = FONT.render(f'You achieved a score of {self.Score()}',True, (200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
                pygame.quit() #Fenster schließen
                sys.exit() #beendet allen Code
            if event.type == pygame.KEYDOWN: #Steuerung
                if event.key == pygame.K_u:
                    dead = False
                    self.schlange.reset()
            screen.fill((0,0,0))
            screen.blit(game_over_text, (Feldgröße/2 - (game_over_text.get_width()/2), Feldgröße/2 - game_over_text.get_height()/2))
            screen.blit(score_text, (Feldgröße/2 - (score_text.get_width()/2), (Feldgröße/2 + score_text.get_height() * 1.5)))
        
        
        
    def death_screen(self):
            meme_rect = pygame.Rect(0, 0, Feldgröße, Feldgröße)
            screen.blit(meme, meme_rect )
        

    def Gras_Feld(self):
    
        GRAS_FARBE = (167,255,61)
        for Zeile in range(Anzahl_Zellen):
            if Zeile % 2 == 0:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 == 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse, Zeile * Zellengroesse + Overlay_Zeile, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)
            else:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 != 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse, Zeile * Zellengroesse + Overlay_Zeile, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)

    def Score(self):
        global current_score
        current_score = str(len(self.schlange.body) - 3) #score startet nicht bei 3
        score_surface = SCHRIFTART.render(current_score, True, (56,74,12))
        score_x = int(Feldgröße - 60) #Wo Score Anzeige
        score_y = int(Feldgröße - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        frucht_rect = komische_frucht.get_rect(midright = (score_rect.left, score_rect.centery))
        hintergrund_rect = pygame.Rect(frucht_rect.left, frucht_rect.top, frucht_rect.width + score_rect.width, frucht_rect.height )

        pygame.draw.rect(screen, (255, 0, 255), hintergrund_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(komische_frucht, frucht_rect)
        return current_score
        


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
Zellengroesse = 40   
Anzahl_Zellen = 20
Overlay_Zeile = 120

Feldgröße = Zellengroesse * Anzahl_Zellen
Bildschrimhöhe = Feldgröße + Overlay_Zeile
Bildschrimbreite = Feldgröße

screen = pygame.display.set_mode((Feldgröße,Feldgröße)) #Legt fenstergröße fest Breite*Höhe
pygame.display.set_caption('Snake Fake')
Icon = pygame.image.load('Memes\icon snake.png')
pygame.display.set_icon(Icon)
clock = pygame.time.Clock()
FPS = 60
komische_frucht = pygame.image.load('Frucht\Pilz.png').convert_alpha() #convert: ändert Bild in besseres Format für python
meme = pygame.image.load('Memes\8dca0ed8f9a4ffbe171fb804c61b73e8.jpg').convert_alpha()
#SCHRIFTART = pygame.font.Font('Fonts\__MACOSX\._DESIB___.TTF', 25)
SCHRIFTART = pygame.font.Font(None, 25)
alive = True
FONT = pygame.font.SysFont('Arial', 60)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()
global schlange
while True: #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
            pygame.quit() #Fenster schließen
            sys.exit() #beendet allen Code
        if event.type == SCREEN_UPDATE:
            main_game.Update()
        
        if event.type == pygame.KEYDOWN: #Steuerung
            if event.key == pygame.K_UP: 
                if main_game.schlange.Richtung.y != 1: #Man kann nur nach oben gehen, wenn man nicht nach unten geht
                    main_game.schlange.Richtung = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.schlange.Richtung.y != -1:
                    main_game.schlange.Richtung = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.schlange.Richtung.x != 1:
                    main_game.schlange.Richtung = Vector2(-1, 0)
                
            if event.key == pygame.K_RIGHT:
                if main_game.schlange.Richtung.x != -1:
                    main_game.schlange.Richtung = Vector2(1, 0)

                
    screen.fill(pygame.Color((178,255,102)))
    main_game.Malen()
    pygame.display.update() #Updatet nach jedem while loop
    clock.tick(FPS) #updatet 30x pro sekunde
