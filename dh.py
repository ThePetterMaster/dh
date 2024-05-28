import random

# Função para encontrar um gerador primitivo de um número primo
def find_primitive_root(p):
    """
    Encontra uma raiz primitiva para um número primo p.
    
    p: O número primo.
    phi: O valor de p - 1.
    factors: Um conjunto de fatores de phi.
    
    A função testa números de 2 a p-1 para encontrar uma raiz primitiva r.
    """
    if p == 2:
        return 1
    phi = p - 1
    factors = set()
    n = phi
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.add(n)
    
    for r in range(2, p):
        is_primitive = True
        for factor in factors:
            if pow(r, phi // factor, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return r
    return None

# Função para gerar chaves pública e privada
def generate_keys(p, g):
    """
    Gera uma chave privada e uma chave pública.
    
    p: O número primo.
    g: A raiz primitiva.
    private_key: A chave privada escolhida aleatoriamente entre 2 e p-2.
    public_key: A chave pública calculada como g^private_key % p.
    """
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return private_key, public_key

# Função para calcular a chave secreta compartilhada
def compute_shared_secret(their_public_key, private_key, p):
    """
    Calcula a chave secreta compartilhada.
    
    their_public_key: A chave pública da outra parte.
    private_key: A chave privada da própria parte.
    p: O número primo.
    shared_secret: A chave secreta compartilhada calculada como their_public_key^private_key % p.
    """
    shared_secret = pow(their_public_key, private_key, p)
    return shared_secret

# Exemplo de uso
if __name__ == "__main__":
    """
    Exemplo de uso:
    
    - Escolha de um número primo grande p e uma raiz primitiva g.
    - Geração de chaves pública e privada para duas partes (A e B).
    - Cálculo da chave secreta compartilhada para ambas as partes.
    - Verificação de que as chaves secretas compartilhadas são iguais.
    """
    # Escolher um número primo grande p
    p = 23  # Este é um exemplo, na prática, p deve ser um primo muito grande
    # Encontrar uma raiz primitiva g para p
    g = find_primitive_root(p)

    print(f"Número primo (p): {p}")
    print(f"Raiz primitiva (g): {g}")

    # Parte A gera suas chaves pública e privada
    private_key_a, public_key_a = generate_keys(p, g)
    print(f"Chave privada de A: {private_key_a}")
    print(f"Chave pública de A: {public_key_a}")

    # Parte B gera suas chaves pública e privada
    private_key_b, public_key_b = generate_keys(p, g)
    print(f"Chave privada de B: {private_key_b}")
    print(f"Chave pública de B: {public_key_b}")

    # Parte A calcula a chave secreta compartilhada
    shared_secret_a = compute_shared_secret(public_key_b, private_key_a, p)
    print(f"Chave secreta compartilhada calculada por A: {shared_secret_a}")

    # Parte B calcula a chave secreta compartilhada
    shared_secret_b = compute_shared_secret(public_key_a, private_key_b, p)
    print(f"Chave secreta compartilhada calculada por B: {shared_secret_b}")

    # As chaves secretas compartilhadas devem ser iguais
    assert shared_secret_a == shared_secret_b, "As chaves secretas compartilhadas não coincidem!"
    print("A chave secreta compartilhada é a mesma para ambas as partes.")
