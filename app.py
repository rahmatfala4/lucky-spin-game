import flet as ft
import sqlite3
import random
import requests
import time

# --- DATA ADS & BOT ---
AD_UNIT_ID = "ca-app-pub-4097764438032261/2278791277"
TOKEN = "8246991089:AAEtMJjz-5C5InI8HYAItHEESw7DkR0o4Kc"
CHAT_ID = "8389633075"

def get_balance(username):
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def add_points(username, points):
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance=balance+? WHERE username=?", (points, username))
    conn.commit()
    conn.close()

def main(page: ft.Page):
    page.title = "Lucky Spin Reward"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    user_now = "Player1"

    txt_saldo = ft.Text(f"Rp {get_balance(user_now)}", size=35, color="green", weight="bold")
    status_text = ft.Text("Tonton Video untuk Spin!", size=16)

    def kirim_notif(pesan):
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": pesan})

    def jalankan_spin():
        # Logika Spin sesudah iklan
        hadiah = random.choice([50, 100, 200, 500, 1000])
        add_points(user_now, hadiah)
        txt_saldo.value = f"Rp {get_balance(user_now)}"
        status_text.value = f"🎉 Selamat! Dapat Rp {hadiah}"
        page.update()

    def play_rewarded_ad(e):
        # Simulasi pemanggilan iklan Reward ca-app-pub-4097764438032261/2278791277
        status_text.value = "Memuat Video Iklan..."
        page.update()
        time.sleep(2) # Simulasi loading iklan
        
        # Di APK asli, fungsi ini dipicu oleh SDK AdMob 'onUserEarnedReward'
        status_text.value = "Iklan Selesai! Memutar roda..."
        page.update()
        time.sleep(1)
        jalankan_spin()

    page.add(
        ft.Text("BERANDA REWARD", size=24, weight="bold"),
        ft.Card(ft.Container(content=txt_saldo, padding=20)),
        ft.Icon(name=ft.icons.RENEW, size=100, color="orange"),
        status_text,
        ft.ElevatedButton("SPIN (NONTON IKLAN)", on_click=play_rewarded_ad, bgcolor="orange", color="white"),
        ft.TextButton("Tarik Saldo", on_click=lambda _: kirim_notif(f"WD Request dari {user_now}"))
    )

ft.app(target=main)
