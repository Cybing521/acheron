# Source Generated with Decompyle++
# File: tmp9u4ltubj.marshal (Python 3.11)

new_value = self.actionClosableTabs.isChecked()
self.tabWidget.setTabsClosable(new_value)
self.preferences.closeable_tabs = new_value
if new_value:
    tab_bar = self.tabWidget.tabBar()
    tab_bar.setTabButton(0, QtWidgets.QTabBar.ButtonPosition.LeftSide, None)
    tab_bar.setTabButton(0, QtWidgets.QTabBar.ButtonPosition.RightSide, None)
    return None
