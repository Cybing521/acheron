# Source Generated with Decompyle++
# File: tmp4t81sdoe.marshal (Python 3.11)

impl = getDOMImplementation()
if not impl:
    m = self.tr('Error loading serializer!')
    QtWidgets.QMessageBox.critical(self, self.tr('Error'), m)
    logger.error(m)
    return None
dt = None.createDocumentType('html', '-//W3C//DTD XHTML 1.0 Strict//EN', 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd')
dom = impl.createDocument('http://www.w3.org/1999/xhtml', 'html', dt)
html = dom.documentElement
head = dom.createElement('head')
html.appendChild(head)
title = dom.createElement('title')
title_string = f'''{self.serial_number} Modbus Details'''
title.appendChild(dom.createTextNode(title_string))
head.appendChild(title)
body = dom.createElement('body')
html.appendChild(body)
h1 = dom.createElement('h1')
h1.appendChild(dom.createTextNode(title_string))
body.appendChild(h1)
p = dom.createElement('p')
body.appendChild(p)
# WARNING: Decompyle incomplete
