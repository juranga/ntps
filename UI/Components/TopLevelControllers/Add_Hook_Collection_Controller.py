import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QTableWidgetItem

#from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component
#from UI.Components.TopLevelControllers.HookComponents.create_edit_hooks import Ui_CEHook
from UI.Components.TopLevelControllers.HookComponents.create_hook_collection_ui import Ui_Dialog
from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection
from Infrastructure.HookLibrary.Hook_Collection_Manager import Hook_Collection_Manager
#from UI.Components.TopLevelControllers.HookComponents import Ui_CEHook
#from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Add_Hook_Collection_Controller(QDialog):
    def startAddHookCollection(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            print("roigroups accepted from Save:")
            print(ui.roiGroups)
            self.HookCollection = Hook_Collection(ui.roiGroups['HCName'],ui.roiGroups['HCStatus'],ui.roiGroups['HCExecutionSequence'])
            print ("HOOK COLLECTION OBJECT CREATED WITH PATH: ",self.HookCollection.get_name()," & SEQUENCE #: ",self.HookCollection.get_sequence_number())
            if(self.hook_collection_table.rowCount() == 0):
                global hook_collection_manager
                hook_collection_manager = Hook_Collection_Manager()
                print("Hook Collection Manager Created: ")
            hook_collection_manager.add_hook_collection(self.HookCollection)
            self.hook_collection_table.insertRow(self.hook_collection_table.rowCount())
            self.hook_collection_table.setItem(self.hook_collection_table.rowCount()-1,0,QTableWidgetItem(self.HookCollection.get_name()))
            self.hook_collection_table.setItem(self.hook_collection_table.rowCount()-1,1,QTableWidgetItem(str("Number of Hooks")))
            self.hook_collection_table.setItem(self.hook_collection_table.rowCount()-1,2,QTableWidgetItem(self.HookCollection.enabled))
            self.hook_collection_table.setItem(self.hook_collection_table.rowCount()-1,3,QTableWidgetItem(str(self.HookCollection.get_sequence_number())))
            for x in hook_collection_manager.hook_collection:
                print("HOOK COLLECTIONS IN MANAGER: ", x.get_name())




    if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = Edit_Hook_Controller()
        w.show()
        sys.exit(app.exec())

