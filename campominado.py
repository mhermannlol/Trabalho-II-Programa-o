import random
import re

tamanho = 5
minas = 3

print("Campo Minado")

def criar_tabuleiros():
    visivel = [['-' for _ in range(tamanho)] for _ in range(tamanho)]
    real = [['0' for _ in range(tamanho)] for _ in range(tamanho)]
    
    minas_colocadas = 0
    while minas_colocadas < minas:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        if real[linha][coluna] != 'M':
            real[linha][coluna] = 'M'
            minas_colocadas += 1
            
    for l in range(tamanho):
        for c in range(tamanho):
            if real[l][c] == 'M':
                continue
            
            contagem = 0
            for dl in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nl, nc = l + dl, c + dc
                    if 0 <= nl < tamanho and 0 <= nc < tamanho:
                        if real[nl][nc] == 'M':
                            contagem += 1
            real[l][c] = str(contagem)
            
    return visivel, real

def exibir_tabuleiro(tabuleiro):
    print("\n   " + " ".join(str(i) for i in range(tamanho)))
    print("  " + "-" * (tamanho * 2 + 1))
    for i in range(tamanho):
        print(f"{i} | " + " ".join(tabuleiro[i]))

def jogar():
    visivel, real = criar_tabuleiros()
    reveladas = 0
    objetivo = (tamanho * tamanho) - minas

    while True:
        exibir_tabuleiro(visivel)
        
        entrada = input("digite a linha e coluna (ex: 1 2, 1-2): ")

        numeros = re.findall(r'\d+', entrada)
        
        if len(numeros) < 2:
            print("entrada inválida")
            continue
            
        l, c = int(numeros[0]), int(numeros[1])
            
        if not (0 <= l < tamanho and 0 <= c < tamanho):
            print("Posição fora do tabuleiro. Escolha números de 0 a 4.")
            continue
            
        if visivel[l][c] != '-':
            print("Você já abriu essa posição.")
            continue
            
        if real[l][c] == 'M':
            print("Fim de jogo.")
            exibir_tabuleiro(real)
            break
        else:
            visivel[l][c] = real[l][c]
            reveladas += 1
            
            if reveladas == objetivo:
                print("Foram reveladas todas as posições sem minas.")
                exibir_tabuleiro(real)
                break

if __name__ == "__main__":
    jogar()
