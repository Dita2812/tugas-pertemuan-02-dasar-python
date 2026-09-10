nama = input("Nama: ")
nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (
    nilai_tugas *0.20
    + nilai_uts * 0.35
    + nilai_uas * 0.45
)

print(f"Nama: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")