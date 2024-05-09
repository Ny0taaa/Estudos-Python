def recomendar_plano(consumo_medio):

    if consumo_medio <= 10:
        return "Plano Essencial Fibra - 50Mbps"

    elif consumo_medio <= 20:
        return "Plano Prata Fibra - 100Mbps"

    else:
        return "Plano Premium Fibra - 300Mbps"
    
consumo = float(input())
print(recomendar_plano(consumo))