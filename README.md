# albert-heijn-bonuskaart-generator

> Today I decided to try and reverse engineer the algorithm behind the Albert Heijn Bonuskaart.

## In Short

Albert Heijn Bonuskaart numbers follow the GTIN-13 format, starting with a fixed `26` prefix, followed by 11 digits that pass a checksum validation.

> `26xxxxx xxxxxc`  
> `26` = static prefix  
> `xxxxx` = semi-logical prefix range (partially reverse engineered)  
> `xxxxx` = 5 random digits  
> `c` = checksum digit  

This project generates fully valid Bonuskaart numbers using known valid prefix ranges and proper checksum calculation.


## Info
If you want to make sure for yourself that the codes are valid, go to https://www.ah.nl/klantenkaarten/bonuskaart and make an account. Then edit your card number for each card you want to validate. No rate limits  seem to be in place for this, just make sure to not use a VPN

## Disclaimer
For educational purposes only
