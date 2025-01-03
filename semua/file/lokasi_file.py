import os

tempat_file = os.environ.get("TEMPAT_FILE_JUSTIP", "./")

lokasi_file = {
    "akun": tempat_file + "akun.csv",
    "pesanan": tempat_file + "pesanan.csv",
    "progress_pesanan": tempat_file + "progress_pesanan/",
    "rating": tempat_file + "rating.csv"
}