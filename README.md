# albert-heijn-bonuskaart-generator

> Today I decided to try and reverse engineer the algorithm behind the Albert Heijn Bonuskaart.

---

## In short

The Bonuskaart uses GTIN-13–based barcodes with a fixed prefix of `26`, followed by 11 digits that complete a valid checksum sequence. This project generates fully valid Bonuskaart numbers based on those rules.

## Info
If you want to make sure for yourself that the codes are valid, go to https://www.ah.nl/klantenkaarten/bonuskaart and make an account. Then edit your card number for each card you want to validate. No rate limits  seem to be in place for this, just make sure to not use a VPN

## Disclaimer
