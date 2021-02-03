README
Doulos SIL v5.890
========================

This file describes the Graphite source files included with the Doulos SIL font. This information should be distributed along with the Doulos SIL font and any derivative works.

As a reminder: these source files are Copyright (c) 1994-2021 SIL International (http://www.sil.org/),
with Reserved Font Names "Doulos" and "SIL".
This Font Software is licensed under the SIL Open Font License, Version 1.1.
            
doulos.gdl            - definition of glyphs and glyph classes; auto-generated from the font
main.gdh              - bulk of Graphite rules and extra definitions to support them
features.gdh          - feature and language-feature definitions
pitches.gdh           - rules and definitions to support tone ligatures
fontSpecific.gdh      - font-specific definition for Doulos SIL
stddef.gdh            - standard GDL abbreviations

In order to modify the Graphite tables in this font:
* Strip out the existing tables
  Using the Font-TTF-Scripts package ( http://scripts.sil.org/FontUtils ), you could use something like:
    ttftable -delete graphite old-font-with-Graphite-tables.ttf  new-font-without-Graphite-tables.ttf 
* Run:
    grcompiler -d -v2 -n2048 -w3521 -w510 font.gdl ttf-file-with-Graphite-tables-stripped.ttf output-ttf.ttf
  
Further detail of features is available in the file /source/opentype/featureinfo.xlsx
