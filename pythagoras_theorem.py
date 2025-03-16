import math

while True:
    a = input('Enter length. ')

    try:
        int(a)

        while True:
            b = input('Enter height. ')

            try:
                int(b)

                a = int(a)
                b = int(b)
                print('a^2 + b^2 = c^2')
                print('{}^2 + {}^2 = c^2'.format(a, b))
                a = a**2
                b = b**2
                c = a + b
                c = math.sqrt(c)
                print('%.3f' % a, '+', '%.3f' % b, '= c^2\nc =', '%.3f' % c)
                print('Therefore, hypotenuse of triangle is {} units.'.format('%.3f' % c))
                raise SystemExit

            except ValueError:
                print('Invalid input. Numbers only.')
                continue

    except ValueError:
        print('Invalid input. Numbers only.')
        continue
