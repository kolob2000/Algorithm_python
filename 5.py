first, second = map(ord, input('введите две английских буквы через пробел - ').lower().split())

if first > second:
    _ = first
    first = second
    second = _
print(f'Первый символ - {chr(first)} - {first - 96}, второй символ - {chr(second)} - {second - 96}')

print(f'Между ними {second - first - 1} символ(ов)')
