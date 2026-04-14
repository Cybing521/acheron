# Source Generated with Decompyle++
# File: tmp1yye2ep5.marshal (Python 3.11)

tab_widget = self.get_tab_widget(controller)
if not tab_widget:
    return None

try:
    if self.shown_tab == tab_widget:
        self.shown_tab = None
    index = self.tab_widgets.index(tab_widget)
    self.tab_widgets.pop(index)
    self.tabWidget.removeTab(index + 1)
except ValueError:
    pass

tab_widget.deleteLater()
if len(self.tab_widgets) == 0:
    self.stackedWidget.setCurrentIndex(1)
    self.logo_animation.start()
tree_item = self.tab_tree_items.pop(tab_widget, None)
# WARNING: Decompyle incomplete
