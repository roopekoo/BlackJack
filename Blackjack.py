# Simple Blackjack:

import random
from tkinter import *


def calculate_points(lista):
    """
    Laskee käyttäjän korttilistasta arvot pisteiksi.
    :param lista:
    :return: ans: palauttaa lasketun pistesumman
    """
    ans = 0
    for i in range(len(lista)):
        # Halkaiseen listan alkion YY.gif muotoon [YY, gif]
        if "." in lista[i]:
            lista[i] = lista[i].split(".")
        if lista[i][0][1] == "1":
            ans += 10
        elif lista[i][0][1] == "J":
            ans += 10
        elif lista[i][0][1] == "Q":
            ans += 10
        elif lista[i][0][1] == "K":
            ans += 10
        elif lista[i][0][1] == "9":
            ans += 9
        elif lista[i][0][1] == "8":
            ans += 8
        elif lista[i][0][1] == "7":
            ans += 7
        elif lista[i][0][1] == "6":
            ans += 6
        elif lista[i][0][1] == "5":
            ans += 5
        elif lista[i][0][1] == "4":
            ans += 4
        elif lista[i][0][1] == "3":
            ans += 3
        elif lista[i][0][1] == "2":
            ans += 2
        elif lista[i][0][1] == "A":
            if ans + 11 <= 21:
                ans += 11
            else:
                ans += 1
    return ans


class Blackjack:
    def __init__(self):
        """
        Asioiden sijottelua ja tyhjien listojen luomista myöhempään käyttöön.
        """
        self.__dealer_card_labels = []
        self.__dealer_points = []
        self.__player_card_labels = []
        self.__player_points = []
        self.__kuvalista = []
        self.__KORTIT_ALKUP = []
        self.__window = Tk()
        self.__window.title("BlackJack")

        # Infobox kertoo ohjeita tai tilanteen, kuka voitti
        self.__infobox = Label(self.__window)
        self.__infobox.grid(row=0, column=0, columnspan=4)

        self.__newgame = Button(self.__window, text="New game",
                                command=self.reset)
        self.__newgame.grid(row=1, column=0, sticky="ew")

        self.__hit = Button(self.__window, text="Hit", command=self.hit)
        self.__hit.grid(row=2, column=0, sticky="ew")

        self.__stand = Button(self.__window, text="Stand", command=self.stand)
        self.__stand.grid(row=3, column=0, sticky="ew")

        self.__exit = Button(self.__window, text="Exit",
                             command=self.__window.destroy)
        self.__exit.grid(row=4, column=0, sticky="ew")

        self.__dealer_info = Label(self.__window,
                                   text="Dealer's points and cards:")
        self.__dealer_info.grid(row=1, column=1)

        self.__dealer_points_label = Label(self.__window)
        self.__dealer_points_label.grid(row=2, column=1)

        self.__player_info = Label(self.__window,
                                   text="Player's points and cards:")
        self.__player_info.grid(row=3, column=1)

        self.__player_points_label = Label(self.__window)
        self.__player_points_label.grid(row=4, column=1)

        self.reset()

    def start(self):
        self.__window.mainloop()

    def reset(self):
        """
        Tyhjentää pöydän korteista, sekoittaa pakan, nollaa tulokset ja
        alustaa pelin.
        :return:
        """

        self.__player_card_labels = []
        self.__kuvalista = []
        self.__player_points = []
        self.__dealer_points = []
        self.__dealer_card_labels = []
        self.__KORTIT_ALKUP = ["HA.gif", "H2.gif", "H3.gif", "H4.gif",
                               "H5.gif", "H6.gif", "H7.gif", "H8.gif",
                               "H9.gif", "H10.gif", "HJ.gif", "HQ.gif",
                               "HK.gif", "DA.gif", "D2.gif", "D3.gif",
                               "D4.gif", "D5.gif", "D6.gif", "D7.gif",
                               "D8.gif", "D9.gif", "D10.gif", "DJ.gif",
                               "DQ.gif", "DK.gif", "CA.gif", "C2.gif",
                               "C3.gif", "C4.gif", "C5.gif", "C6.gif",
                               "C7.gif", "C8.gif", "C9.gif", "C10.gif",
                               "CJ.gif", "CQ.gif", "CK.gif", "SA.gif",
                               "S2.gif", "S3.gif", "S4.gif", "S5.gif",
                               "S6.gif", "S7.gif", "S8.gif", "S9.gif",
                               "S10.gif", "SJ.gif", "SQ.gif", "SK.gif"]
        random.shuffle(self.__KORTIT_ALKUP)

        # Siirtää kortit tkinter-kuvina listaan
        for picfile in self.__KORTIT_ALKUP:
            pic = PhotoImage(file="Cards/" + picfile)
            self.__kuvalista.append(pic)

        # Käännetty kortti listan viimeiseksi.
        self.__kuvalista.append(PhotoImage(file="Cards/XX.gif"))

        # Näyttää pelaajan korttien pisteet
        for i in range(2):
            self.__player_points.append(self.__KORTIT_ALKUP[i])
        player_pts = calculate_points(self.__player_points)
        self.updatescore(player_pts, "P")

        # Asettaa kortit ikkunaan riippuen korttilistan koosta
        for i in range(len(self.__player_points)):
            new_label = Label(self.__window)
            new_label.grid(row=4, column=2 + i)
            self.__player_card_labels.append(new_label)
            self.__player_card_labels[i].configure(image=self.__kuvalista[i])

        # Näyttää jakajan osittaispisteet (toinen kortti piilossa)
        for i in range(2, 4):
            self.__dealer_points.append(self.__KORTIT_ALKUP[i])
        self.__dealer_points_label.configure(text="Points: ?".format())

        # Näytetään jakajan kortit, joista toinen on piilotettu.
        for i in range(len(self.__dealer_points)):
            new_label = Label(self.__window)
            new_label.grid(row=2, column=2 + i)
            self.__dealer_card_labels.append(new_label)

            if i == 1:
                self.__dealer_card_labels[i].configure(
                    image=self.__kuvalista[-1])

            else:
                self.__dealer_card_labels[i].configure(
                    image=self.__kuvalista[2 + i])

        self.__infobox.configure(
            text="Press 'Hit' to get a new card; "
                 "Press 'Stand' to see who wins.")
        # Nappien käyttö ja lukitus
        self.togglelock(DISABLED, NORMAL, NORMAL)

    def hit(self):
        """
        Lisää pelaajalle uuden kortin ja laskee pisteet.
        :return:
        """

        n = len(self.__player_points) + len(self.__dealer_points)
        self.__player_points.append(self.__KORTIT_ALKUP[n])
        player_pts = calculate_points(self.__player_points)
        self.updatescore(player_pts, "P")
        self.__player_card_labels = []

        for i in range(len(self.__player_points)):
            new_label = Label(self.__window)
            new_label.grid(row=4, column=2 + i)
            self.__player_card_labels.append(new_label)

            if i >= 2:
                self.__player_card_labels[i].configure(
                    image=self.__kuvalista[i + 2])

            else:
                self.__player_card_labels[i].configure(
                    image=self.__kuvalista[i])

        # Näytetään jakajan toinen kortti ja sen pisteet. Julistetaan pelaaja
        # hävinneeksi ja lukitaan tai poistetaan lukituksesta oikeat napit.
        if player_pts > 21:
            self.__dealer_card_labels[1].configure(image=self.__kuvalista[3])
            dealer_pts = calculate_points(self.__dealer_points)
            self.updatescore(dealer_pts, "D")
            self.togglelock(NORMAL, DISABLED, DISABLED)
            self.__infobox.configure(
                text="You lost! You busted because you got more than 21 "
                     "points.")

    def stand(self):
        """
        Näyttää jakajan piilotetun kortin ja jos jakajalla on alle 17 pistettä,
        hän joutuu ottamaan pakasta niin kauan kortteja, kunnes pisteitä on
        vähintään 17.

        :return:
        """

        self.__dealer_card_labels[1].configure(image=self.__kuvalista[3])
        dealer_pts = calculate_points(self.__dealer_points)
        player_pts = calculate_points(self.__player_points)
        self.updatescore(dealer_pts, "D")

        while dealer_pts < 17:
            n = len(self.__player_points) + len(self.__dealer_points)
            self.__dealer_points.append(self.__KORTIT_ALKUP[n])
            dealer_pts = calculate_points(self.__dealer_points)
            self.updatescore(dealer_pts, "D")
            self.__dealer_card_labels = []

            for i in range(len(self.__dealer_points)):
                new_label = Label(self.__window)
                new_label.grid(row=2, column=2 + i)
                self.__dealer_card_labels.append(new_label)

                if i == 0 or i == 1:
                    self.__dealer_card_labels[i].configure(
                        image=self.__kuvalista[2 + i])

                else:
                    self.__dealer_card_labels[i].configure(
                        image=self.__kuvalista[
                            n + 1 + i - len(self.__dealer_points)])

        # Voittajan julistus
        if dealer_pts > 21:
            self.__infobox.configure(text="You won! The dealer was busted.")

        elif dealer_pts == 21:
            if player_pts == dealer_pts:
                if len(self.__player_points) > len(self.__dealer_points):
                    self.__infobox.configure(
                        text="You lost! You and the dealer got Blackjack but "
                             "the dealer has fewer cards.")
                elif len(self.__player_points) < len(self.__dealer_points):
                    self.__infobox.configure(
                        text="You won! You and the dealer got Blackjack and "
                             "you have fewer cards.")
                else:
                    self.__infobox.configure(
                        text="You lost! You and the dealer got Blackjack and "
                             "both have the same amount of cards so the dealer"
                             " wins.")
            else:
                self.__infobox.configure(
                    text="You lost! The dealer got Blackjack.")
        elif player_pts == 21:
            self.__infobox.configure(text="You won! You got Blackjack.")

        elif dealer_pts > player_pts:
            self.__infobox.configure(
                text="You lost! The dealer was closer to 21 points than you.")

        elif dealer_pts < player_pts:
            self.__infobox.configure(
                text="You won! You were closer to 21 points than the dealer.")
        else:
            self.__infobox.configure(
                text="You lost! Your and the dealer's points were the same so "
                     "the dealer wins.")

        self.togglelock(NORMAL, DISABLED, DISABLED)

    def updatescore(self, pts, user):
        """
        Päivittää tuloksen näkyville
        :param pts: Lasketut pisteet
        :param user: Käyttäjä (D)ealer tai (P)layer
        """

        if user == "D":
            self.__dealer_points_label.configure(text="Points: {}".format(pts))

        elif user == "P":
            self.__player_points_label.configure(text="Points: {}".format(pts))

    def togglelock(self, New_game, Hit, stand):
        """
        Lukitsee käytöstä tai avaa nappeja käyttöön.
        :param New_game: NORMAL tai DISABLED
        :param Hit: NORMAL tai DISABLED
        :param stand: NORMAL tai DISABLED
        """

        self.__newgame.configure(state=New_game)
        self.__hit.configure(state=Hit)
        self.__stand.configure(state=stand)


def main():
    gui = Blackjack()
    gui.start()


main()
