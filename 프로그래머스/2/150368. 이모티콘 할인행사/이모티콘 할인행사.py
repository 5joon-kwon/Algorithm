def solution(users, emoticons):
    rates = [10, 20, 30, 40]
    best_plus, best_sale = 0, 0
    m = len(emoticons)
    disc = [0] * m

    def evaluate():
        nonlocal best_plus, best_sale
        plus, sale = 0, 0

        for urate, money in users:
            tot = 0
            for price, r in zip(emoticons, disc):
                if r >= urate:
                    tot += price * (100 - r) // 100
                if tot >= money:
                    plus += 1
                    tot = 0
                    break
            sale += tot
        if (plus > best_plus) or (plus == best_plus and sale > best_sale):
            best_plus, best_sale = plus, sale

    def dfs(depth):
        if depth == m:
            evaluate()
            return

        for r in rates:
            disc[depth] = r
            dfs(depth + 1)
        disc[depth] = 0

    dfs(0)
    
    return [best_plus, best_sale]