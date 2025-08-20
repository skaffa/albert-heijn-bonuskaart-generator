> [!Warning]
> It may be possible that you generate a code that is registered to a Premium member.  
> This will cause you to pay more, in favour of the cardholder.  
> So far this has happened twice to me, paying about 60 cents extra each.  

> I decided to try and reverse engineer the algorithm behind the Albert Heijn Bonuskaart.

## In short

Albert Heijn Bonuskaart numbers follow the GTIN-13/EAN-13 format, starting with a fixed `26` prefix, followed by 11 digits that pass a checksum validation.

> `26xxxxx xxxxxc`  
> `26` = static prefix  
> `xxxxx` = semi-logical prefix range (partially reverse engineered)  
> `xxxxx` = 5 random digits  
> `c` = checksum digit  

This project generates fully valid Bonuskaart numbers using known valid prefix ranges and proper checksum calculation.

## Usage & Live Demo

You can use the tool directly via the [live page](https://skaffa.github.io/albert-heijn-bonuskaart-generator).  
Originally developed in Python, the project was later ported to HTML/CSS/JavaScript for easier access and cross-device compatibility.  
  
To run the original Python script locally:  
  
1. Download `generator.py`  
2. Run it using Python 3:  
  
   ```bash
   python3 generator.py
   ```

## Info
If you want to make sure for yourself that the codes are valid, go to https://www.ah.nl/klantenkaarten/bonuskaart and make an account. Then edit your card number for each card you want to validate. No rate limits  seem to be in place for this, just make sure to not use a VPN. During my tests, all codes generated with this script were valid, with no exceptions.  
Update: Even in the store it has worked every single time so far (about 20 times)

## Disclaimer
For educational purposes only
