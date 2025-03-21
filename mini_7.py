# Sistem Quiz Interaktif
pertanyaan_quiz = {
    "Apa ibu kota Perancis?": "Paris",
    "Berapa 2 + 2?": "4",
    "Warna apa yang Anda dapat jika Anda mencampur merah dan putih?": "Pink"
}

def jalankan_quiz(pertanyaan_quiz):
    skor = 0
    for soal, jawaban in pertanyaan_quiz.items():
        jawaban_pengguna = input(soal + " ")
        if jawaban_pengguna.lower() == jawaban.lower():
            print("Benar!")
            skor += 1
        else:
            print("Salah!")
    print(f"Skor akhir Anda adalah {skor}/{len(pertanyaan_quiz)}.")

if __name__ == "__main__":
    jalankan_quiz(pertanyaan_quiz)