def ksa(chave):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + chave[i % len(chave)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prga(s, mensagem_len):
    i = j = 0
    keystream = []
    for _ in range(mensagem_len):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        keystream.append(s[(s[i] + s[j]) % 256])
    return keystream

def rc4(mensagem, chave):
    chave_bytes = [ord(c) for c in chave]
    s = ksa(chave_bytes)
    keystream = prga(s, len(mensagem))
    mensagem_bytes = [ord(c) for c in mensagem]
    cifrado = ''.join(chr(m ^ k) for m, k in zip(mensagem_bytes, keystream))
    return cifrado

mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave: ")

mensagem_cifrada = rc4(mensagem, chave)
print(f"Mensagem cifrada: {mensagem_cifrada}")

mensagem_decifrada = rc4(mensagem_cifrada, chave)
print(f"Mensagem decifrada: {mensagem_decifrada}")
