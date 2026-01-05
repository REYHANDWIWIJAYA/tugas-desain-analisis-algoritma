# ============================================
# 0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING
# Kasus: Optimasi Muatan Carrier Pendakian
# ============================================

class KnapsackDP:
    def __init__(self, items, capacity):
        """
        items    : list of tuple (nama, berat, nilai)
        capacity : kapasitas carrier (kg)
        """
        self.items = items
        self.capacity = int(capacity * 10)  # konversi ke satuan 0.1 kg
        self.n = len(items)
        self.dp = None
        self.selected_items = []

    def solve(self):
        # Step 1: Inisialisasi tabel DP
        # dp[i][w] = nilai maksimum dengan i item dan kapasitas w
        self.dp = [[0 for _ in range(self.capacity + 1)]
                   for _ in range(self.n + 1)]

        # Step 2: Isi tabel DP (bottom-up)
        for i in range(1, self.n + 1):
            name, weight, value = self.items[i - 1]
            weight_int = int(weight * 10)

            for w in range(self.capacity + 1):
                # Opsi 1: Tidak ambil item
                exclude = self.dp[i - 1][w]

                # Opsi 2: Ambil item (jika muat)
                if weight_int <= w:
                    include = self.dp[i - 1][w - weight_int] + value
                    self.dp[i][w] = max(include, exclude)
                else:
                    self.dp[i][w] = exclude

        # Step 3: Backtracking (menentukan item terpilih)
        self.selected_items = []
        w = self.capacity

        for i in range(self.n, 0, -1):
            if self.dp[i][w] != self.dp[i - 1][w]:
                self.selected_items.append(self.items[i - 1])
                w -= int(self.items[i - 1][1] * 10)

        self.selected_items.reverse()

        return {
            "max_value": self.dp[self.n][self.capacity],
            "selected_items": self.selected_items,
            "remaining_capacity": w / 10
        }

    def print_solution(self):
        result = self.solve()

        print("=" * 60)
        print("HASIL OPTIMASI 0/1 KNAPSACK (CARRIER)")
        print("=" * 60)
        print(f"Kapasitas Carrier : {self.capacity / 10} kg")
        print(f"Nilai Maksimum   : {result['max_value']}")
        print("\nItem Terpilih:")
        print("-" * 60)
        print(f"{'No':<5}{'Nama Item':<20}{'Berat (kg)':<15}{'Nilai'}")
        print("-" * 60)

        total_weight = 0
        for i, (name, weight, value) in enumerate(result["selected_items"], 1):
            print(f"{i:<5}{name:<20}{weight:<15}{value}")
            total_weight += weight

        print("-" * 60)
        print(f"Total Berat      : {total_weight:.1f} kg")
        print(f"Sisa Kapasitas   : {result['remaining_capacity']:.1f} kg")
        print("=" * 60)


def main():
    # Data barang carrier (nama, berat, nilai)
    items = [
        ("Tenda", 4.0, 10),
        ("Sleeping Bag", 1.5, 9),
        ("Jaket Gunung", 1.0, 8),
        ("Matras", 1.0, 7),
        ("Kompor Portable", 1.0, 7),
        ("Headlamp", 0.3, 6),
        ("Kotak P3K", 0.7, 8),
        ("Jas Hujan", 0.8, 6),
        ("Peralatan Makan", 0.7, 5),
        ("Makanan Instan", 3.0, 9)
    ]

    capacity = 8  # kg

    knapsack = KnapsackDP(items, capacity)
    knapsack.print_solution()


if __name__ == "__main__":
    main()
