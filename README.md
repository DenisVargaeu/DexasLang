

### 📄 `README.md` (vysvetľuje ako nastaviť otváranie `.dex` súborov)


# DexasLang 🐍

**DexasLang** je jednoduchý vlastný programovací jazyk **vytvorený v jazyku Python** a zabalený do spustiteľného `.exe` súboru. Tento jazyk umožňuje učiť sa základy programovania bez inštalácie Pythonu.

---

## 🛠️ Spustenie cez `.dex` súbor (odporúčané)

Aby si mohol spúšťať `.dex` súbory **dvojklikom**, stačí ich raz prepojiť s interpretom `dexaslang.exe`.

### 🔄 Postup:
1. Otvor na  súbor `program.dex`
2. windows ta vizve na  **„Viberte ako spustit apliakciu “** kliknite na  **„viac aplikacii“**
3. Zaškrtni ak nieje **„Vždy používať túto aplikáciu na otváranie .dex súborov“**
4. Zoskroluj uplne nadol  **„Vybrat inu aplikaciu“ / „Look for another app“**
5. Vyber `dexaslang.exe` z rozbaleného ZIP priečinka
7. Potvrď tlačidlom **OK**

Hotovo! Teraz môžeš dvojklikom spúšťať `.dex` programy cez tvoj interpreter 🚀



## 📄 Obsah ZIP balíka

```

dexaslang/
├── /_internal          ← dll subori pre interpreta (nemazat !!)
├── dexaslang.exe       ← Interpreter (vytvorený v Pythone)
├── program.dex         ← Ukážkový skript
├── README.md           ← Tento návod

````



## ✨ Podporované príkazy v DexasLang

| Kategória   | Príkazy |
|-------------|--------|
| Premenné    | `SET`, `INPUT` |
| Výpis       | `PRINT`, `ADD` |
| Podmienky   | `IF`, `ELSEIF`, `ELSE`, `END` |
| Cyklus      | `WHILE`, `END` |
| Funkcie     | `DEF`, `CALL`, `END` |



## 🧾 Ukážka `.dex` programu

```txt
INPUT meno
PRINT meno
SET x 1
WHILE x <= 3
  PRINT x
  SET x x+1
END
DEF pozdrav
  PRINT meno
END
CALL pozdrav
````

---

## 🧠 O autorovi

Vytvoril: **Denis Varga**
YouTube: [DexasStudio](https://youtube.com/@DexasStudio)
Web: [https://denisvarga.eu](https://denisvarga.eu)

