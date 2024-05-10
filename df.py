import random

def rnd_lotto():
    results = []

    while len(results) < 6:
        rnd_num = random.randint(1, 45)
        if rnd_num in results:
            print("results 안에 rnd_num가 있으므로, result를 제거 후 출력하겠습니다.")
        else:
            results.append(rnd_num)

    return results

print(rnd_lotto())