#importes de modulos matematicos
import math
import cmath

for cpx in [3j, 1.5+1j, -2-2j]:
	plr = cmath.polar(cpx)
	print("Complexo: ", cpx)
	print("Forma polar: ", plr, "em radianos")
	print("Amplitude: ", abs(cpx))
	print("Angulo: ", math.degrees(plr[1]), "em graus")

