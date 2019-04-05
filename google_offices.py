print('Hello!!!')
geust = input("Guest: ")
require = ("1.Google Kazakhstan", "2.Google Paris", "3.Google SAR", "4.Google Kyrgyzstan",
           "5.Google San-Francisco", "6.Google Germany", "7.Google Moscow", "8.Google Sweeden")
print('\n'.join(require))

offices = int(input("Choose office you want in number:"))
if offices == 1:
        with open('google_kazakhstan.txt', 'a') as kazakstan:
           kazakstan.write(input('Leave your complaint here about Kazakhstan Google office, please.'))
elif offices == 2:
        with open('google_paris.txt', 'a') as paris:
           paris.write(input('Leave your complaint here about Paris Google office, please.'))
elif offices == 3:
        with open('google_sar.txt', 'a') as sar:
           sar.write(input('Leave your complaint here about SAR Google office, please.'))
elif offices == 4:
        with open('google_kyr.txt', 'a') as kyrgyzstan:
           kyrgyzstan.write(input('Leave your complaint here about Kyrgyzstan Google office, please.'))
elif offices == 5:
        with open('google_san_francisco.txt', 'a') as san_francisco:
           san_francisco.write(input('Leave your complaint here about San Francisco Google office, please.'))
elif offices == 6:
        with open('google_germany.txt', 'a') as germany:
           germany.write(input('Leave your complaint here about Germany Google office, please.'))
elif offices == 7:
        with open('google_moscow.txt', 'a') as moscow:
            moscow.write(input('Leave your complaint here about Moscow Google office, please.'))
elif offices == 8:
        with open('google_sweeden.txt', 'a') as sweeden:
           sweeden.write(input('Leave your complaint here about Sweeden Google office, please.'))
