#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import telepot
from telepot.loop import MessageLoop
import numpy as np

class Location:
    def __init__(self, number, code):
        self.number = number
        self.code = code
        self.path = 'map/'+str(number)+'.png'

class Team:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.state = 0
        self.location = -1
        self.location_list = np.random.choice(20, 10, replace=False)
        self.tappa = -2
        self.name = ""
        self.point = 100


class Main:
    def init_location(self):
        locations = {}
        locations[0] = Location(0, "4084544200246416") #Bagno giu
        locations[1] = Location(1, "5631821205716525") #salone fondo sx
        locations[2] = Location(2, "7213014780738864") #salone fondo dx
        locations[3] = Location(3, "4020773788281556") #salone top sx
        locations[4] = Location(4, "5324145425647236") #salone top dx
        locations[5] = Location(5, "2452627472042763") #anti-deposito 
        locations[6] = Location(6, "2357566420885028") #scale giu
        locations[7] = Location(7, "8276226712136434") #ingresso passaggio chiesa
        locations[8] = Location(8, "4618400231731464") #bagno su
        locations[9] = Location(9, "4222730725152073") #berit
        locations[10] = Location(10, "6764776222615623") #gialla
        locations[11] = Location(11, "6500764610156356") #proiettore sedie rosse
        locations[12] = Location(12, "1005676030467185") #magazzino
        locations[13] = Location(13, "0834748665818083") #piccola di fianco magazzino
        locations[14] = Location(14, "5457357300166141") #piccola computer room
        locations[15] = Location(15, "4304277227242228") #arcobaleno
        locations[16] = Location(16, "1725384112384022") #sarfa's
        locations[17] = Location(17, "0354205414684874") #verde
        locations[18] = Location(18, "3604055634867741") #basket
        locations[19] = Location(19, "5524781162751786") #caritas/fontana
        return locations
    def __init__(self):
        self.team = {}
        self.TOKEN = 'your token goes here'
        self.bot = telepot.Bot(self.TOKEN)
        self.TOKEN_BB = 'your token_bb goes here'
        self.bb = telepot.Bot(self.TOKEN_BB)
        self.channel_id = 224534081
        self.locations = self.init_location()
        self.posizione = 1

    def quest(self, chat_id, tappa):
        if tappa == 0:
            self.bot.sendMessage(chat_id, "Se non ho la testa, sono piu' alto.\nCon la testa, invece, sono piu' basso.\nSapete cosa sono?")
        elif tappa == 1:
            self.bot.sendMessage(chat_id, "Risolvete questa: quanto vale il triangolo?")
            f = open('tappa1-eq.jpg', 'rb')
            self.bot.sendPhoto(chat_id, f)
        elif tappa == 2:
            self.bot.sendMessage(chat_id, "Risolvete questa enigma!")
            f = open('tappa2-ettari.png', 'rb')
            self.bot.sendPhoto(chat_id, f)
        elif tappa == 3:
            self.bot.sendMessage(chat_id, "Piu' e' caldo, piu' e' fresco. Cos'e'?")
        elif tappa == 4:
            self.bot.sendMessage(chat_id, "Chi la crea la vende. Chi la compra non la usa. Chi la sta usando non la vede. Cos'e'?")
        elif tappa == 5:
            self.bot.sendMessage(chat_id, "Risolvete questa enigma!\nSecondo il diagramma qui sotto, A=2, B=3, C=3 e D=4. Quindi, quanto vale E?")
            f = open('tappa5-E.gif', 'rb')
            self.bot.sendPhoto(chat_id, f)
        elif tappa == 6:
            self.bot.sendMessage(chat_id, "Sulla lavagna sono disegnate 5 forme.\nUna di queste e' sbagliata. Quale?")
            f = open('tappa6-shape.png', 'rb')
            self.bot.sendPhoto(chat_id, f)
        elif tappa == 7:
            self.bot.sendMessage(chat_id, "Due bambini, Sara e Francesco, giocano con le macchinine.\nSe Sara dà una delle sue macchinine a Francesco, quest'ultimo ne avrà il doppio di quelle di Sara.\nSe invece Francesco offre una macchinina a Sara, tutti e due avranno lo stesso numero di automobiline.\nQuante macchinine hanno all’inizio i due bambini?")
        elif tappa == 8:
            self.bot.sendMessage(chat_id, "Tutti lo possono aprire, ma nessuno sa chiuderlo. Cos'e'?")
        elif tappa == 9:
            self.bot.sendMessage(chat_id, "A un uomo sono state prescritte 10 pillole.\nPartendo oggi, deve prendere una pillola al giorno, ma siccome la concentrazione del medicinale e' diversa in ciascuna pillola, deve prenderle in un ordine specifico.\nDato che sono tutte uguali d'aspetto, l'uomo ha deciso di scrivere un numero su ciascuna di esse per ricordarsi in che ordine deve prenderle.\n\nQuante pillole deve numerare se vuole tenere traccia dell'ordine?")
            f = open('tappa9-pillole.gif', 'rb')
            self.bot.sendPhoto(chat_id, f)
    def answer(self, tappa, ans):
        if tappa == 0:
            if ans.lower() == 'il cuscino' or ans.lower() == 'cuscino' or ans.lower() == 'un cuscino':
                return True
            else:
                return False
        elif tappa == 1:
            if ans == '1':
                return True
            else:
                return False
        elif tappa == 2:
            if ans == '50' or ans.lower() == '50 euro' or ans == '50€' or ans == '50 €':
                return True
            else:
                return False
        elif tappa == 3:
            if ans.lower() == 'il pane' or ans.lower() == 'pane' or ans.lower() == 'la pagnotta' or ans.lower() == 'pagnotta' or ans == 'LO STRONZO':
                return True
            else:
                return False
        elif tappa == 4:
            if ans.lower() == 'la bara' or ans.lower() == 'bara' or ans.lower() == 'cassa' or ans.lower() == 'la cassa' or ans.lower() == 'la cassa da morto' or ans.lower() == 'cassa da morto':
                return True
            else:
                return False
        elif tappa == 5:
            if ans == '5' or ans.lower() == 'cinque':
                return True
            else:
                return False
        elif tappa == 6:
            if ans.lower() == 'd':
                return True
            else:
                return False
        elif tappa == 7:
            if ans.lower() == '5 e 7' or ans.lower() == '5 7' or ans.lower() == '7 e 5' or ans.lower() == '7 5':
                return True
            else:
                return False
        elif tappa == 8:
            if ans.lower() == 'l\'uovo' or ans.lower() == 'l\' uovo' or ans.lower() == 'un uovo' or ans.lower() == 'uovo' or ans.lower() == 'l uovo':
                return True
            else:
                return False
        elif tappa == 9:
            if ans == '8' or ans.lower() == 'otto' or ans.lower() == 'otto pillole':
                return True
            else:
                return False

    def execTappa(self, chat_id, command="", tappa=-5, text =""):
        if command == 'first001':
            self.team[chat_id] = Team(chat_id)
            self.bot.sendMessage(chat_id, "Ciao! Scrivete il nome della vostra squadra")
            self.team[chat_id].tappa = -10
        elif tappa == -10:
            self.team[chat_id].name = text
            self.bot.sendMessage(chat_id, "Bene, "+text+"! Ora inviatemi un selfie di squadra! :D")
            self.team[chat_id].tappa = -9
        elif tappa == -9:
            self.bot.sendMessage(chat_id, "Per proseguire dovete inviare una foto di squadra!")
        elif tappa == -1:
            self.team[chat_id].name = text
            self.bot.sendMessage(chat_id, "Bene, "+text+"! Possiamo cominciare!")
            self.team[chat_id].tappa = 0
            self.bot.sendMessage(chat_id, "La vostra prima tappa e' questa!")
            f = open(self.locations[self.team[chat_id].location_list[self.team[chat_id].tappa]].path, 'rb')
            self.bot.sendPhoto(chat_id, f)

        elif self.team[chat_id].tappa>=0 and self.team[chat_id].tappa<=9 and self.team[chat_id].state == 0:
            print("here1")
            print(command)
            print(self.team[chat_id].state == 0)
            print(self.locations[self.team[chat_id].location_list[self.team[chat_id].tappa]].code)
            if command == self.locations[self.team[chat_id].location_list[self.team[chat_id].tappa]].code:
                print("here2")
                self.bot.sendMessage(chat_id, "Ecco la prova per la tappa!")
                self.quest(chat_id, self.team[chat_id].tappa)
                self.team[chat_id].state = 1
            else:
                self.bot.sendMessage(chat_id, "Questa non e' la tappa che state cercando")
        elif tappa>=0 and self.team[chat_id].tappa<=9 and self.team[chat_id].state == 1:
            if self.answer(tappa, text):
                self.bot.sendMessage(chat_id, "Corretto! Potete proseguire :)")
                self.team[chat_id].tappa += 1
                self.team[chat_id].state = 0
                self.bb.sendMessage(self.channel_id, self.team[chat_id].name + " ha superato la tappa "+ str(tappa) + "!")
                if self.team[chat_id].tappa!=10:
                    self.bot.sendMessage(chat_id, "La vostra prossima tappa e' " + str(self.team[chat_id].location_list[self.team[chat_id].tappa]))
                    f = open(self.locations[self.team[chat_id].location_list[self.team[chat_id].tappa]].path, 'rb')
                    self.bot.sendPhoto(chat_id, f)
            else:
                self.bot.sendMessage(chat_id, "Risposta Errata, perdete punti...")
                self.team[chat_id].point -= 1
                self.bb.sendMessage(self.channel_id, self.team[chat_id].name + " ha sbagliato alla tappa "+ str(tappa) + "!\nHa risposto: " + text)
                self.quest(chat_id, self.team[chat_id].tappa)
        elif tappa ==10:
            self.bot.sendMessage(chat_id, "Dovete inviare un video per proseguire!")
        elif self.team[chat_id].tappa == 11:
            print("command =:" +command)
            if command == '42':
                self.bot.sendMessage(chat_id, "Complimenti! Avete completato il gioco :D")
                self.team[chat_id].point += 50
                self.team[chat_id].tappa = 12
                self.bot.sendMessage(chat_id, "Avete totalizzato "+ str(self.team[chat_id].point) +" punti (esclusi quelli di foto e video) e avete finito il gioco per " + self.ranking())
                self.bb.sendMessage(self.channel_id, self.team[chat_id].name + "ha terminato con " + str(self.team[chat_id].point) +" punti (esclusi quelli di foto e video)")
            else:
                self.bot.sendMessage(chat_id, "Dovete ricomporre l'indizio finale per terminare!")

        else:
            print("here")

    def ranking(self):
        if self.posizione == 1:
            self.posizione +=1
            return 'primi!'
        elif self.posizione == 2:
            self.posizione +=1
            return 'secondi!'
        elif self.posizione == 3:
            self.posizione +=1
            return 'terzi!'
        elif self.posizione == 4:
            self.posizione +=1
            return 'quarti!'
        elif self.posizione == 5:
            self.posizione +=1
            return 'quinti!'
        elif self.posizione == 6:
            self.posizione +=1
            return 'sesti!'
        elif self.posizione == 7:
            self.posizione +=1
            return 'settimi!'
        elif self.posizione == 8:
            self.posizione +=1
            return 'ottavi!'
        elif self.posizione == 9:
            self.posizione +=1
            return 'noni!'
        elif self.posizione == 10:
            self.posizione +=1
            return 'decimi!'

    def leaderboard(self):
        s = []
        for key, value in self.team.items():
            s.append((value.name, value.point))
        s.sort(reverse=True, key=lambda tup: tup[1])
        leaderboard = ""
        i = 1
        for team in s:
            leaderboard += str(i)+". "+team[0]+ " " + str(team[1])+" punti\n"
            i +=1
        return leaderboard

    def handle2(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            rec = msg['text']
            if rec == 'classifica':
                self.bb.sendMessage(self.channel_id, self.leaderboard())

    def help(self, chat_id, tappa):
        if tappa<10 and self.team[chat_id].state == 0:
            self.bot.sendMessage(chat_id, "Prima dovete raggiungere la tappa!")
        elif tappa == 0:
            self.bot.sendMessage(chat_id, "Ci poggi la testa sopra...")
            self.team[chat_id].point -= 3
        elif tappa ==1:
            self.bot.sendMessage(chat_id, "Il cerchio vale 5. Il quadrato 2...")
            self.team[chat_id].point -= 5
        elif tappa ==2:
            self.bot.sendMessage(chat_id, "L'indovinello dice un sacco di cose inutili, concentrati solamente su Roland")
            self.team[chat_id].point -= 3
        elif tappa ==3:
            self.bot.sendMessage(chat_id, "Quello fresco e' piu' buono da mangiare")
            self.team[chat_id].point -= 5
        elif tappa ==4:
            self.bot.sendMessage(chat_id, "Chi la usa non vede perche' e' morto...")
            self.team[chat_id].point -= 7
        elif tappa ==5:
            self.bot.sendMessage(chat_id, "Considera le sezioni che confinano con le lettere")
            self.team[chat_id].point -= 10
        elif tappa ==6:
            self.bot.sendMessage(chat_id, "La figura A e' composta da tre 3...")
            self.team[chat_id].point -= 7
        elif tappa ==7:
            self.bot.sendMessage(chat_id, "Le macchinine di Francesco sono 7.")
            self.team[chat_id].point -= 10
        elif tappa==8:
            self.bot.sendMessage(chat_id, "Si mangia. Una volta che lo rompi non si rimette piu' insieme...")
            self.team[chat_id].point -= 7
        elif tappa==9:
            self.bot.sendMessage(chat_id, "Il primo giorno prende la pillola senza segnarla. Gli restano 9 pillole, quante deve segnarne di queste?")
            self.team[chat_id].point -= 7
        else:
            self.bot.sendMessage(chat_id, "Nessun aiuto qui")

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        if content_type == 'text':
            rec = msg['text']
            if rec[0:6] == '/start':
                print(msg['text'][7:])
                self.execTappa(chat_id, command=msg['text'][7:])
            elif rec[0:5] == '/help':
                self.help(chat_id, self.team[chat_id].tappa)
            else:
                self.execTappa(chat_id, tappa=self.team[chat_id].tappa, text=rec)
                if self.team[chat_id].tappa == 10 and self.team[chat_id].state ==0:
                    self.bot.sendMessage(chat_id, "Complimenti! Ci siete quasi.\nPer ottenere l'ultimo indizio, inviate un video nel quale la squadra canta una canzone imbarazzante per almeno 30 secondi.\nPiu' e' imbarazzante e piu' punti farete!")
                    self.team[chat_id].state = 1
        elif content_type == 'photo':
            if self.team[chat_id].tappa == -9:
                self.bot.download_file(msg['photo'][-1]['file_id'], './'+str(chat_id)+'_'+self.team[chat_id].name+'.png')
                self.bot.sendMessage(chat_id, "Bene, "+self.team[chat_id].name+"! Possiamo cominciare!")
                self.team[chat_id].tappa = 0
                self.bb.sendMessage(self.channel_id, self.team[chat_id].name + " is in the game!")
                f = open(str(chat_id)+'_'+self.team[chat_id].name+'.png', 'rb')
                self.bb.sendPhoto(self.channel_id, f)
                self.bot.sendMessage(chat_id, "La vostra prima tappa e' questa!")
                f = open(self.locations[self.team[chat_id].location_list[self.team[chat_id].tappa]].path, 'rb')
                self.bot.sendPhoto(chat_id, f)
        elif content_type == 'video':
            if self.team[chat_id].tappa == 10:
                if msg['video']['duration']>=2:
                    file_id = msg['video']['file_id'] 
                    self.bot.download_file(file_id, './'+str(chat_id)+'_'+self.team[chat_id].name+'.mp4')
                    self.bot.sendMessage(chat_id, "Ottimo! Ecco l'indizio per l'ultima tappa!")
                    self.team[chat_id].point += 50
                    f = open('final_up.png', 'rb')
                    self.bot.sendPhoto(chat_id, f)
                    self.bot.sendMessage(chat_id, "Ops! Ne manca meta', provate a chiedere ai vostri edu!")
                    self.bb.sendMessage(self.channel_id, self.team[chat_id].name + " e' alla prova finale!")
                    f = open(str(chat_id)+'_'+self.team[chat_id].name+'.mp4', 'rb')
                    self.bb.sendVideo(self.channel_id, f)
                    self.team[chat_id].tappa = 11
                else:
                    self.bot.sendMessage(chat_id, "Dovete inviare un video di almeno 30 secondi per proseguire!")


    def run(self):
        MessageLoop(self.bot, self.handle).run_as_thread()
        MessageLoop(self.bb, self.handle2).run_as_thread()
        print ('Listening ...')
        # Keep the program running.
        while 1:
            time.sleep(10)

a = Main()
a.run()









