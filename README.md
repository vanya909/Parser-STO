# Parser-STO
Программа, которая из исходных данных сделает docx документ с оформлением по СТО

## Использование:

Программа нужна, чтобы из исходных данных сделать отформатированный отчёт

### Рабочая директория

Рабочая директория может быть задана в файле конфига переменной
`WorkingDirectory`
Все файлы и директории необходимые для работы должны находиться именно в ней.
(Исходный файл, папка со скриншотами, папка с результатом, шаблон)\
По умолчанию: `working`

### Исходный файл

Имя исходного файла может быть задано в файле конфига переменной `InputFileName`
Файл должен быть в расширении `.txt`. Именно из этого файла будут браться
исходные данные для Отчёта.\
По умолчанию: `input data.txt`

### Скриншоты

Название папки скриншотов может быть задано в файле конфига переменной `ScreenshotsDirectoryName`. Оттуда будут браться все скриншоты для Отчёта.
Поддерживаются форматы `.jpeg`, `.jpg`, `.png`, `.gif`\
По умолчанию: `Screenshots`

### Папка с результатом

Название папки с результатом может быть задано в файле конфига переменной `OutputDirectoryName`. Именно в этой папке будет лежать итоговый отчёт.\
По умолчанию: `out`

### Отчёт

Имя отчёта может быть задано в файле конфига переменной `OutputFileName`\
По умолчанию: `Отчёт.docx`

## Форматирование

Данные вводятся в файл `input data.txt`
- Символ `\!` в начале строки означает, что вся строка должна быть написана ***полужирным*** текстом
- Символ `\*` в начале строки означает, что весь текст, что следует после этого
  символа до следующего такого же символа, по возможности, должен быть помещён
  на одной странице. Это нужно, чтобы избежать разрывов текста в логических
  блоках
- Для того, чтобы вставить рисунок, необходимо использовать символ `&`, за которым в треугольных скобках следует имя рисунка, т.е. `&<picture1.png>`
  - Можно также использовать имя рисунка без расширения, т.е. `&<picture1>`, но
    нужно убедиться, что отсутствует второй рисунок с таким же именем
  - Всё, что следует за именем рисунка является его описанием, т.е.
    `&<picture1>Это описание`
  - Если описание отсутствует, то будет вставлен рисунок без описания
  - Рисунки берутся из папки `Screenshots`

## Шаблон

Шаблон - это документ в формате `.docx`, который будет подставлен в итоговый
отчёт первой страницей. Этот шаблон также содержит плейсхолдеры, которые в ходе
работы программы будут заменены на определённые значения, которые задаются в
файле конфига в секции `template`. Например, если в шаблоне присутствует
плейсхолдер `{studentName}` и в конфиге присутствует переменная
`studentName="Петров Б. Б."`, то в итоговом отчёте на месте `{studentName}`
будет находиться `Петров Б. Б.`

По умолчанию шаблон используется для титульной страницы.

Имя шаблона также может быть задано в файле конфига переменной `templateName`\
По умолчанию: `template`