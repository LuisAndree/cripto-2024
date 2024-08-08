import random

def string_para_binario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)

def gerar_chave_binaria(tamanho):
    return ''.join(random.choice('01') for _ in range(tamanho))

def cifra_fluxo_binaria(msg_bin, chave_bin):
    return ''.join(str(int(m_bit) ^ int(k_bit)) for m_bit, k_bit in zip(msg_bin, chave_bin))

def criptografar_binario(mensagem):
    mensagem_bin = string_para_binario(mensagem)
    chave_bin = gerar_chave_binaria(len(mensagem_bin))
    
    mensagem_criptografada = cifra_fluxo_binaria(mensagem_bin, chave_bin)
    return mensagem_criptografada, chave_bin

def main():
    mensagem = input("Digite a mensagem para criptografar: ").strip()
    
    mensagem_criptografada, chave_bin = criptografar_binario(mensagem)
    
    print(f"Mensagem em binário: {string_para_binario(mensagem)}")
    print(f"Chave gerada: {chave_bin}")
    print(f"Mensagem criptografada: {mensagem_criptografada}")

if __name__ == "__main__":
    main()