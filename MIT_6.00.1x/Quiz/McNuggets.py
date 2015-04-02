def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n == 0:
        return True
    elif n < 6 or n == 17 or n == 16 or n == 28:
        return False
    elif McNuggets(n - 20) or McNuggets(n - 9) or McNuggets(n - 6):
        return True 