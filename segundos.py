def main():
    segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
    dias = segundos // 86400
    segundosRestantes = segundos % 86400
    horas = segundosRestantes // 3600
    segundosRestantes1 = segundos % 3600
    minutos = segundosRestantes1 // 60
    segundosRestantesFinal = segundosRestantes1 % 60   
    print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundosRestantesFinal,"segundos.")
main()