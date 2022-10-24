# def mnozenie(a, b):
#     try:
#         return a * b
#     except TypeError:
#         print("Błędne dane lub ich brak")

# print(mnozenie(5, 5))
# print(mnozenie(5, 0))
# print(mnozenie(5, "5"))
#print(mnozenie("5", "5"))# tutaj wystąpi błąd (nie można mnożyć dwóch stringów). Patrzymy na błąd typu "TypeError:"

#inna wersja
def mnozenie(a, b):
    try:
        print("wynik działania:", a * b)
    except TypeError:
        print("Błędne dane lub ich brak")
    else:
        print("Udało się prawidłowo pomnożyć")
    finally:
        lista = []
        lista.append(a)
        lista.append(b)
        print("Elementy:", lista)

mnozenie(5, 5)
mnozenie("5", "5")

invalid_age = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]

def check_age(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except (TypeError, KeyError, ValueError, ImportError):
            print("Niepoprawne dane: {}".format(user))
    return count


def check_age2(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except TypeError:
            print("Niepoprawne dane: {}".format(user))
        except KeyError:
            print("Niepoprawne klucze: {}".format(user))
        except ValueError:
            print("Niepoprawne wiek: {}".format(user))
    return count


def check_age3(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except Exception as e:
            print("Wystąpił błąd:", e)
    return count

def check_age4(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except TypeError:
            print("Niepoprawne dane: {}".format(user))
        except KeyError:
            print("Niepoprawne klucze: {}".format(user))
        except ValueError:
            print("Niepoprawny wiek: {}".format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("{} --> {}".format(i, user))
    return count

