from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from libs.Ui_Settings import Ui_DlgSettings
from libs.config import CConfig


class SettingsDialog(QDialog, Ui_DlgSettings):
    def __init__(self, text="Settings", parent=None, listItem=None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)
        config = CConfig()
        self.sldFontSize.setValue(config.SETTING_FONT_SIZE)
        self.sldLineSize.setValue(config.SETTING_PEN_SIZE)
        self.sldTransparency.setValue(config.SETTING_TRANSPARENCY)
        self.sldLblIndent.setValue(config.SETTING_LABEL_INDENT)

    @pyqtSlot()
    def on_btnOK_clicked(self):
        config = CConfig()
        config.SETTING_FONT_SIZE = self.sldFontSize.value()
        config.SETTING_PEN_SIZE = self.sldLineSize.value()
        config.SETTING_TRANSPARENCY = self.sldTransparency.value()
        config.SETTING_LABEL_INDENT = self.sldLblIndent.value()
        self.close()

    @pyqtSlot()
    def on_btnCancel_clicked(self):
        self.close()