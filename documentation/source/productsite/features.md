
Doulos SIL is an OpenType-enabled font that supports the Latin and Cyrillic scripts. It includes a number of optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'cv17'), although some applications may provide a direct way to control certain common features such as small caps. For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

*Please note that Graphite support has been removed in the current release, but continues to be available in the version 5 fonts. See our [Previous Versions archive](https://software.sil.org/doulos/download/previous-versions).*

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Doulos SIL as a web font, see *DoulosSIL-webfont-example.html* in the font package *web* folder. For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly, a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Stylistic alternates

#### Small caps from lowercase

<span class='affects'>Affects: all lowercase letters with capital equivalents</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>a ... z</span> (all letters with capital equivalents) | `smcp=0`
Small caps | <span class='doulos-smcp-1-R normal'>a ... z</span> (all letters with capital equivalents) | `smcp=1`

#### Small caps from capitals

*This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: all capitals</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>A ... Z</span> (all capitals) | `c2sc=0`
Small caps | <span class='doulos-c2sc-1-R normal'>A ... Z</span> (all capitals) | `c2sc=1`

#### Single-story a and g

*This feature was formerly called 'Literacy alternates'.*

<span class='affects'>Affects: U+0061 U+00AA U+00E0 U+00E1 U+00E2 U+00E3 U+00E4 U+00E5 U+0101 U+0103 U+0105 U+01CE U+01DF U+01E1 U+01FB U+0201 U+0203 U+0227 U+1E01 U+1E9A U+1EA1 U+1EA3 U+1EA5 U+1EA7 U+1EA9 U+1EAB U+1EAD U+1EAF U+1EB1 U+1EB3 U+1EB5 U+1EB7 U+2C65 U+2090 U+1D43 U+0363 U+0067 U+011D U+011F U+0121 U+0123 U+01E7 U+01F5 U+01E5 U+1E21 U+A7A1 U+1D4D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='doulos-R normal'>a ª à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | `ss01=0`
Single-story | <span class='doulos-ss01-1-R normal'>a ª à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | `ss01=1`

#### Single-story a (only)

<span class='affects'>Affects: U+0061 U+00AA U+00E0 U+00E1 U+00E2 U+00E3 U+00E4 U+00E5 U+0101 U+0103 U+0105 U+01CE U+01DF U+01E1 U+01FB U+0201 U+0203 U+0227 U+1E01 U+1E9A U+1EA1 U+1EA3 U+1EA5 U+1EA7 U+1EA9 U+1EAB U+1EAD U+1EAF U+1EB1 U+1EB3 U+1EB5 U+1EB7 U+2C65 U+2090 U+1D43 U+0363</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='doulos-R normal'>a ª à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ </span> | `ss11=0`
Single-story | <span class='doulos-ss11-1-R normal'>a ª à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ </span> | `ss11=1`

#### Single-story g (only)

<span class='affects'>Affects: U+0067 U+011D U+011F U+0121 U+0123 U+01E7 U+01F5 U+01E5 U+1E21 U+A7A1 U+1D4D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='doulos-R normal'>g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | `ss12=0`
Single-story | <span class='doulos-ss12-1-R normal'>g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | `ss12=1`

#### Barred-bowl forms 

<span class='affects'>Affects: U+0111 U+0180 U+01E5</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='doulos-R normal'>đ ƀ ǥ</span> | `ss04=0`
Barred-bowl | <span class='doulos-ss04-1-R normal'>đ ƀ ǥ</span> | `ss04=1`

### Character alternates

#### B hook

<span class='affects'>Affects: U+0181</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Ɓ</span> | `cv13=0`
Lowercase-style | <span class='doulos-cv13-1-R normal'>Ɓ</span> | `cv13=1`

#### D hook

<span class='affects'>Affects: U+018A</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Ɗ</span> | `cv17=0`
Lowercase-style | <span class='doulos-cv17-1-R normal'>Ɗ</span> | `cv17=1`

#### H stroke

<span class='affects'>Affects: U+0126</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Ħ</span> | `cv28=0`
Vertical stroke | <span class='doulos-cv28-1-R normal'>Ħ</span> | `cv28=1`

#### J stroke hook

<span class='affects'>Affects: U+0284</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='doulos-R normal'>ʄ</span> | `cv37=0`
Top serif | <span class='doulos-cv37-1-R normal'>ʄ</span> | `cv37=1`

#### Eng

<span class='affects'>Affects: U+014A</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard                          | <span class='doulos-R normal'>Ŋ</span> | `cv43=0`
Lowercase style on baseline       | <span class='doulos-cv43-1-R normal'>Ŋ</span> | `cv43=1`
Uppercase style with descender    | <span class='doulos-cv43-2-R normal'>Ŋ</span> | `cv43=2`
Alt. lowercase style on baseline  | <span class='doulos-cv43-3-R normal'>Ŋ</span> | `cv43=3`

#### N left hook

<span class='affects'>Affects: U+019D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Ɲ</span> | `cv44=0`
Lowercase-style | <span class='doulos-cv44-1-R normal'>Ɲ</span> | `cv44=1`

#### Open-O

<span class='affects'>Affects: U+0186 U+0254 U+1D10 U+1D53 U+1D97</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='doulos-R normal'>Ɔ ɔ ᴐ ᵓ ᶗ</span> | `cv46=0`
Top serif | <span class='doulos-cv46-1-R normal'>Ɔ ɔ ᴐ ᵓ ᶗ</span> | `cv46=1`

#### OU

<span class='affects'>Affects: U+0222 U+0223 U+1D3D U+1D15</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>Ȣ ȣ ᴕ ᴽ</span> | `cv47=0`
Open     | <span class='doulos-cv47-1-R normal'>Ȣ ȣ ᴕ ᴽ</span> | `cv47=1`

#### p hook

<span class='affects'>Affects: U+01A5</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>ƥ</span> | `cv49=0`
Right hook | <span class='doulos-cv49-1-R normal'>ƥ</span> | `cv49=1`

####  R tail

<span class='affects'>Affects: U+2C64</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Ɽ</span> | `cv55=0`
Lowercase-style | <span class='doulos-cv55-1-R normal'>Ɽ</span> | `cv55=1`

#### T hook

<span class='affects'>Affects: U+01AC</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>Ƭ</span> | `cv57=0`
Right hook | <span class='doulos-cv57-1-R normal'>Ƭ</span> | `cv57=1`

#### V hook

<span class='affects'>Affects: U+01B2 U+028B U+1DB9</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard                | <span class='doulos-R normal'>Ʋ ʋ ᶹ</span> | `cv62=0`
Straight with low hook  | <span class='doulos-cv62-1-R normal'>Ʋ ʋ ᶹ</span> | `cv62=1`
Straight with high hook | <span class='doulos-cv62-2-R normal'>Ʋ ʋ ᶹ</span> | `cv62=2`

#### Y hook

<span class='affects'>Affects: U+01B3</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='doulos-R normal'>Ƴ</span> | `cv68=0`
Left hook | <span class='doulos-cv68-1-R normal'>Ƴ</span> | `cv68=1`

#### Ezh

<span class='affects'>Affects: U+01B7 U+04E0</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard       | <span class='doulos-R normal'>Ʒ Ӡ</span> | `cv20=0`
Reversed sigma | <span class='doulos-cv20-1-R normal'>Ʒ Ӡ</span> | `cv20=1`

#### ezh curl

<span class='affects'>Affects: U+0293</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>ʓ</span> | `cv19=0`
Large bowl | <span class='doulos-cv19-1-R normal'>ʓ</span> | `cv19=1`

#### rams horn

<span class='affects'>Affects: U+0264</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='doulos-R normal'>ɤ</span> | `cv25=0`
Large bowl  | <span class='doulos-cv25-1-R normal'>ɤ</span> | `cv25=1`
Small gamma | <span class='doulos-cv25-2-R normal'>ɤ</span> | `cv25=2`

#### Clicks

<span class='affects'>Affects: U+01C0 U+01C1 U+01C2 U+2980</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard (descending) | <span class='doulos-R normal'>ǀ ǁ ǂ ⦀</span> | `cv69=0`
Baseline              | <span class='doulos-cv69-1-R normal'>ǀ ǁ ǂ ⦀</span> | `cv69=1`

### Diacritic and symbol alternates

#### Vietnamese-style diacritics

<span class='affects'>Affects: U+1EA4 U+1EA5 U+1EA6 U+1EA7 U+1EA8 U+1EA9 U+1EAA U+1EAB U+1EAE U+1EAF U+1EB0 U+1EB1 U+1EB2 U+1EB3 U+1EB4 U+1EB5 U+1EBE U+1EBF U+1EC0 U+1EC1 U+1EC2 U+1EC3 U+1EC4 U+1EC5 U+1ED0 U+1ED1 U+1ED2 U+1ED3 U+1ED4 U+1ED5 U+1ED6 U+1ED7</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard         | <span class='doulos-R normal'>Ấấ Ầầ Ẩẩ Ẫẫ Ắắ Ằằ Ẳẳ Ẵẵ Ếế Ềề Ểể Ễễ Ốố Ồồ Ổổ Ỗỗ</span> | `cv75=0`
Vietnamese-style | <span class='doulos-cv75-1-R normal'>Ấấ Ầầ Ẩẩ Ẫẫ Ắắ Ằằ Ẳẳ Ẵẵ Ếế Ềề Ểể Ễễ Ốố Ồồ Ổổ Ỗỗ</span> | `cv75=1`

#### Kayan diacritics

<span class='affects'>Affects: U+0300 U+0301</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='doulos-R normal'>◌̀́</span> | `cv79=0`
Side by side | <span class='doulos-cv79-1-R normal'>◌̀́</span> | `cv79=1`

#### Ogonek

<span class='affects'>Affects: U+0328 U+0104 U+0105 U+0118 U+0119 U+012E U+012F U+0172 U+0173 U+01EA U+01EB U+01EC U+01ED</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>anything with ◌̨ (Ąą Ęę Įį Ųų Ǫǫ Ǭǭ)</span> | `cv76=0`
Straight | <span class='doulos-cv76-1-R normal'>anything with ◌̨ (Ąą Ęę Įį Ųų Ǫǫ Ǭǭ)</span> | `cv76=1`

#### Caron

<span class='affects'>Affects: U+010F U+013D U+013E U+0165</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='doulos-R normal'>ď Ľ ľ ť</span> | `cv77=0`
Global-style | <span class='doulos-cv77-1-R normal'>ď Ľ ľ ť</span> | `cv77=1`

#### Modifier apostrophe

<span class='affects'>Affects: U+02BC U+A78B U+A78C</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>ʼ Ꞌ ꞌ</span> | `cv70=0`
Large    | <span class='doulos-cv70-1-R normal'>ʼ Ꞌ ꞌ</span> | `cv70=1`

#### Modifier colon

<span class='affects'>Affects: U+A789</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>꞉</span> | `cv71=0`
Expanded | <span class='doulos-cv71-1-R normal'>꞉</span> | `cv71=1`

#### Empty set

<span class='affects'>Affects: U+2205</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>∅</span> | `cv98=0`
Zero-style | <span class='doulos-cv98-1-R normal'>∅</span> | `cv98=1`

### Cyrillic alternates

*There are also Cyrillic characters affected by the “Ezh” and “Small capitals” features. Some languages may also use the “Modifier apostrophe”.*

#### Cyrillic E

<span class='affects'>Affects: U+042D U+044D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>Э э</span> | `cv80=0`
Mongolian-style | <span class='doulos-cv80-1-R normal'>Э э</span> | `cv80=1`

#### Cyrillic shha

<span class='affects'>Affects: U+04BB</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>һ</span> | `cv81=0`
Uppercase-style | <span class='doulos-cv81-1-R normal'>һ</span> | `cv81=1`

#### Cyrillic breve

<span class='affects'>Affects: U+0306</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard       | <span class='doulos-R normal'>anything with ◌̆ (Ә̆ә̆)</span> | `cv82=0`
Cyrillic-style | <span class='doulos-cv82-1-R normal'>anything with ◌̆ (Ә̆ә̆)</span> | `cv82=1`

#### Serbian Cyrillic alternates

*Unlike other features, this is activated by tagging the span of text as being in the Serbian language, not by turning on an OpenType feature. It is also not available through TypeTuner Web although a similar feature is supported (cv84).*

<span class='affects'>Affects: U+0431</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>б</span> | 
Serbian  | <span class='doulos-R normal' lang='sr'>б</span> | `lang='sr'`

#### Macedonian Cyrillic alternates

*Unlike other features, this is activated by tagging the span of text as being in the Macedonian language, not by turning on an OpenType feature. It is also not available through TypeTuner Web although a similar feature is supported (cv84).*

<span class='affects'>Affects: U+0431</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='doulos-R normal'>б</span> | 
Macedonian | <span class='doulos-R normal' lang='mk'>б</span> | `lang='mk'`

#### Serbian and Macedonian Cyrillic alternates

*This feature provides an alternate way to activate the Serbian and Macedonian forms in applications that do not support language-specific features.*

<span class='affects'>Affects: U+0431</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard                 | <span class='doulos-R normal'>б</span> | `cv84=0`
Serbian Macedonian forms | <span class='doulos-cv84-1-R normal'>б</span> | `cv84=1`

### Tone alternates

#### Chinantec tones

<span class='affects'>Affects: U+02CB U+02C8 U+02C9 U+02CA</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='doulos-R normal'>ˋ ˈ ˉ ˊ</span> | `cv90=0`
Chinantec-style | <span class='doulos-cv90-1-R normal'>ˋ ˈ ˉ ˊ</span> | `cv90=1`

#### Tone numbers

*This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+02E5 U+02E6 U+02E7 U+02E8 U+02E9 U+A712 U+A713 U+A714 U+A715 U+A716</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖</span> | `cv91=0`
Numbers  | <span class='doulos-cv91-1-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖</span> | `cv91=1`

#### Hide tone contour staves

*This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+02E5 U+02E6 U+02E7 U+02E8 U+02E9 U+A712 U+A713 U+A714 U+A715 U+A716</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='doulos-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖ (˩˦˥˧˨ ꜖꜓꜒꜔꜕)</span> | `cv92=0`
Hide staves  | <span class='doulos-cv92-1-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖ (˩˦˥˧˨ ꜖꜓꜒꜔꜕)</span> | `cv92=1`

### Numeral alternates

#### Subscript numerals

*This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='doulos-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `subs=0`
Subscript | <span class='doulos-subs-1-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `subs=1`

#### Superscript numerals

*This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='doulos-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `sups=0`
Superscript | <span class='doulos-sups-1-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `sups=1`

#### Automatic fractions

*When activated this feature will automatically create fractions when numerals are separated by either the fraction slash (U+2044) or the solidus (U+002F). This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039 U+002F U+2044</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard (none) | <span class='doulos-R normal'>1⁄2 456⁄789 1/2 456/789</span> | `frac=0`
Automatic       | <span class='doulos-frac-1-R normal'>1⁄2 456⁄789 1/2 456/789</span> | `frac=1`

[font id='doulos' face='DoulosSIL-Regular' size='150%']
[font id='doulos-smcp-1' face='DoulosSIL-Regular' size='150%' feats='smcp 1']
[font id='doulos-c2sc-1' face='DoulosSIL-Regular' size='150%' feats='c2sc 1']
[font id='doulos-ss01-1' face='DoulosSIL-Regular' size='150%' feats='ss01 1']
[font id='doulos-ss11-1' face='DoulosSIL-Regular' size='150%' feats='ss11 1']
[font id='doulos-ss12-1' face='DoulosSIL-Regular' size='150%' feats='ss12 1']
[font id='doulos-ss04-1' face='DoulosSIL-Regular' size='150%' feats='ss04 1']
[font id='doulos-cv13-1' face='DoulosSIL-Regular' size='150%' feats='cv13 1']
[font id='doulos-cv17-1' face='DoulosSIL-Regular' size='150%' feats='cv17 1']
[font id='doulos-cv28-1' face='DoulosSIL-Regular' size='150%' feats='cv28 1']
[font id='doulos-cv37-1' face='DoulosSIL-Regular' size='150%' feats='cv37 1']
[font id='doulos-cv43-1' face='DoulosSIL-Regular' size='150%' feats='cv43 1']
[font id='doulos-cv43-2' face='DoulosSIL-Regular' size='150%' feats='cv43 2']
[font id='doulos-cv43-3' face='DoulosSIL-Regular' size='150%' feats='cv43 3']
[font id='doulos-cv44-1' face='DoulosSIL-Regular' size='150%' feats='cv44 1']
[font id='doulos-cv46-1' face='DoulosSIL-Regular' size='150%' feats='cv46 1']
[font id='doulos-cv47-1' face='DoulosSIL-Regular' size='150%' feats='cv47 1']
[font id='doulos-cv49-1' face='DoulosSIL-Regular' size='150%' feats='cv49 1']
[font id='doulos-cv55-1' face='DoulosSIL-Regular' size='150%' feats='cv55 1']
[font id='doulos-cv57-1' face='DoulosSIL-Regular' size='150%' feats='cv57 1']
[font id='doulos-cv62-1' face='DoulosSIL-Regular' size='150%' feats='cv62 1']
[font id='doulos-cv62-2' face='DoulosSIL-Regular' size='150%' feats='cv62 2']
[font id='doulos-cv68-1' face='DoulosSIL-Regular' size='150%' feats='cv68 1']
[font id='doulos-cv20-1' face='DoulosSIL-Regular' size='150%' feats='cv20 1']
[font id='doulos-cv19-1' face='DoulosSIL-Regular' size='150%' feats='cv19 1']
[font id='doulos-cv25-1' face='DoulosSIL-Regular' size='150%' feats='cv25 1']
[font id='doulos-cv25-2' face='DoulosSIL-Regular' size='150%' feats='cv25 2']
[font id='doulos-cv69-1' face='DoulosSIL-Regular' size='150%' feats='cv69 1']
[font id='doulos-cv75-1' face='DoulosSIL-Regular' size='150%' feats='cv75 1']
[font id='doulos-cv79-1' face='DoulosSIL-Regular' size='150%' feats='cv79 1']
[font id='doulos-cv76-1' face='DoulosSIL-Regular' size='150%' feats='cv76 1']
[font id='doulos-cv77-1' face='DoulosSIL-Regular' size='150%' feats='cv77 1']
[font id='doulos-cv70-1' face='DoulosSIL-Regular' size='150%' feats='cv70 1']
[font id='doulos-cv71-1' face='DoulosSIL-Regular' size='150%' feats='cv71 1']
[font id='doulos-cv98-1' face='DoulosSIL-Regular' size='150%' feats='cv98 1']
[font id='doulos-cv80-1' face='DoulosSIL-Regular' size='150%' feats='cv80 1']
[font id='doulos-cv81-1' face='DoulosSIL-Regular' size='150%' feats='cv81 1']
[font id='doulos-cv82-1' face='DoulosSIL-Regular' size='150%' feats='cv82 1']
[font id='doulos-cv84-1' face='DoulosSIL-Regular' size='150%' feats='cv84 1']
[font id='doulos-cv90-1' face='DoulosSIL-Regular' size='150%' feats='cv90 1']
[font id='doulos-cv91-1' face='DoulosSIL-Regular' size='150%' feats='cv91 1']
[font id='doulos-cv92-1' face='DoulosSIL-Regular' size='150%' feats='cv92 1']
[font id='doulos-subs-1' face='DoulosSIL-Regular' size='150%' feats='subs 1']
[font id='doulos-sups-1' face='DoulosSIL-Regular' size='150%' feats='sups 1']
[font id='doulos-frac-1' face='DoulosSIL-Regular' size='150%' feats='frac 1']
