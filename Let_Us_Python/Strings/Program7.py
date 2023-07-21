# Convert the string into :-
'LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak.'

string = 'Light travels faster than sound. This is why some people appear bright until you hear them speak.'

s = 'Light travels faster than sound. This is why some people appear bright until you hear them speak'
s1, s2 = s.split('.')
a,b,c,d,e = s1.split(' ')
s1 = a.upper() + ' ' + b + ' ' + c + ' ' + d + ' ' + e.upper() + '.'
print(s1 + s2)
