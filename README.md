# albert-heijn-bonuskaart-generator

> Today I decided to reverse engineer the algorithm behind the Albert Heijn Bonuskaart.

---

## In short

The Bonuskaart uses GTIN-13–based barcodes with a fixed prefix of `26`, followed by 11 digits that complete a valid checksum sequence. This project generates fully valid Bonuskaart numbers based on those rules.

## Info
PROOF OF CONCEPT. All generated codes wil be considered valid by the regex on their website, but not all codes will be accepted by their back-end. I do know of some ways to get actual correct codes, but this will be implemented later.

## Disclaimer
