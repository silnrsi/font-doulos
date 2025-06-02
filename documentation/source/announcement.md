Release 7.000 - Major release

This release is focused on feature refinements, new character support, and diacritic positioning improvements.

Both desktop and web fonts are provided in a single, all-platforms package on the [Download page](https://software.sil.org/doulos/download).

***Note that this may be the final major version of Doulos SIL. Please consider switching to one of our other font families.***

#### Fewer alternate font versions

- There is no longer a *Compact* variant. A *Compact* version of the v6.2 font remains available from https://software.sil.org/lcgfonts/download/

- TypeTuner Web no longer offers line spacing alternatives for the v7 font (Normal, Tight, Loose). If you need Tight or Loose variants the v6.2 font s available and supports line spacing alternatives.

- There are no ‘pre-tuned’ regional or *Literacy* special-purpose modified variants. The v6.2 variants, including a *Literacy* version, remains available from https://software.sil.org/lcgfonts/download/. You can still manually create v7 variants with TypeTuner Web that include literacy forms and other alternatives.

#### Feature enhancements

- The default form for capital N with left hook has been changed to the lowercase style to match the capital Eng. The related feature (`cv44`) has been changed to substitute the uppercase style form.
    - U+019D LATIN CAPITAL LETTER N WITH LEFT HOOK

- Additions to Modifier Apostrophe feature (`cv70`)
    - U+02BB MODIFIER LETTER TURNED COMMA
    - U+02BD MODIFIER LETTER REVERSED COMMA
    - U+0312 COMBINING TURNED COMMA ABOVE
    - U+0314 COMBINING REVERSED COMMA ABOVE

- Addition to Rams Horn feature (`cv25`)
    - U+10791 MODIFIER LETTER SMALL RAMS HORN

- Small caps added for these parentheses and brackets
    - U+0028 LEFT PARENTHESIS
    - U+0029 RIGHT PARENTHESIS
    - U+005B LEFT SQUARE BRACKET
    - U+005D RIGHT SQUARE BRACKET
    - U+007B LEFT CURLY BRACKET
    - U+007D RIGHT CURLY BRACKET

#### New character support

- Unicode 16 additions
    - U+1C89 CYRILLIC CAPITAL LETTER TJE
    - U+1C8A CYRILLIC SMALL LETTER TJE
    - U+A7CB LATIN CAPITAL LETTER RAMS HORN
        - This was previously in the SIL PUA (U+F26E)
    - U+A7CC LATIN CAPITAL LETTER S WITH DIAGONAL STROKE
    - U+A7CD LATIN SMALL LETTER S WITH DIAGONAL STROKE
    - U+A7DA LATIN CAPITAL LETTER LAMBDA
    - U+A7DB LATIN SMALL LETTER LAMBDA
    - U+A7DC LATIN CAPITAL LETTER LAMBDA WITH STROKE

- Orthographic at signs
    - U+24B6 CIRCLED LATIN CAPITAL LETTER A
    - U+24D0 CIRCLED LATIN SMALL LETTER A

- Additional Cyrillic modifiers
    - U+A69C MODIFIER LETTER CYRILLIC HARD SIGN
    - U+A69D MODIFIER LETTER CYRILLIC SOFT SIGN

- Case mapping for Coptic eie
    - U+2C89 COPTIC SMALL LETTER EIE

- Upwards ancora (and revised downwards form)
    - U+2E14 DOWNWARDS ANCORA
    - U+2E15 UPWARDS ANCORA

- Prosodic symbols
    - U+23D1 METRICAL BREVE
    - U+23D2 METRICAL LONG OVER SHORT
    - U+23D3 METRICAL SHORT OVER LONG
    - U+23D4 METRICAL LONG OVER TWO SHORTS
    - U+23D5 METRICAL TWO SHORTS OVER LONG
    - U+23D6 METRICAL TWO SHORTS JOINED
    - U+2E3D VERTICAL SIX DOTS

- Doubled brackets and parentheses
    - U+27EA MATHEMATICAL LEFT DOUBLE ANGLE BRACKET
    - U+27EB MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET
    - U+2E28 LEFT DOUBLE PARENTHESIS
    - U+2E29 RIGHT DOUBLE PARENTHESIS

- Logical symbols
    - U+21AE LEFT RIGHT ARROW WITH STROKE
    - U+22BB XOR
    - U+22BC NAND
    - U+22BD NOR

#### Improvements and fixes

- Support added for complex positioning of bridging double diacritics and nearby marks. Correct rendering requires a very specific encoding sequence - see https://software.sil.org/fonts/bridging-diacritics/
    - U+035C COMBINING DOUBLE BREVE BELOW
    - U+035D COMBINING DOUBLE BREVE
    - U+035E COMBINING DOUBLE MACRON
    - U+035F COMBINING DOUBLE MACRON BELOW
    - U+0360 COMBINING DOUBLE TILDE
    - U+0361 COMBINING DOUBLE INVERTED BREVE
    - U+0362 COMBINING DOUBLE RIGHTWARDS ARROW BELOW
    - U+1DCD COMBINING DOUBLE CIRCUMFLEX ABOVE
    - U+1DFC COMBINING DOUBLE INVERTED BREVE BELOW
    - U+F17A COMBINING DOUBLE DIAERESIS (in SIL PUA)

- Fixed position of
    - U+1D09 LATIN SMALL LETTER TURNED I
    - U+1D4E MODIFIER LETTER SMALL TURNED I

- Fixed dotless form of
    - U+1DF1A LATIN SMALL LETTER I WITH STROKE AND RETROFLEX HOOK

- Revised design of
    - U+A720 MODIFIER LETTER STRESS AND HIGH TONE
    - U+A721 MODIFIER LETTER STRESS AND LOW TONE

- Improved design of some combining diacritics
    - U+032B COMBINING INVERTED DOUBLE ARCH BELOW
    - U+033C COMBINING SEAGULL BELOW
    - U+1AB7 COMBINING OPEN MARK BELOW
    - U+1AB8 COMBINING DOUBLE OPEN MARK BELOW
    - U+1AC7 COMBINING INVERTED DOUBLE ARCH ABOVE

- Revised anchors on many letters to improve diacritic positioning, including these and related letters
    - U+004A LATIN CAPITAL LETTER J
    - U+0051 LATIN CAPITAL LETTER Q
    - U+0059 LATIN CAPITAL LETTER Y
    - U+0066 LATIN SMALL LETTER F
    - U+0069 LATIN SMALL LETTER I
    - U+006A LATIN SMALL LETTER J
    - U+0079 LATIN SMALL LETTER Y
    - U+0434 CYRILLIC SMALL LETTER DE

- Reviewed anchors on spacing acutes and graves
    - U+0060 GRAVE ACCENT
    - U+00B4 ACUTE ACCENT
    - U+02CA MODIFIER LETTER ACUTE ACCENT
    - U+02CB MODIFIER LETTER GRAVE ACCENT
    - U+02CE MODIFIER LETTER LOW GRAVE ACCENT
    - U+02CF MODIFIER LETTER LOW ACUTE ACCENT
