import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Ustawiamy piny na wyjscie
GPIO.setup(0, GPIO.OUT)         #Ustawienie pinu dla PWM dla silnika lewego
GPIO.setup(1, GPIO.OUT)         #Ustawienie kierunku dla silnika lewego
GPIO.setup(14, GPIO.OUT)        #Ustawienie pinu dla PWM dla silnika prawego
GPIO.setup(15, GPIO.OUT)        #Ustawienie kierunku dla silnika prawego

#Ustawiamy piny na wejscie
GPIO.setup(17, GPIO.IN)         #Dla lewego czujnika
GPIO.setup(27, GPIO.IN)         #Dla prawego czujnika
GPIO.setup(22, GPIO.IN)         #Guzik, ktory sluzy do zakonczenia programu

#Ustawiamy programowy PWM na pinach GPIO0 oraz GPIO14 czestotliwosc sygnalu to 50Hz
l=GPIO.PWM(0,50)
p=GPIO.PWM(14,50)

def sterowanie():               #Funkcja zajmujaca sie sterowaniem silnikami
    while(GPIO.input(22)==False):   #Petla dziala tak dlugo jak guzik pod GPIO22 nie jest wcisniety
        if((GPIO.input(17)==False) and (GPIO.input(27)==False)):    #Wtedy kiedy czujniki nie widza "celu"
            GPIO.output(1, 1)                                       #Ustawia lewy silnik na jazde do przodu
            GPIO.output(15, 0)                                      #Ustawia prawy silnik na jazde do tylu
            l.start(50)                                             #Ustawia poziom wypelnienia sygnalu na lewy silnik na 50%
            p.start(50)                                             #Ustawia poziom wypelnienia sygnalu na prawy silnik na 50%

        if((GPIO.input(17)==True) and (GPIO.input(27)==False)):     #Wtedy gdy lewy czujnik widzi "cel"
            GPIO.output(1, 0)                                       #Ustawia lewy silnik na jazde do tylu
            GPIO.output(15, 1)                                      #Ustawia prawy silnik na jazde do przodu
            l.start(65)                                             #Ustawia poziom wypelnienia sygnalu na lewy silnik na 65%
            p.start(65)                                             #Ustawia poziom wypelnienia sygnalu na prawy silnik na 65%

        if((GPIO.input(17)==False) and (GPIO.input(27)==True)):     #Wtedy gdy prawy czujnik widzi "cel"
            GPIO.output(1, 1)                                       #Ustawia lewy silnik na jazde do przodu
            GPIO.output(15, 0)                                      #Ustawia prawy silnik na jazde do tylu
            l.start(65)                                             #Ustawia poziom wypelnienia sygnalu na lewy silnik na 65%
            p.start(65)                                             #Ustawia poziom wypelnienia sygnalu na prawy silnik na 65%

        if((GPIO.input(17)==True) and (GPIO.input(27)==True)):      #Wtedy gdy oba czujniki widza "cel"
            GPIO.output(1, 1)                                       #Ustawia lewy silnik na jazde do przud
            GPIO.output(15, 1)                                      #Ustawia prawy silnik na jazde do przodu
            l.start(100)                                            #Ustawia poziom wypelnienia sygnalu na lewy silnik na 100%
            p.start(100)                                            #Ustawia poziom wypelnienia sygnalu na prawy silnik na 100%
        time.sleep(0.1)
    l.stop()                                #Zatrzymanie pracy lewego silnika
    p.stop()                                #Zatrzymanie pracy prawego silnika

    if __name__=="__main__":
    print "Program wyszukuje cel po czym za nim podaza przy uzyciu czujnikow cyfrowych"
    sterowanie()
    GPIO.cleanup()              #Czyscimy ustawienia GPIO by zabezpieczyc RaspberryPi oraz miec "clean exit"
