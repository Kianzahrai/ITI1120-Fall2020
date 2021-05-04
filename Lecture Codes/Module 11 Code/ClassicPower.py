def ClassicPower(nb, p) : # nb**p
	
    result = 1

    for i in range (p, 0, -1):
        result = nb * result
        print(result, end = " ")

    print()
    return result

