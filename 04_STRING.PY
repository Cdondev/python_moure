my_string = "mi strig"
my_other_string = 'mi otra string'

print(len(my_other_string))
print(len(my_string))

my_mew_line_string = 'este es un string\ncon salto de linea '
print(my_mew_line_string)

my_string_con_tab = '\teste es un strin con tabulacion'
print(my_string_con_tab)


#formateo 

name, surname, age = 'carlos', 'Dominguez', 24
print('mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('mi nombre es %s %s y mi edad es %d' % (name,surname,age))
print(f'mi nombre es {name} {surname} y mi edad es {age}')

#desenpaquetado de caracteres

language ='python'
a,b,c,d,e,f = language
print(a)
print(c)

language_other = language[1:3]
print(language_other)

language_alide = language[-2]
print(language_alide)

language_reverse = language[::-1]
print(language_reverse)

#operaciones

print(language.capitalize())
print(language.upper())
print(language.count('p'))
print(language.isnumeric())
print(language.lower())