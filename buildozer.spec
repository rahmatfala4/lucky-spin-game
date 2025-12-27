[app]
title = Lucky Spin Reward
package.name = luckyspin
package.domain = com.albashira.reward
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Persyaratan Library
requirements = python3,flet,requests,sqlite3

# Orientasi Layar
orientation = portrait

# Izin Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE, VIBRATE

# Pengaturan API Android
android.api = 31
android.minapi = 21

# Metadata AdMob (Wajib ada agar tidak crash)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-4097764438032261

[buildozer]
log_level = 2
warn_on_root = 1
