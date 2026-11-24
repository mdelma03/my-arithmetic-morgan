
def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers.

    Utilise l'algorithme d'Euclide sur les valeurs absolues des entiers
    fournis en entrée.

    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.

    Returns
    -------
    int
        Le plus grand commun diviseur positif de ``a`` et ``b``.

    Raises
    ------
    ValueError
        Si ``a`` et ``b`` sont tous les deux nuls.

    Examples
    --------
    >>> from my_arithmetic_morgan import pgcd
    >>> pgcd(48, 18)
    6
    """
    if a == 0 and b == 0:
        raise ValueError("Le PGCD de 0 et 0 n'est pas défini.")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
