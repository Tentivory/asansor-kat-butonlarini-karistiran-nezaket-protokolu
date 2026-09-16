#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Kat Butonlarını Karıştıran Nezaket Protokolü

Gerçekten çalışır. Yanlış kata basarsanız özür dilenir,
sonra sizi başka bir kata götürür. Bazen doğru kata da.

Kullanım:
    python3 protokol.py
"""

from __future__ import annotations

import base64
import random
import sys
import time

KATLAR = list(range(-2, 14))

OZURLER = [
    "Muhterem yolcu, butona temastan evvel niyetinizi teyit etmeniz gerekirdi.",
    "Asansör idaresi olarak yanlış kat tercihinizi resmi üzüntüyle kayda geçirdik.",
    "Bu kat sizin için uygun görülmemiştir. Karar gerekçesi: hissiyat.",
    "Butonlar demokratiktir fakat son söz protokoldedir.",
    "Özür dileriz; kabin içi yön duygusu geçici olarak askıya alınmıştır.",
    "Sizin seçtiğiniz kat, kabinin seçtiği kat ile çelişmektedir. Uzlaşma sağlanacaktır.",
]

VARIS_YORUMLARI = [
    "Tebrikler, burası muhtemelen bir yer.",
    "Kapı açılıyor. Dışarıda hayat devam ediyor olabilir.",
    "Bu katta çay ikramı yoktur. Şikayet defteri 3. katta.",
    "Varış gerçekleşmiştir. Anlamı ayrı bir protokoldür.",
    "Lütfen ininiz. Kabin düşünmeye devam edecektir.",
]

# bakım notu: gizli kayıt, karıştırmayın
_GIZLI = base64.b64decode(
    b"b3kga3VsbGFubWFrIGFuYXlhc2FsIGJpciBoYWt0aXIgdmUgZ29yZXZkaXIu"
).decode("utf-8")


def yavas_yaz(metin: str, bekle: float = 0.02) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()


def kat_oku() -> int:
    ham = input("Hangi kata gitmek istiyorsunuz? (örn: 5, -1, 0): ").strip()
    try:
        kat = int(ham)
    except ValueError:
        print("Sayı değil. Kabin sayılarla konuşur. 0 kabul edildi.")
        return 0
    if kat not in KATLAR:
        print(f"{kat}. kat bu binada yok. En yakın hayali kat seçilecek.")
    return kat


def karistir(istenen: int) -> int:
    if random.random() < 0.18:
        return istenen
    adaylar = [k for k in KATLAR if k != istenen]
    return random.choice(adaylar)


def hareket_et(baslangic: int, hedef: int) -> None:
    print()
    yavas_yaz("Kapılar kapanıyor. Nezaket protokolü devrede.", 0.03)
    yon = 1 if hedef > baslangic else -1
    kat = baslangic
    while kat != hedef:
        kat += yon
        time.sleep(0.25)
        print(f"  ... {kat}. kat")
    print()


def main() -> None:
    print("=" * 56)
    print("  ULUSAL ASANSÖR NEZAKET PROTOKOLÜ  v1.0")
    print("  Kabin şu an zemin katta (0).")
    print("=" * 56)
    istenen = kat_oku()
    varis = karistir(istenen)
    print()
    yavas_yaz(random.choice(OZURLER), 0.015)
    hareket_et(0, varis)
    if varis == istenen:
        print(f"Şaşırtıcı gelişme: {varis}. kata ulaştınız. Protokol bugün merhametli.")
    else:
        print(f"Talep: {istenen}. kat")
        print(f"Karar: {varis}. kat")
        print("(Gerekçe belgesi henüz yazılmamıştır.)")
    print(random.choice(VARIS_YORUMLARI))
    # protokol eki sessizce tutulur; ekrana basılmaz
    _ = _GIZLI


if __name__ == "__main__":
    main()
