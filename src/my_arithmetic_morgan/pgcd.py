
def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers."""
    if a == 0 and b == 0:
        raise ValueError("Le PGCD de 0 et 0 n'est pas défini.")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
