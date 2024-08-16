def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Não existe inverso modular')
    return x % m

def gerar_chaves_rsa():
    p = 61 
    q = 53  
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  
    d = modinv(e, phi)
    return ((e, n), (d, n))

def cifrar_rsa(mensagem, chave_publica):
    e, n = chave_publica
    mensagem_cifrada = [pow(ord(char), e, n) for char in mensagem]
    return mensagem_cifrada

def decifrar_rsa(mensagem_cifrada, chave_privada):
    d, n = chave_privada
    mensagem_decifrada = ''.join([chr(pow(char, d, n)) for char in mensagem_cifrada])
    return mensagem_decifrada

mensagem = input("Digite a mensagem: ")
chave_publica, chave_privada = gerar_chaves_rsa()

mensagem_cifrada = cifrar_rsa(mensagem, chave_publica)
print(f"Mensagem cifrada: {mensagem_cifrada}")

mensagem_decifrada = decifrar_rsa(mensagem_cifrada, chave_privada)
print(f"Mensagem decifrada: {mensagem_decifrada}")
