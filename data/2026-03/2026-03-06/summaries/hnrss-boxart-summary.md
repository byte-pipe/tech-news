---
title: BoxArt
url: https://boxart.lt/blog/poor_mans_polaroid
date: 2026-03-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-06T06:01:39.879328
---

# BoxArt

# Vargšo Žmogaus Polaroidas – santrauka

## Pagrindinė idėja
- Sukurtas nebrangus „Polaroido“ pakaitalas, naudojantis čekių spausdintuvą.
- Nuotraukų kaina: Polaroido – apie 1 € vienam, šio įrenginio – mažiau nei 1 centas.
- Įrenginys nebrangus dėl savarankiško komponentų įsigijimo ir didelio spausdinimo popieriaus (50 m čekių rulonas) kainos santykio.

## Komponentai
- **Kompiuteris**: Raspberry Pi Zero, veikia kaip valdiklis, apdoroja nuotrauką ir siunčia ją į spausdintuvą.
- **Kameros modulis**: Pi kamera su laidu, kompaktiška ir lengvai integruojama.
- **Elektra**: Galimi trys variantai – tiesioginis maitinimas iš rozetės, savarankiškas įkrovimo rinkinys (baterija, įtampos keitiklis, krovimo valdiklis) arba įsigytas power bankas.
- **Spausdintuvas**: Mažas šilumos spausdintuvas, reikalaujantis specifinio čekių popieriaus (modelis PT‑310, įsigytas iš Kinijos).

## Energijos sprendimai
- Power bankas naudojamas dėl patogumo ir mažesnės kainos nei atskirų dalių rinkinys.
- Saugumo patarimai: naudoti apsauginius akinius, vengti tiesioginio kontakto su baterija, galimas gaisro gesinimas vandeniu (reikalingas smėlis, kad nebūtų trumpas).

## Spaudintuvas ir sąsaja
- Prijungimas prie Raspberry Pi per laidą arba Bluetooth.
- Spausdintuvas šildo popierių vietoj rašalo, todėl spausdinimas yra greitas ir ekonomiškas.
- Rekomenduojamas modelis: PT‑310 (kaina nuo 20 € iki 60 €).

## Dėžės konstrukcija
- Dėžės dizainas sukurtas FreeCAD programoje, išspausdintas 3D spausdintuvu.
- Dėžė suskirstyta į kelias dalis: spausdintuvo skyrius, baterijos ir kompiuterio modulis, mygtukų laikiklis, kosmetiniai elementai.
- Baigiamasis apdorojimas: šlifavimas, glaisto užtepimas, dažymas (minty geltona su juoda).

## Surinkimas ir valdymas
- Įmontuoti LED indikatoriai: mėlyna – elektros tiekimas, žalia – įrenginys paruoštas, raudona – vyksta spausdinimas.
- Mygtukai: įjungimo/išjungimo (per jungiklį), fotoaparato nuotraukos darymo, pakartotinio spausdinimo, termometro (baterijos perkaitimo apsauga).
- Power banko modulis su ekranu ir įkrovimo lizdu integruotas į korpusą.

## Programavimas
- Programinė įranga rašyta Python kalba, naudojama biblioteka `picamera2` ir `escpos.printer`.
- Pagrindinės funkcijos: nuotraukų fiksavimas, šviesumo matavimas, histogramų lygiavimas, gama korekcija, CLAHE taikymas.
- Kodo fragmentas pateiktas straipsnyje, visas šaltinis prieinamas skaitytojui.

## Išvados ir privalumai
- Žymiai mažesnės nuotraukų gamybos išlaidos nei tradicinis Polaroidas.
- Lankstus energijos šaltinis (baterija, power bankas, tinklo maitinimas).
- Galimybė pritaikyti programinį apdorojimą ir papildomas funkcijas (pvz., termometro apsauga).
- Savarankiškas dizainas ir 3D spausdinimas leidžia pritaikyti įrenginį pagal asmeninius poreikius.