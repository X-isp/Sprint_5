# При создании матрёшки будем передавать значение size в конструктор класса, 
# а при рекурсивном разборе заставим функцию печатать размер каждой матрёшки. 
# У каждой матрёшки есть атрибут size — размер матрёшки, обозначенный символами:
    # XXS (extra extra small) — крошечный;
    # XS (extra small) — очень маленький;
    # S (small) — маленький;
    # M (medium) — средний;
    # L (large) — большой;
    # XL (extra large) — очень большой;
    # XXL (extra extra large) — очень-очень большой.

class Matryoshka:

    def __init__(self, size, item=None):
        self.size = size
        self.inner_item = item


if __name__ == '__main__':
    # 1 Вариант создания экземпляров класса Matryoshka:

    # # Создаём самую маленькую матрёшку. Внутри неё ничего нет. Размер S.
    # the_smallest_one = Matryoshka('S')
    # # Создаём матрёшку побольше - размера M. 
    # # И передаём ей в конструктор самую маленькую матрёшку.
    # the_middle_one = Matryoshka('M', the_smallest_one)
    # # Создаём матрёшку побольше, размера L; передаём в её конструктор 
    # # матрёшку размера M.
    # the_biggest_one = Matryoshka('L', the_middle_one) 

    # 2 Вариант создания экземпляров класса Matryoshka:
    the_biggest_one = Matryoshka('L', Matryoshka('M', Matryoshka('S')))

    # Размер большой матрёшки.
    print(the_biggest_one.size)

    # Размер матрёшки, вложенной в большую.
    print(the_biggest_one.inner_item.size)

    # Размер матрёшки, вложенной во вложенную в большую.
    print(the_biggest_one.inner_item.inner_item.size)

    # Содержимое наименьшей матрёшки.
    print(the_biggest_one.inner_item.inner_item.inner_item)