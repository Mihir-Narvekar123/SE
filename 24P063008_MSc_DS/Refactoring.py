import math
from typing import List

class PrimeGenerator:
    def generate_primes(self, max_value: int) -> List[int]:
        """
        Generates all prime numbers up to max_value.
        :param max_value: Upper limit to generate primes.
        :return: List of prime numbers.
        """

        # Refactor #1: Improved boundary check (no primes < 2)
        if max_value < 2:
            return []

        # Refactor #2: Renamed variables for clarity
        size = max_value + 1
        is_prime = [True] * size

        # Refactor #3: 0 and 1 are not prime
        is_prime[0] = is_prime[1] = False

        # Refactor #4: Apply sieve logic in helper method
        self._apply_sieve(is_prime)

        # Refactor #5: Collect primes into a list
        return self._collect_primes(is_prime)

    def _apply_sieve(self, is_prime: List[bool]):
        """
        Marks non-prime numbers in the is_prime list using the Sieve of Eratosthenes.
        """
        limit = int(math.sqrt(len(is_prime))) + 1

        for i in range(2, limit):
            if is_prime[i]:
                # Refactor #6: Start crossing out from i*i
                for j in range(i * i, len(is_prime), i):
                    is_prime[j] = False

    def _collect_primes(self, is_prime: List[bool]) -> List[int]:
        """
        Extracts prime numbers from the boolean list.
        """
        return [i for i, prime in enumerate(is_prime) if prime]
if __name__ == "__main__":
    pg = PrimeGenerator()
    primes = pg.generate_primes(50)
    print("Primes up to 50:", primes)
