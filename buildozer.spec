[app]
title = Camera App
package.name = cameraapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Essentiële bibliotheken
requirements = python3,kivy

# Scherminstellingen
orientation = portrait
fullscreen = 1

# Android permissies (Cruciaal voor camera en opslag)
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31

# (Optioneel) Icoon en splash screen
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

[buildozer]
log_level = 2
warn_on_root = 1
