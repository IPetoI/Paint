import cv2 as cv
import numpy as np
import time


def mouse_click(event, x, y, flags, param):
    global kep, kep2, egerLenyomva, korSugar, korSzin, x0, y0, alakzat
    x0 = x
    y0 = y

    if event == cv.EVENT_LBUTTONUP:
        egerLenyomva = False

    if event == cv.EVENT_LBUTTONDOWN:
        egerLenyomva = True
        cv.circle(kep, (x, y), korSugar, korSzin, -1)
        if alakzat == "kor":
            cv.circle(kep, (x, y), korSugar, korSzin, -1)
        elif alakzat == "teglalap":
            cv.rectangle(kep, (x - korSugar, y - korSugar), (x + korSugar, y + korSugar), korSzin, -1, 1)
        elif alakzat == "elipszis":
            cv.ellipse(kep, (x, y), (0, korSugar), 0, 0, 360, korSzin, 5, -1)
        cv.imshow('Paint', kep)

    if event == cv.EVENT_MOUSEMOVE:
        milyenEger(kep2, x0, y0, korSugar, korSzin)
        if egerLenyomva:
            if alakzat == "kor" or alakzat is None:
                cv.circle(kep, (x, y), korSugar, korSzin, -1)
            elif alakzat == "teglalap":
                cv.rectangle(kep, (x - korSugar, y - korSugar), (x + korSugar, y + korSugar), korSzin, -1, 1)
            elif alakzat == "elipszis":
                cv.ellipse(kep, (x, y), (0, korSugar), 0, 0, 360, korSzin, 5, -1)
            cv.imshow('Paint', kep)


egerLenyomva = False

for i in range(2):
    time.sleep(0.1)
    if i>0:
        alakzat="kor"

def milyenEger(kep2, x, y, korSugar, korSzin):
    kep2.fill(255)
    cv.circle(kep2, (x, y), korSugar, korSzin, -1)
    maszkos = cv.bitwise_and(kep2, kep)
    cv.imshow('Paint', maszkos)


kep = np.ndarray((480, 640, 3), np.uint8)
kep.fill(255)
kep2 = np.ndarray((480, 640, 3), np.uint8)
kep2.fill(255)
mask = np.ndarray((480, 640, 3), np.uint8)
mask.fill(0)

print('\n'"-- Rajzolo program --")

print('\n''Szinek: R -> Piros''          ''Ecset merete: Nagyitas    -> + ''      '
      '      Alakzatok: ''Kor       -> o''            Egyeb: ''Lap Torlese -> t''\n'
      '        G -> Zold''                         ''Kicsinyites -> -''                '
      '        ''Teglalap  -> p''                   ''Mentes      -> s'
      '\n''        B -> Kek''                                                                 '
      ' ''Elipszis  -> i''                   ''Kilepes     -> q vagy ESC'
      '\n''        K -> Fekete''\n''        W -> Feher')

korSugar = 10
korSzin = (0, 0, 255)

cv.imshow('Paint', kep)
cv.setMouseCallback('Paint', mouse_click)

while True:
    key = cv.waitKey(0)

    if key == 43:
        if korSugar < 100:
            korSugar = korSugar + 5
            milyenEger(kep2, x0, y0, korSugar, korSzin)
    elif key == 45:
        if korSugar > 5:
            korSugar = korSugar - 5
            milyenEger(kep2, x0, y0, korSugar, korSzin)

    elif key == key == 82 or key == 114:
        korSzin = (0, 0, 255)
        milyenEger(kep2, x0, y0, korSugar, korSzin)
    elif key == key == 71 or key == 103:
        korSzin = (0, 255, 0)
        milyenEger(kep2, x0, y0, korSugar, korSzin)
    elif key == key == 66 or key == 98:
        korSzin = (255, 0, 0)
        milyenEger(kep2, x0, y0, korSugar, korSzin)
    elif key == key == 75 or key == 107:
        korSzin = (0, 0, 0)
        milyenEger(kep2, x0, y0, korSugar, korSzin)
    elif key == key == 87 or key == 119:
        korSzin = (255, 255, 255)
        milyenEger(kep2, x0, y0, korSugar, korSzin)

    elif key == 84 or key == 116:
        kep.fill(255)
        cv.imshow('Paint', kep2)

    elif key == 83 or key == 115:
        cv.imwrite('Rajz.png', kep)
        print('Sikeres mentes!')

    elif key == 81 or key == 113 or key == 27:
        break

    elif key == 79 or key == 111:
        alakzat = "kor"
    elif key == 80 or key == 112:
        alakzat = "teglalap"
    elif key == 73 or key == 105:
        alakzat = "elipszis"

cv.destroyAllWindows()