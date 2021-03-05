#!/usr/bin/python3
# this is a smith configuration file

# output folders use smith defaults and don't need to be set here

# set some default folders (most are already set by default)
#STANDARDS = 'references/v5'
STANDARDS = 'references/b1'

APPNAME = 'DoulosSIL'
familyname = APPNAME
DEBPKG = 'fonts-sil-doulos'

# Get VERSION and BUILDLABEL from Regular UFO; must be first function call:
getufoinfo('source/' + familyname + '-Regular' + '.ufo')

ftmlTest('tools/ftml-smith.xsl')

opts = preprocess_args({'opt': '--quick'})

# APs to ignore when generating OT and GDL classes
omitapps = '--omitaps "C L11 L12 L13 L21 L22 L23 L31 L32 L33 ' + \
                'C11 C12 C13 C21 C22 C23 C31 C32 C33 U11 U12 U13 U21 U22 U23 U31 U32 U33"'

cmds = []
cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${DS:FILE}']))
cmds.append(cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'))

#for dspace in ('Roman', 'Italic'):
for dspace in ('Roman',):
#for dspace in ('Italic',):
    designspace('source/' + familyname + dspace + '.designspace',
#                target = process('${DS:FILENAME_BASE}.ttf', 
#                    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${DS:FILE}'])),
                target = process('${DS:FILENAME_BASE}.ttf', *cmds),
                instances = ['Doulos SIL Regular'] if '--quick' in opts else None,
#                ap = 'source/${DS:FILENAME_BASE}_ap.xml',
#                classes = 'source/${DS:FAMILYNAME_NOSPC}_classes.xml', # fails for Gentium Book
                classes = 'source/{}_classes.xml'.format(familyname),
                opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/${DS:FILENAME_BASE}.fea',
                    make_params = omitapps,
                    depends = ('source/opentype/{}_gsub.fea'.format(familyname),
                        'source/opentype/${DS:FILENAME_BASE}_gpos_lkups.fea',
                        'source/opentype/{}_gpos_feats.fea'.format(familyname),
                        'source/opentype/{}_gdef.fea'.format(familyname)),
                    to_ufo = 'True' # copies to instance UFOs
                    ),
#               graphite = gdl('source/${DS:FILENAME_BASE}.gdl',
#                   master = 'source/graphite/main.gdh',
#                   make_params = omitapps,
#                   params = '-e gdlerr-${DS:FILENAME_BASE}.txt',
#                   depends = ('source/graphite/features.gdh',
#                       'source/graphite/pitches.gdh',
#                       'source/graphite/stddef.gdh')
#                   ),
                woff = woff('web/${DS:FILENAME_BASE}.woff',
                    metadata=f'../source/{familyname}-WOFF-metadata.xml',
                    cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
                    ),
                version = VERSION,
#                pdf=fret(params = '-r -oi')
                )

def configure(ctx):
    ctx.find_program('ttfautohint')
