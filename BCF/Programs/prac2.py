class DiffieHellman:
    def __init__(self, P, G, private_key):
        self.P = P          # Prime number
        self.G = G          # Primitive root
        self.private_key = private_key
        self.public_key = pow(G, private_key, P)

    def generate_shared_key(self, other_public_key):
        # Shared secret key = (other_public_key ^ private_key) mod P
        return pow(other_public_key, self.private_key, self.P)


if __name__ == "__main__":
    # Public values (agreed upon by Alice & Bob)
    P = 23
    G = 9

    # Alice and Bob choose private keys
    alice = DiffieHellman(P, G, private_key=4)
    bob = DiffieHellman(P, G, private_key=3)

    print(f"Alice's Public Key: {alice.public_key}")
    print(f"Bob's Public Key: {bob.public_key}")

    # Generate shared secret keys
    alice_secret = alice.generate_shared_key(bob.public_key)
    bob_secret = bob.generate_shared_key(alice.public_key)

    print(f"Secret Key for Alice: {alice_secret}")
    print(f"Secret Key for Bob: {bob_secret}")
