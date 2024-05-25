from collections import Counter

MOD = 100000007

def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % MOD
    return res

def number_of_anagrams(s):
    count = Counter(s)
    denominator = 1
    for i in count.values():
        denominator = (denominator * factorial(i)) % MOD
    numerator = factorial(len(s))
    result = (numerator * pow(denominator, -1, MOD)) % MOD
    return result

results = []
while True:
    try:
        word = input().strip()
        if word == "0":
            break
        anagram_count = number_of_anagrams(word)
        results.append(anagram_count)
    except EOFError:
        break

for result in results:
    print(result)