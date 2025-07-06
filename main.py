from os import system, name
from typing import List
from utils.BinarySearch import binary_search
from utils.LinearSearch import linear_search

# Enum-like for status
STATUS = ["Belum", "Dalam Perjalanan", "Selesai"]

def clear_console():
    system("cls" if name == "nt" else "clear")

def menu() -> int:
    print("=== Menu Pengiriman ===")
    print("1. Tambah data pengiriman")
    print("2. Cari ID pengiriman")
    print("3. Tampilkan data pengiriman berdasarkan prioritas")
    print("4. Perbarui status pengiriman")
    print("5. Tampilkan semua data pengiriman")
    print("6. Keluar")
    try:
        return int(input("Masukkan pilihan: "))
    except ValueError:
        return -1

def tambah_data(data: List[List], id_list: List[int], counter: int) -> int:
    try:
        prioritas = int(input("Masukkan prioritas: "))
        waktu = int(input("Masukkan waktu estimasi (menit): "))

        print("Status:")
        for i, s in enumerate(STATUS, 1):
            print(f"{i}. {s}")
        status_idx = int(input("Masukkan status pengiriman: ")) - 1

        if not (0 <= status_idx < len(STATUS)):
            print("Status tidak valid!\n")
            return counter

        id_pengiriman = counter
        id_list.append(id_pengiriman)
        data.append([id_pengiriman, prioritas, waktu, STATUS[status_idx]])
        print(f"ID pengiriman {id_pengiriman} berhasil ditambahkan\n")
        return counter + 1
    except ValueError:
        print("Input tidak valid!\n")
        return counter

def cari_id(data: List[List], id_list: List[int]):
    try:
        id_list.sort()
        data.sort(key=lambda x: x[0])
        id_input = int(input("Masukkan ID pengiriman: "))
        index = binary_search(id_list, id_input)

        if index == -1:
            print("ID pengiriman tidak ditemukan\n")
        else:
            i, p, w, s = data[index]
            print(f"Data ditemukan: \nID: {i}, Prioritas: {p}, Waktu: {w}, Status: {s}\n")
    except ValueError:
        print("Input tidak valid!\n")

def tampilkan_by_prioritas(data: List[List]):
    try:
        prioritas = int(input("Masukkan prioritas: "))
        hasil = [f"ID: {i}, Prioritas: {p}, Waktu: {w}, Status: {s}"
                 for i, p, w, s in data if p == prioritas]

        if not hasil:
            print("Tidak ada pengiriman dengan prioritas tersebut\n")
        else:
            print("Daftar Pengiriman:")
            print("\n".join(hasil), "\n")
    except ValueError:
        print("Input tidak valid!\n")

def perbarui_status(data: List[List], id_list: List[int]):
    try:
        id_input = int(input("Masukkan ID pengiriman: "))

        # Sort sinkron antara id_list dan data
        combined = sorted(zip(id_list, data), key=lambda x: x[0])
        sorted_ids, sorted_data = zip(*combined)

        index = binary_search(sorted_ids, id_input)

        if index == -1:
            print("ID pengiriman tidak ditemukan\n")
            return

        current_status = sorted_data[index][3]
        next_status = STATUS[(STATUS.index(current_status) + 1) % len(STATUS)]
        sorted_data[index][3] = next_status

        print(f"Status diperbarui menjadi: {next_status}\n")

        # Update kembali ke data asli
        for i in range(len(data)):
            if data[i][0] == id_input:
                data[i][3] = next_status
                break

    except ValueError:
        print("Input tidak valid!\n")


def tampilkan_semua(data: List[List]):
    if not data:
        print("Belum ada data pengiriman\n")
        return

    print("Daftar Pengiriman:")
    for i, p, w, s in data:
        print(f"ID: {i}, Prioritas: {p}, Waktu: {w}, Status: {s}")
    print()

def main():
    clear_console()
    count = 1000
    data_pengiriman = [
        [1023, 2, 30, "Belum"],
        [2044, 1, 25, "Dalam Perjalanan"],
        [1422, 3, 45, "Belum"],
        [1987, 1, 20, "Selesai"],
        [1566, 2, 40, "Dalam Perjalanan"]
    ]
    data_id = [row[0] for row in data_pengiriman]

    while True:
        pilihan = menu()
        if pilihan == 1:
            count = tambah_data(data_pengiriman, data_id, count)
        elif pilihan == 2:
            cari_id(data_pengiriman, data_id)
        elif pilihan == 3:
            tampilkan_by_prioritas(data_pengiriman)
        elif pilihan == 4:
            perbarui_status(data_pengiriman, data_id)
        elif pilihan == 5:
            tampilkan_semua(data_pengiriman)
        elif pilihan == 6:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
