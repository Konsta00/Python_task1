try:
    num = int(input("Syötä kokonaisluku: "))
    
    if num <= 1:
        print(num, "ei ole alkuluku.")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, "on alkuluku.")
        else:
            print(num, "ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte. Syötä kokonaisluku.")