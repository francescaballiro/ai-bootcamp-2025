#funzione mydivmod
def mydivmod(a, b):
    divisione = (a//b)
    resto = (a%b)
    risultato = (divisione, resto)
    return(risultato)


#funzione pow_list
def pow_list(*lista):
    '''Implement a function that takes a list
    and returns another list with each value raised
    to the power of 2'''
    quadrato = []
    for el in lista:
        risultato = el**2
        quadrato.append(risultato)
    return(quadrato)
assert pow_list([1, 2, 3] == [1, 4, 9])

#funzione count_words
def count_words(stringa):
    ''' Implement a trivial function that counts the
    number of words in the given string.'''
    lista= stringa.split()  #split divide la stringa in una lista contenente tutte le parole della str come elemento
    return (len(lista))
assert count_words("hello world")

#funzione reverse_string
def reverse_string(parola):
    ''' Implement a function that takes a string
    and returns it reversed.'''
    lista = []
    for x in parola:
        lista += [x]
    contrario = lista[: : -1]
    parola2 = ""
    for el in contrario:
        parola2 += str(el)
    return(parola2)
assert reverse_string("hello") == "olleh"

#funzione factorial
def factorial(n):
    ''' Implement a function that computes the factorial of a given number.
    Factorial of n (n!) is the product of all positive integers from 1 to n.'''
    risultato = 1
    for i in range (1, n+1):
        risultato *= i
    return(risultato)
assert factorial(5) == 120

#funzione is_palindrome
def is_palindrome(parola):
    '''Implement a function that checks if a given string is a palindrome.'''
    stringa1 = parola
    lista = []
    for x in stringa1:
        lista += [x]
    contrario = lista[: : -1]
    stringa2 = ""
    for el in contrario:
        stringa2 += str(el)
    if stringa1 == stringa2:
        return True
    else:
        return False
assert is_palindrome("racecar") == True

#funzione  sum_even_numbers
def  sum_even_numbers(lista =[]):
    '''Implement a function that takes a list of numbers
    and returns the sum of all even numbers in the list.'''
    risultato = 0
    for x in lista:
        if x%2 == 0:
            risultato += x
        else:
            risultato == risultato
    return(risultato)
assert sum_even_numbers([1, 2, 3, 4, 5]) == 6

#funzione find_max
def find_max(lista=[]):
    lista.sort()
    massimo=lista[-1]
    return(massimo)
assert find_max([3, 1, 4, 1, 5]) == 5



#funzione count_vowels
def count_vowels(stringa):
    '''Implement a function that takes a string
    and returns the count of vowels ('a', 'e', 'i', 'o', 'u') in it.'''
    contatore = 0
    for el in stringa:
        if el == "a":
            contatore +=1
        elif el == "e":
            contatore +=1
        elif el == "i":
            contatore +=1
        elif el == "o":
            contatore +=1
        elif el == "u":
            contatore +=1
        else:
            contatore == contatore
    return (contatore)
assert count_vowels("hello world") == 3