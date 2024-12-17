

def custom_write(file_name, strings):
    strings_positions = {}
    count = 0
    file = open(file_name, "a", encoding="utf-8")
    for stroc in strings:
        count += 1
        strings_positions[(count, file.tell())] = stroc
        file.write(f"{stroc}\n")
    file.seek(0)
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('mod_7_2.txt', info)
for elem in result.items():
  print(elem)