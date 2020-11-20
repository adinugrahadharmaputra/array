arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    arrBerat.sort()
    global bMin, bMax
    bMax += arrBerat[-1]
    bMin += arrBerat[0]
    
    # Definisikan Proses Mencari Berat Maximum Dan Minimum


def rerata(arrBerat):
    total = 0
    for i in arrBerat:
        total += i
    # Definisikan Proses Mencari Rerata Dari Total Berat
    rerata = total/len(arrBerat)
    return rerata
    # Return Hasil Rerata


print('Masukan banyak data berat balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukan berat balita ke-{i+1} :', end=' ')
    b = float(input())
    berat = round(b,3)

    # Inisialisasi Input Data Berat
    arrBerat.append(berat)

    # Masukkan Data Berat Ke Array (arrBerat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print('Berat balita minimum : {:.2f} kg'.format(bMin), '\nBerat balita maksimum : {:.2f} kg'.format(bMax), '\nRerata berat balita : {:.2f} kg'.format(rerata(arrBerat)))