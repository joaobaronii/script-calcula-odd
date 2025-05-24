from scipy.stats import poisson
import math


def calcula_prob(media, ocorrencia, mais_menos):
    match mais_menos:
        case 1:
            prob = 0
            for i in range(math.ceil(ocorrencia)):
                prob += poisson.pmf(i, media)
            return 1 - prob
        case 2:
            prob = 0
            for i in range(math.ceil(ocorrencia)):
                prob += poisson.pmf(i, media)
            return prob
        case 3:
            return poisson.pmf(ocorrencia, media)


def calcula_odd(prob):
    return 1 / prob


def calcula_margem_casa(odd_justa, odd_casa):
    margem = (odd_justa - odd_casa) / odd_justa
    return margem * 100


if __name__ == "__main__":
    media = float(input("Digite a média do evento por partida: "))
    ocorrencia = float(input("Digite o número de ocorrências para odd bater: "))
    
    while True:
        print(
            f"1- para mais de {ocorrencia} \n2- para menos de {ocorrencia} \n3- para exatamente {ocorrencia}"
        )
        mais_menos = int(input("Digite a opção desejada: "))
        if mais_menos in [1, 2, 3]:
            probabilidade = calcula_prob(media, ocorrencia, mais_menos)
            break
        else:
            print("Opção inválida. Tente novamente.")

    print(f"\nA probabilidade de ocorrer é {probabilidade * 100:.2f}%")
    
    odd = calcula_odd(probabilidade)
    
    print(f"A odd justa, sem margem de lucro, é de {odd:.2f}")
    
    odd_casa = float(input("Digite a odd da casa: "))
    margem = calcula_margem_casa(odd, odd_casa)
    
    print(f"A margem de lucro da casa nessa aposta é de {margem:.2f}%")
