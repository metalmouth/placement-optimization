# Алгоритм оптимизации размещения
Алгоритм оптимизации размещения на Python. Задача решена по книге Тоби Сегарана "Программируем коллективный разум".

Также добавлены юнит-тесты (библиотека ```unittest``` в файле ```crosscount_test.py```)
<p align="center">
  <img src="https://github.com/user-attachments/assets/2ac3999e-6550-42f1-95fb-4bb1f0a12b8a" alt="network_diagram"/>
</p>

## Общее описание

В начале инициализируются списки ```people``` и ```links``` — они отражают субъектов и связи между ними соответственно, список ```links``` содержит в себе кортежи из двух элементов списка ```people```, т.е. один кортеж отражает одну связь. Функция ```crosscount``` является целевой функцией, которая получает на вход список координат субъектов. Полученный список координат преобразуется в словарь «субъект – его координаты», затем происходит перебор всех возможных соединений двух точек. Если два отрезка пересекаются (доли, создаваемые точкой пересечения лежат в промежутке от 0 до 1), то к стоимости прибавляется 1. 

Для того, чтобы в процессе визуализации точки не находились друг к другу слишком близко к стоимости в случае, когда расстояние между точками меньше 50 пикселей прибавляется пропорция (1.0 - (dist / 50.0)), где ```dist``` – расстояние между точками.

Для отрисовки в функции drawnetwork используется библиотка ```Pillow```. Функция принимает список сгенерированных координат и отображает линии и имена субъектов на изображении размером 400x400 пикселей, которое сохраняется в рабочем каталоге.

Список координат создается с помощью одной из двух функций оптимизации (файл ```optimization.py```).

**Первый метод оптимизации** — случайный подбор (функция ```randomoptimize```), в которой происходит 1000 итераций на основе списка ```domain```, определяющего область определения. Функция принимает на вход начальный список координат и целевую функцию. Решение с минимальной стоимостью принимается оптимальным.

**Второй метод оптимизации** основан на алгоритме имитации отжига. В этом алгоритме используется понятие температуры, значения, вероятность приятия решение как лучшее. В начале значение температуры очень велико, но со временем оно уменьшается, и алгоритм отсекает всё больше неоптимальных вариантов, останавливаясь на действительно оптимальном.
