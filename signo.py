dia = input("digite o dia de se nascimento: ")
mes = input("digite o mes do seu nascimento: ")
if dia>=20 and dia<=31 and mes==3 or dia>=1 and dia<=20 and  mes==4:
   print "aries"
elif dia>=21 and dia<=30 and mes==4 or dia>=1 and dia<=20 and mes==5:
   print "touro"
elif dia>=21 and dia<=31 and mes==5 or dia>=1 and dia<=20 and mes==6:
   print "gemeos"
elif dia>=21 and dia<=30 and mes==6 or dia>=1 and dia<=21 and mes==7:
   print "cancer"
elif dia>=22 and dia<=31 and mes==7 or dia>=1 and dia<=22 and mes==8:
   print "leao"
elif dia>=22 and dia<=31 and mes==8 or dia>=1 and dia<=22 and mes==9:
   print "virgem"
elif dia>=22 and dia<=30 and mes==9 or dia>=1 and dia<=22 and mes==10:
   print "libra"
elif dia>=23 and dia <=31 and mes==10 or dia>=1 and dia<=21 and mes==11:
   print "escorpiao"
elif dia>=22 and dia<=30 and mes==11 or dia>=1 and dia<=21 and mes==12:
   print "sagitario"
elif dia>=22 and dia<=31 and mes==12 or dia>=1 and dia<=20 and mes==1:
  print "capricornio"
elif dia>=21 and dia<=31 and mes==1 or dia>=1 and dia<=18 and mes==2:
  print "aquario"
elif dia>=19 and dia<=29 and mes==2 or dia>=1 and dia<=19 and mes==3:
  print "peixes"
else:
  print "mes ou dia invalido"
