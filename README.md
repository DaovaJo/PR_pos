# PR_pos

ОТЧЕТ ПОСЕЩАЕМОСТИ СТУДЕНТОВ ПО

Входные данные:
    		Студент: ФИО, ID
    		Группа: ЗВД и очка (студенты ДОТ не в счет)
    		Курсы: 1 (полный и СПО), 2 (полный и СПО), 3 (полный и СПО), 4 (полный и СПО)
    	    Преподаватели: все виды договоров (ГПХ и штат)
    		Дисциплина

Выход:
o	Студенты
    ПОИСК – поиск ведется по ФИО и ID (используемые входные данные)
    По настройке «студенты» получить на выходе:

    ФАЙЛЫ НУЖНЫЕ ДЛЯ РАБОТЫ
    	Excel таблицу
    Column: ID, ФИО, учебная группа, вход-выход студента
    	ДИАГРАММА (matplotlib или уже GUI)
    	ВВОД ДАННЫХ ПО СПРАВКЕ – исключить из периода отсутствия по неуважительной причине и ВКЛЮЧИТЬ в период отсутствия по УВАЖИТЕЛЬНОЙ причине
    УСЛОВИЕ:
    Высчитывать посещаемость по планируемым парам по выписке из СИРИУС. 


Если студент в зоне посещаемости менее 80% за отчетный период, студен попадает в список студентов на дисциплинарное взыскание. (требуемый вид отчета - ОТДЕЛЬНЫЙ)


Если студент 2 раза попадает в список о дисциплинарном взыскании, то студент автоматически попадает в список на отчисление (требуемый вид отчета – ОТДЕЛЬНЫЙ)
![image](https://user-images.githubusercontent.com/103495315/205715084-c4bdb98b-16ac-478c-a1ee-127ff50dc755.png)



УЧИТЫВАТЬ ОПОЗДАНИЕ СТУДЕНТА НА БОЛЕЕ 10-15 МИНУТ
(должна быть регулируемая настройка)

   o	ГРУППА

Высчитать посещаемость группы по среднему показателю посещаемости студентов группы 
![image](https://user-images.githubusercontent.com/103495315/205715305-9d202162-a893-42a5-8532-8ce2e6780557.png)

 

   o	КУРС

Вычислить среднюю посещаемость студентов по средним показателям групп.
ПРИМЕЧАНИЕ – подсчет идет отдельно по потоку очки и отдельно по ЗВД и ОЗВД (СПО не считается)

 ![image](https://user-images.githubusercontent.com/103495315/205715421-2f68aa6b-7ed9-4a2b-8e1e-1123b2ae59e2.png)


Дополнительная настройка посещаемость по преподавателю и по дисциплине.
Также круговая диаграмма или же гистограмма (посмотрим)
Планируемый UI/UX дизайн для ПО

 
