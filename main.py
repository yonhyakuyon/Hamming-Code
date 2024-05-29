import random
def hamming_encode(data):
    # Предполагаем, что data - это строка из 4 бит, например "1011"
    if len(data) != 4 or not all(bit in '01' for bit in data):
        raise ValueError("Это должна быть 4-битовая строка")

    d = list(map(int, data))  # Преобразуем строку в список целых чисел

    # Места контрольных битов: p1, p2, d1, p3, d2, d3, d4
    hamming_code = [0] * 7

    # Расставляем информационные биты
    hamming_code[2] = d[0]
    hamming_code[4] = d[1]
    hamming_code[5] = d[2]
    hamming_code[6] = d[3]

    # Вычисляем контрольные биты
    hamming_code[0] = hamming_code[2] ^ hamming_code[4] ^ hamming_code[6]
    hamming_code[1] = hamming_code[2] ^ hamming_code[5] ^ hamming_code[6]
    hamming_code[3] = hamming_code[4] ^ hamming_code[5] ^ hamming_code[6]

    return ''.join(map(str, hamming_code))

# Пример использования
data = input()
encoded = hamming_encode(data)
print(f"Закодированная информация: {encoded}")

def hamming_decode(code):
    # Предполагаем, что code - это строка из 7 бит, например "0110011"
    if len(code) != 7 or not all(bit in '01' for bit in code):
        raise ValueError("Code must be a 7-bit binary string")

    h = list(map(int, code))  # Преобразуем строку в список целых чисел

    # Вычисляем синдромы
    p1 = h[0] ^ h[2] ^ h[4] ^ h[6]
    p2 = h[1] ^ h[2] ^ h[5] ^ h[6]
    p3 = h[3] ^ h[4] ^ h[5] ^ h[6]

    # Определяем ошибочный бит
    error_position = p1 + (p2 << 1) + (p3 << 2) - 1

    #Исправляем ошибку, если есть
    if error_position >= 0:
        h[error_position] ^= 1

    # Извлекаем информационные биты
    data = [h[2], h[4], h[5], h[6]]

    return ''.join(map(str, data))

def hamming_decode_error(code):
    # Предполагаем, что code - это строка из 7 бит, например "0110011"
    if len(code) != 7 or not all(bit in '01' for bit in code):
        raise ValueError("Code must be a 7-bit binary string")

    h = list(map(int, code))  # Преобразуем строку в список целых чисел

    # Вычисляем синдромы
    p1 = h[0] ^ h[2] ^ h[4] ^ h[6]
    p2 = h[1] ^ h[2] ^ h[5] ^ h[6]
    p3 = h[3] ^ h[4] ^ h[5] ^ h[6]

    # Извлекаем информационные биты
    data = [h[2], h[4], h[5], h[6]]

    return ''.join(map(str, data))
def replace_random_char(s):
    # Преобразуем строку в список символов для удобства замены
    s_list = list(s)

    # Генерируем случайный индекс
    index = random.randint(0, len(s) - 1)

    # Проверяем символ по этому индексу и выполняем замену
    if s_list[index] == '0':
        s_list[index] = '1'
    elif s_list[index] == '1':
        s_list[index] = '0'

    # Преобразуем список обратно в строку
    new_s = ''.join(s_list)

    return new_s

# Пример использования
decoded = hamming_decode(encoded)
print(f"Декодированная информация с исправлением ошибки: {decoded}")
for i in range(3):
    new = replace_random_char(encoded)
    errors = hamming_decode_error(new)
    print(f"Декодированная информация с ошибками: {errors}")