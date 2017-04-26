Пакет утилит для разборки (decompiling) *epf*-, *erf*-, *ert*- и *md*-файлов и сборки (compiling) *epf*- и *erf*-файлов
===

Что делает
---

При установке пакета в каталоге скриптов интерпретатора Python создаются исполняемые файлы *decompile1c.exe* и
*compile1c.exe*. Первый используется для разборки *epf*- и *erf*-файлов с помощью 
[v8Reader][1], *ert*- и *md*-файлов с помощью 
[GComp][2], а второй для сборки *epf*- и *erf*-файлов с помощью v8Unpack. 

Пути к сервисной информационной базе, *V8Reader.epf*, *V8Unpack.exe* и GComp указываются в файле настроек 
*decompiler1cwrapper.ini*, который сначала ищется в текущем каталоге, а затем в каталоге данных приложения пользователя 
(в Windows 10 каталог *C:\\Users\\\<Пользователь>\AppData\Roaming\Util1C\Decompiler1CWrapper\>*). Если путь к платформе 
1С:Предприятие 8 в файле настроек не указан, то он ищется автоматически.

Требования
---

- Windows
- Python 3.5
- Платформа 1С:Предприятие 8.3
- Сервисная информационная база (в которой будет запускаться *V8Reader.epf*)
- [v8Reader][1]
- v8Unpack
- [GComp][2]

[1]: https://github.com/xDrivenDevelopment/v8Reader
[2]: http://1c.alterplast.ru/gcomp/