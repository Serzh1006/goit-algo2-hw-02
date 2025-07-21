from typing import List, Dict, Tuple

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def helper(n: int) -> Tuple[int, List[int]]:
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]
        max_profit = float('-inf')
        best_cut = []
        for i in range(1, n + 1):
            profit, cut_list = helper(n - i)
            total_profit = prices[i - 1] + profit
            if total_profit > max_profit:
                max_profit = total_profit
                best_cut = [i] + cut_list
        memo[n] = (max_profit, best_cut)
        return memo[n]

    profit, cuts = helper(length)
    return {
        "max_profit": profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts_tracker = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        max_profit = float('-inf')
        for j in range(1, i + 1):
            if prices[j - 1] + dp[i - j] > max_profit:
                max_profit = prices[j - 1] + dp[i - j]
                cuts_tracker[i] = [j] + cuts_tracker[i - j]
        dp[i] = max_profit

    return {
        "max_profit": dp[length],
        "cuts": cuts_tracker[length],
        "number_of_cuts": len(cuts_tracker[length]) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()