---
title: GitHub - Flowseal/zapret-discord-youtube · GitHub
url: https://github.com/Flowseal/zapret-discord-youtube
site_name: github
content_file: github-github-flowsealzapret-discord-youtube-github
fetched_at: '2026-05-01T11:58:25.090421'
original_url: https://github.com/Flowseal/zapret-discord-youtube
author: Flowseal
description: Contribute to Flowseal/zapret-discord-youtube development by creating an account on GitHub.
---

Flowseal

 

/

zapret-discord-youtube

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star26.9k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

432 Commits
432 Commits
.github
.github
 
 
.service
.service
 
 
bin
bin
 
 
lists
lists
 
 
utils
utils
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
general (ALT).bat
general (ALT).bat
 
 
general (ALT10).bat
general (ALT10).bat
 
 
general (ALT11).bat
general (ALT11).bat
 
 
general (ALT2).bat
general (ALT2).bat
 
 
general (ALT3).bat
general (ALT3).bat
 
 
general (ALT4).bat
general (ALT4).bat
 
 
general (ALT5).bat
general (ALT5).bat
 
 
general (ALT6).bat
general (ALT6).bat
 
 
general (ALT7).bat
general (ALT7).bat
 
 
general (ALT8).bat
general (ALT8).bat
 
 
general (ALT9).bat
general (ALT9).bat
 
 
general (FAKE TLS AUTO ALT).bat
general (FAKE TLS AUTO ALT).bat
 
 
general (FAKE TLS AUTO ALT2).bat
general (FAKE TLS AUTO ALT2).bat
 
 
general (FAKE TLS AUTO ALT3).bat
general (FAKE TLS AUTO ALT3).bat
 
 
general (FAKE TLS AUTO).bat
general (FAKE TLS AUTO).bat
 
 
general (SIMPLE FAKE ALT).bat
general (SIMPLE FAKE ALT).bat
 
 
general (SIMPLE FAKE ALT2).bat
general (SIMPLE FAKE ALT2).bat
 
 
general (SIMPLE FAKE).bat
general (SIMPLE FAKE).bat
 
 
general.bat
general.bat
 
 
service.bat
service.bat
 
 
View all files

## Repository files navigation

# Flowseal/zapret-discord-youtube

NEW: Ускорение Telegram Desktop -https://github.com/Flowseal/tg-ws-proxyАльтернативаhttps://github.com/bol-van/zapret-win-bundleТакже вы можете материально поддержать оригинального разработчика zapretтут

Caution

### ФЕЙКИ

Я не веду никакие другие страницы/группы в телеграм/ютуб каналыЕсли вы наткнулись на что-то вне этой страницы гитхаба, что распространяется от моего лица -ФЕЙК.

Warning

### АНТИВИРУСЫ

WinDivert может вызвать реакцию антивируса.
WinDivert - это инструмент для перехвата и фильтрации трафика, необходимый для работы zapret.
Замена iptables и NFQUEUE в Linux, которых нет под Windows.
Он может использоваться как хорошими, так и плохими программами, но сам по себе не является вирусом.
Драйвер WinDivert64.sys подписан для возможности загрузки в 64-битное ядро Windows.

*Выдержка изreadme.mdрепозиторияbol-van/zapret-win-bundle

Некоторые антивирусы склонны относить файлы WinDivert к классам повышенного риска или хакерским инструментам. Происходит удаление файла и помещение его в карантин. При этом детект обязательно имеет названиеWinDivertилиNot-a-virus:RiskTool.Multi.WinDivert

В случае проблем с антивирусом добавьте папку с запретом в исключения, либо отключите детектирование PUA (потенциально нежелательных приложений). Например, в касперском есть галочка "Обнаруживать легальные приложения, которые злоумышленники часто используют для нанесения вреда". При аккуратной и правильной настройке исключений - рекомендуется настроить исключение, но если вы не до конца понимаете что делаете - рекомендуется отключить детект PUA.

Important

Все бинарные файлы в папкеbinвзяты изzapret-win-bundle/zapret-winwsиzapret/releases. Вы можете это проверить с помощью хэшей/контрольных сумм. Проверяйте, что запускаете, используя сборки из интернета!

## ⚙️Использование

1. Включите Secure DNS* В Chrome - "Использовать безопасный DNS", и выбрать поставщика услуг DNS (выбрать вариант, отличный от поставщика по умолчанию)
* В Firefox - "Включить DNS через HTTPS, используя: Максимальную защиту", затем "Выбрать поставщика" и вписать URL поставщика вручную, например можно использоватьhttps://dns.google/dns-query(т.к. поставщик Cloudflare может быть заблокирован)
* В Windows 11 поддерживается включение Secure DNS прямо в настройках ОС -инструкция тут. Рекомендуется, если вы пользуетесь Windows 11
2. Скачайте архив (zip/rar) состраницы последнего релиза
3. Зайдите в свойства скачанного архива и поставьте галочку "Разблокировать". Если вы используете архиватор 7-Zip или PeaZip, этот шаг можно пропустить
4. Распакуйте содержимое архива по пути, который не содержит кириллицу/спец. символы
5. Запустите нужный файл

## ℹ️Краткие описания файлов

* general.bat ...- запуск стратегии вручнуюЗапуск вручную можно использовать для проверки работоспособности стратегий. Работоспособность той или иной стратегии зависит от многих факторов.Пробуйте разные стратегии (ALT, FAKE и другие), пока не найдёте рабочее для вас решение
* service.bat- установка в автозапуск и другие функции:Install Service- установка любой стратегии в автозапуск (services.msc)Remove Services- удаление стратегии и WinDivert из службCheck Status- проверка статуса обхода и служб (стратегии на автозапуске и WinDivert)Game Filter- переключение режима обхода для игр (и других сервисов, использующих UDP и TCP на портах выше 1023).После переключения требуется перезапуск стратегии.В скобках указан текущий статус (включено/выключено).IPSet Filter- переключение режима обхода сервисов изipset-all.txt.Полезно при тестировании, если не работает ресурс, который без zapret работаетВ скобках указан текущий статус:none- никакие айпи не попадают под проверкуloaded- айпи проверяется на вхождение в списокany- любой айпи попадает под фильтрAuto-Update Check- Вкл/Выкл автоматическую проверку на обновленияUpdate IPSet List- обновление спискаipset-all.txtактуальным из репозиторияUpdate Hosts File- обновление файла hostsдля починки веб версии телеграма и подключения к голосовому чату DiscordCheck for Updates- проверка на обновленияRun Diagnostics- диагностика на распространённые причины, по которым zapret может не работать.В конце можно очистить кэшDiscord, что может помочь, если он неожиданно перестал работатьRun Tests- запуск утилиты для проверки стратегий на работоспособность:Standard tests- проверка сайтов изutils/targets.txtDPI checkers- проверка DPI на различных провайдерах (Cloudflare, Amazon и др.)
* Install Service- установка любой стратегии в автозапуск (services.msc)
* Remove Services- удаление стратегии и WinDivert из служб
* Check Status- проверка статуса обхода и служб (стратегии на автозапуске и WinDivert)
* Game Filter- переключение режима обхода для игр (и других сервисов, использующих UDP и TCP на портах выше 1023).После переключения требуется перезапуск стратегии.В скобках указан текущий статус (включено/выключено).
* IPSet Filter- переключение режима обхода сервисов изipset-all.txt.Полезно при тестировании, если не работает ресурс, который без zapret работаетВ скобках указан текущий статус:none- никакие айпи не попадают под проверкуloaded- айпи проверяется на вхождение в списокany- любой айпи попадает под фильтр
* none- никакие айпи не попадают под проверку
* loaded- айпи проверяется на вхождение в список
* any- любой айпи попадает под фильтр
* Auto-Update Check- Вкл/Выкл автоматическую проверку на обновления
* Update IPSet List- обновление спискаipset-all.txtактуальным из репозитория
* Update Hosts File- обновление файла hostsдля починки веб версии телеграма и подключения к голосовому чату Discord
* Check for Updates- проверка на обновления
* Run Diagnostics- диагностика на распространённые причины, по которым zapret может не работать.В конце можно очистить кэшDiscord, что может помочь, если он неожиданно перестал работать
* Run Tests- запуск утилиты для проверки стратегий на работоспособность:Standard tests- проверка сайтов изutils/targets.txtDPI checkers- проверка DPI на различных провайдерах (Cloudflare, Amazon и др.)
* Standard tests- проверка сайтов изutils/targets.txt
* DPI checkers- проверка DPI на различных провайдерах (Cloudflare, Amazon и др.)

## ☑️Распространенные вопросы и проблемы

### После запуска скриптаgeneral*ничего не происходит

* После запуска стратегии (отдельным bat файлом, не через service), должен открыться winws.exe (обход), который можно увидеть в панели задач.Если этого не произошло, то см.#522

### Не работает телеграм (веб версия) или бесконечное "подключение" к голосовому чату Discord

Запуститеservice.bat, выберите пунктUpdate hosts file. После чего, если ваш hosts будет неактуальным, то Вам будет предложено обновить его самостоятельно:

* Скопируйте весь текст из открывшегося блокнота
* Откройте файлhostsв появившейся папке с помощью текстового редактора, открытого от имени администратора
* Добавьте в конец файлаhostsто, что скопировали (или замените, если до этого Вы уже добавляли подобное)
* Сохраните и перепроверьте подключение. Если не работает - убедитесь, что файлhostsдействительно сохранился.

### Обход не работает / перестал работать

Important

Стратегии со временем могут переставать работать.Определенная стратегия может работать какое-то время, но со временем она может переставать работать из-за обнаружения.
В репозитории представлены множество различных стратегий для обхода. Если ни одна из них вам не помогает, то вам необходимо создать новую, взяв за основу одну из представленных здесь и изменив её параметры.
Информацию про параметры стратегий вы можете найтитут.

* Проверьте, чтобы не было ошибок вservice.bat->Run Diagnostics
* Убедитесь, что адрес ресурса записан в списках доменов или IP
* Проверьте другие стратегии (ALT/FAKEи другие)
* Попробуйте полную переустановку (см. раздел ниже)
* См.#765

### Как переустановить/обновить полностью?

* Сохраните ресурсы/данные, которые вы сами добавляли
* Перезапустите устройство
* service.bat->Remove Services
* service.bat->Run Diagnostics(если есть ошибки - устраните их) -> в конце Y
* Удалите папку с запретом
* Скачайте последнюю версиюсо страницы релизов(zapret-discord-youtube-...)
* Нажмите пкм по архиву -> свойства. Если снизу справа есть галочка разблокировать, то нажмите на неё -> применить -> ОК
* Распакуйте в новую папку в корне диска (без спец. символов и пробелов)
* Далее пробуйте запускать различныеgeneralскрипты (стратегии). Проверьте доступность интернет ресурсов - если не работают, то закрывайте программу (в панели задач иконка замочка) и пробуйте другую стратегию
* Как найдёте рабочую стратегию, можете поставить её на автозапуск:service.bat->Install Service-> выбираете нужную

### Не работает игра/приложение с включённым запретом

* Проверьте, что в service.batGame Filterdisabled, аIPSet Filternone. Иначе это может затронуть доступность ресурсов, которых вы не ожидали.

### Античит ругается на WinDivert

* Прочитайте инструкцию тут -https://github.com/bol-van/zapret-win-bundle/tree/master/windivert-hide

### Требуется цифровая подпись драйвера WinDivert (Windows 7)

* Замените файлыWinDivert.dllиWinDivert64.sysв папкеbinна одноименные изzapret-win-bundle/win7

### При удалении с помощьюservice.bat, WinDivert остается в службах

1. Узнайте название службы с помощью команды, в командной строке Windows (Win+R,cmd):

driverquery
 
|
 
find
 
"
Divert
"

1. Остановите и удалите службу командами:

sc
 stop название_из_первого_шага

sc
 delete название_из_первого_шага

### Не работаетYouTube

* Убедитесь что вы настроили Secure DNS.
* Отключите блокировщик рекламы, известно что YouTube начал с ними бороться.
* Пробуйте все другие стратегии (если раньше работало, но перестало).
* См. также#251

### Не работаетDiscord

* Желательно сначала узнать, на какой стратегии открывается сайт YouTube. Запустите эту стратегию.
* Проверьте Discord в браузере:https://discord.com/app. В браузере работает? Если работает, то можете пользоваться в нём.
* Если Discord и в браузере не работает, убедитесь что вы настроили Secure DNS, и после этого ещё раз пробуйте все стратегии. Бывает такое, что на одной стратегии YouTube работает, а Discord нет.
* См. также#252

### Не нашли своей проблемы

* Создайте еётут

## 🗒️Добавление адресов прочих ресурсов

Список адресов для обхода можно расширить, добавляя их в:

* list-general-user.txtдля доменов (поддомены автоматически учитываются)
* list-exclude-user.txtдля исключения доменов (например, если айпи сети указан вipset-all.txt, но конкретный домен из этой сети не надо фильтровать)
* ipset-all.txtдля IP и подсетей
* ipset-exclude-user.txtдля исключения IP и подсетейФайлы*-user.txtавтоматически создадутся при первом запускеzapretилиservice.bat
* Файлы*-user.txtавтоматически создадутся при первом запускеzapretилиservice.bat

## ⭐Поддержка проекта

Вы можете поддержать проект, поставив ⭐ этому репозиторию (сверху справа этой страницы)

Также вы можете материально поддержать оригинального разработчика zapretтут

## ⚖️Лицензирование

Проект распространяется на условиях лицензииMIT

## 🩷Благодарность участникам проекта

💖 Отдельная благодарность разработчикуzapret-bol-van

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

26.9k

 stars
 

### Watchers

285

 watching
 

### Forks

2.1k

 forks
 

 Report repository

 

## Releases39

1.9.8b

 Latest

 

Apr 30, 2026

 

+ 38 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Batchfile72.0%
* PowerShell28.0%