pushd C:\Users\wardak\Mine\smith_vm\font-doulos

py C:\Users\wardak\Mine\smith_vm\font-doulos\tools\psfgenftml.py "source\DoulosSIL-Regular.ufo" "tests\AllCharsDR.ftml" -t allchars -f D -i "source\glyph_data.csv" -s "../results/DoulosSIL-Regular.ttf" --scale 200 -l "tests\logs\AllChars_DR.log"

py C:\Users\wardak\Mine\smith_vm\font-doulos\tools\psfgenftml.py "source\DoulosSIL-Regular.ufo" "tests\DiacDR.ftml" -t diac -f D -i "source\glyph_data.csv" -s "../results/DoulosSIL-Regular.ttf" --scale 200 -l "tests\logs\Diac_DR.log"

py C:\Users\wardak\Mine\smith_vm\font-doulos\tools\psfgenftml.py "source\DoulosSIL-Regular.ufo" "tests\FeaturesDR.ftml" -t features -f D -i "source\glyph_data.csv" -s "../results/DoulosSIL-Regular.ttf" --scale 200 -l "tests\logs\Features_DR.log"

popd
