x = int(input('ievadīt kvadrāta malas garumu'))
if x<=5 :
  x = input(('ievadīt kvadrāta malas garumu,kas ir lielāka par 5 cm'))
else :
  y=x*x
  x1=x+5
  y1=x1*x1
  procenti=y/y1*100
print("laukumu atšķirība procentos ir",round (procenti))