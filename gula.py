def analisis_minuman(volume_total_ml, gula_total_gram, jumlah_sajian, kalori_total):
    # Konstanta
    KALORI_PER_GRAM_GULA = 4  # 1 gram gula = 4 kalori
    BATAS_GULA_HARIAN = 50    # gram
    BATAS_KALORI_HARIAN_RATA = 2000  # kalori
    
    # Perhitungan dasar
    volume_per_sajian = volume_total_ml / jumlah_sajian
    gula_per_sajian = gula_total_gram / jumlah_sajian
    kalori_per_sajian = kalori_total / jumlah_sajian
    kadar_per_100ml = (gula_total_gram / volume_total_ml) * 100
    
    # Perhitungan kalori dari gula
    kalori_dari_gula = gula_total_gram * KALORI_PER_GRAM_GULA
    kalori_dari_gula_per_sajian = kalori_dari_gula / jumlah_sajian
    persen_kalori_dari_gula = (kalori_dari_gula / kalori_total) * 100
    
    # Klasifikasi kadar gula
    if kadar_per_100ml < 5:
        kategori = "RENDAH GULA"
        deskripsi = "Minuman ini termasuk kategori rendah gula"
        rekomendasi = "Aman untuk dikonsumsi secara rutin"
    elif kadar_per_100ml < 8:
        kategori = "NORMAL"
        deskripsi = "Minuman ini memiliki kadar gula normal"
        rekomendasi = "Dapat dikonsumsi dengan wajar"
    elif kadar_per_100ml < 11:
        kategori = "TINGGI GULA"
        deskripsi = "Minuman ini memiliki kadar gula tinggi"
        rekomendasi = "Batasi konsumsi, maksimal 1 porsi per hari"
    else:
        kategori = "SANGAT TINGGI GULA"
        deskripsi = "Minuman ini memiliki kadar gula sangat tinggi"
        rekomendasi = "Sebaiknya dibatasi, konsumsi sesekali saja"
    
    # Perhitungan persentase dari batas harian
    persen_batas_gula_per_sajian = (gula_per_sajian / BATAS_GULA_HARIAN) * 100
    persen_batas_gula_total = (gula_total_gram / BATAS_GULA_HARIAN) * 100
    persen_kalori_harian_per_sajian = (kalori_per_sajian / BATAS_KALORI_HARIAN_RATA) * 100
    persen_kalori_harian_total = (kalori_total / BATAS_KALORI_HARIAN_RATA) * 100
    
    return {
        'volume_per_sajian': volume_per_sajian,
        'gula_per_sajian': gula_per_sajian,
        'kalori_per_sajian': kalori_per_sajian,
        'kadar_per_100ml': kadar_per_100ml,
        'kategori': kategori,
        'deskripsi': deskripsi,
        'rekomendasi': rekomendasi,
        'kalori_dari_gula': kalori_dari_gula,
        'kalori_dari_gula_per_sajian': kalori_dari_gula_per_sajian,
        'persen_kalori_dari_gula': persen_kalori_dari_gula,
        'persen_batas_gula_per_sajian': persen_batas_gula_per_sajian,
        'persen_batas_gula_total': persen_batas_gula_total,
        'persen_kalori_harian_per_sajian': persen_kalori_harian_per_sajian,
        'persen_kalori_harian_total': persen_kalori_harian_total
    }

def main():
    print("=== Analisis Kadar Gula dan Kalori dalam Minuman Kemasan ===")
    print("Program ini akan menganalisis kandungan gula dan kalori berdasarkan informasi kemasan")
    
    while True:
        try:
            print("\n=== INFORMASI KEMASAN ===")
            volume_total = float(input("1. Volume total kemasan (ml): "))
            jumlah_sajian = float(input("2. Jumlah sajian per kemasan: "))
            gula_total = float(input("3. Kandungan gula total (gram): "))
            kalori_total = float(input("4. Total kalori (kkal): "))
            
            if volume_total <= 0 or gula_total < 0 or jumlah_sajian <= 0 or kalori_total < 0:
                print("Error: Semua nilai harus positif dan volume/sajian harus lebih dari 0!")
                continue
            
            hasil = analisis_minuman(volume_total, gula_total, jumlah_sajian, kalori_total)
            
            print("\n=== HASIL ANALISIS KEMASAN ===")
            print(f"Volume total: {volume_total} ml")
            print(f"Jumlah sajian: {jumlah_sajian}")
            print(f"Gula total: {gula_total} gram")
            print(f"Kalori total: {kalori_total} kkal")
            
            print("\n=== ANALISIS PER SAJIAN ===")
            print(f"1. Volume per sajian: {hasil['volume_per_sajian']:.1f} ml")
            print(f"2. Gula per sajian: {hasil['gula_per_sajian']:.1f} gram")
            print(f"3. Kalori per sajian: {hasil['kalori_per_sajian']:.1f} kkal")
            print(f"4. Kadar gula per 100ml: {hasil['kadar_per_100ml']:.1f} gram")
            
            print(f"\nKATEGORI: {hasil['kategori']}")
            print(f"Deskripsi: {hasil['deskripsi']}")
            print(f"Rekomendasi: {hasil['rekomendasi']}")
            
            print("\n=== ANALISIS KALORI ===")
            print("1. Kalori dari Gula:")
            print(f"   - Per sajian: {hasil['kalori_dari_gula_per_sajian']:.1f} kkal")
            print(f"   - Total: {hasil['kalori_dari_gula']:.1f} kkal")
            print(f"   - Kontribusi gula terhadap total kalori: {hasil['persen_kalori_dari_gula']:.1f}%")
            
            print("\n2. Persentase dari Kebutuhan Harian (2000 kkal):")
            print(f"   - Per sajian: {hasil['persen_kalori_harian_per_sajian']:.1f}%")
            print(f"   - Total kemasan: {hasil['persen_kalori_harian_total']:.1f}%")
            
            print("\n=== ANALISIS GULA ===")
            print("Persentase dari Batas Gula Harian (50g):")
            print(f"1. Per sajian: {hasil['persen_batas_gula_per_sajian']:.1f}%")
            print(f"2. Total kemasan: {hasil['persen_batas_gula_total']:.1f}%")
            
            print("\n=== PANDUAN KADAR GULA ===")
            print("Klasifikasi per 100ml:")
            print("- Rendah gula: <5g/100ml")
            print("- Normal: 5-8g/100ml")
            print("- Tinggi: 8-11g/100ml")
            print("- Sangat tinggi: >11g/100ml")
            
            print("\nCATATAN PENTING:")
            print("- 1 gram gula = 4 kalori")
            print("- Batas konsumsi gula harian WHO: 50 gram")
            print("- Kebutuhan kalori harian rata-rata: 2000 kkal")
            print("- Total kalori dan gula termasuk dari sumber lain")
            
            ulang = input("\nIngin menganalisis minuman lain? (y/n): ")
            if ulang.lower() != 'y':
                print("\nTerima kasih telah menggunakan program ini!")
                break
                
        except ValueError:
            print("Error: Mohon masukkan angka yang valid!")

if __name__ == "__main__":
    main()