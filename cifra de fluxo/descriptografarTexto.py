def cifra_fluxo_binaria(msg_bin, chave_bin):
    return ''.join(str(int(m_bit) ^ int(k_bit)) for m_bit, k_bit in zip(msg_bin, chave_bin))

def binario_para_string(binario):
    chars = [chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8)]
    return ''.join(chars)

def descriptografar_binario(mensagem_criptografada, chave_bin):
    mensagem_bin = cifra_fluxo_binaria(mensagem_criptografada, chave_bin)
    mensagem_descriptografada = binario_para_string(mensagem_bin)
    return mensagem_descriptografada

def main():
    mensagem_criptografada = input("Digite a mensagem criptografada (em binário): ").strip()
    chave_bin = input("Digite a chave (em binário): ").strip()
    
    mensagem_descriptografada = descriptografar_binario(mensagem_criptografada, chave_bin)
    
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")

if __name__ == "__main__":
    main()