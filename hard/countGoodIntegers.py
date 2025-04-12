class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i

        def count_arrangements(freq):
            total = fact[n]
            for count in freq:
                total //= fact[count]
            return total

        def count_with_leading_zero(freq):
            if freq[0] == 0:
                return 0
            total = fact[n-1]
            total //= fact[freq[0] - 1]
            for d in range(1, 10):
                total //= fact[freq[d]]
            return total

        def generate_freq(digit, remain, current):
            if digit == 9:
                current[9] = remain
                yield tuple(current)
                return
            for count in range(remain + 1):
                current[digit] = count
                yield from generate_freq(digit + 1, remain - count, current)
        
        total_good = 0 
        
        for freq in generate_freq(0, n, [0]*10):
            if freq[0] == n:
                continue

            odd_count = sum(1 for cnt in freq if cnt % 2 == 1)
            if odd_count > 1:
                continue
            if n % 2 == 1 and odd_count != 1:
                continue

            half = [cnt // 2 for cnt in freq]
            L = n // 2  # length of the left half

            middle_digit = None
            if n % 2 == 1:
                for d in range(10):
                    if freq[d] % 2 == 1:
                        middle_digit = d
                        break

            half_list = []
            for d in range(10):
                half_list.extend([d] * half[d])
            
            found_valid_palindrome = False
            seen = set()
            for perm in itertools.permutations(half_list):
                if perm in seen:
                    continue
                seen.add(perm)
                if perm and perm[0] == 0:
                    continue

                if n % 2 == 0:
                    full_digits = list(perm) + list(perm)[::-1]
                else:
                    full_digits = list(perm) + [middle_digit] + list(perm)[::-1]

                num = 0
                for d in full_digits:
                    num = num * 10 + d
                if num % k == 0:
                    found_valid_palindrome = True
                    break
            if not found_valid_palindrome:
                continue  

            valid_count = count_arrangements(freq) - count_with_leading_zero(freq)
            total_good += valid_count

        return total_good
