import sqlite3
import random

def tambah_poin(username, poin):
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    
    # Cek apakah user sudah ada
    cursor.execute("SELECT balance FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    
    if row:
        new_balance = row[0] + poin
        cursor.execute("UPDATE users SET balance=? WHERE username=?", (new_balance, username))
    else:
        cursor.execute("INSERT INTO users (username, balance) VALUES (?, ?)", (username, poin))
    
    conn.commit()
    conn.close()
    print(f"Sukses! +{poin} Poin ditambahkan ke akun {username}.")

def game_loop():
    print("--- WELCOME TO MATH REWARD ---")
    user = input("Masukkan Username: ")
    
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        hasil_benar = a + b
        
        print(f"\nBerapa hasil dari {a} + {b}?")
        jawaban = input("Jawaban (atau ketik 'exit' untuk keluar): ")
        
        if jawaban.lower() == 'exit':
            break
        
        if int(jawaban) == hasil_benar:
            tambah_poin(user, 100) # Memberi 100 koin per jawaban benar
        else:
            print("Yah, jawaban salah. Coba lagi!")

if __name__ == "__main__":
    game_loop()
