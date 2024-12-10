class RatingPekerja:
    def __init__(self):
        self.rating = {}  # Menyimpan rating untuk masing-masing layanan

    def proses_rating(self, layanan):
        # Setelah pemesanan, meminta rating untuk layanan yang dipilih
        print("\n--- Berikan Rating untuk Pekerja ---")
        while True:
            try:
                rating = int(input(f"Berikan rating untuk layanan '{layanan}' (1-5): "))
                if 1 <= rating <= 5:
                    self.rating[layanan] = rating
                    print(f"Terima kasih! Anda memberi rating {rating} untuk layanan '{layanan}'.")
                    break
                else:
                    print("Rating harus antara 1 dan 5. Silakan coba lagi.")
            except ValueError:
                print("Masukkan angka yang valid.")

    def tampilkan_rating(self):
        # Menampilkan rating yang sudah diberikan
        print("\n--- Daftar Rating Layanan ---")
        for layanan, rating in self.rating.items():
            print(f"Layanan '{layanan}': {rating} bintang")