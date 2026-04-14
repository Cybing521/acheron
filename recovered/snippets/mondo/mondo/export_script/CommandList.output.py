# Source Generated with Decompyle++
# File: tmpynwyq76f.marshal (Python 3.11)

datafile = scriptfile + '.npz'
logger.debug('Writing script to {}'.format(scriptfile))
f = open(scriptfile, 'wt', encoding = 'utf_8')
for v in self:
    s = str(v)
    if s == 'fig.show()':
        s = 'plt.show()'
    f.write(s)
    f.write('\n')
    None(None, None)
with None:
    if not None:
        pass
logger.debug('Writing script data to {}'.format(datafile))
# WARNING: Decompyle incomplete
