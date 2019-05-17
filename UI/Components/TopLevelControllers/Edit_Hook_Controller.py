import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QTableWidgetItem

#from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component
#from UI.Components.TopLevelControllers.HookComponents.create_edit_hooks import Ui_CEHook
from UI.Components.TopLevelControllers.HookComponents.create_edit_hooks import Ui_CEHook
from Infrastructure.HookLibrary.Hook import Hook
from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection
#from UI.Components.TopLevelControllers.Hook_Controller import Hook_Controller
#from UI.Components.TopLevelControllers.HookComponents import Ui_CEHook
#from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Edit_Hook_Controller(QDialog):
    def startEditHook(self, hook_collection):
        #super().__init__()
        Dialog = QtWidgets.QDialog()
        ui = Ui_CEHook()
        ui.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            print("roigroups accepted from save:")
            print(ui.roiGroups) #['Name'],['Description'],['Path']
            hook = Hook(ui.roiGroups['Path'],ui.roiGroups['Name'])
            if(self.tableWidget_2.rowCount() == 0):
                #hook_collection = Hook_Collection()
                print("Hook Collection Created: ",hook_collection.get_name())
            print ("HOOK OBJECT CREATED WITH PATH: ",hook.get_path()," & SEQUENCE #: ",hook.get_sequence_number())
            hook_collection.add_hook(hook)
            self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
            self.tableWidget_2.setItem(self.tableWidget_2.rowCount()-1,0,QTableWidgetItem(hook.display_name))
            self.tableWidget_2.setItem(self.tableWidget_2.rowCount()-1,1,QTableWidgetItem(ui.roiGroups['Description']))
            self.tableWidget_2.setItem(self.tableWidget_2.rowCount()-1,2,QTableWidgetItem(str(hook.get_sequence_number())))
            #for x in hook_collection.hook_list:
            
            #print("HOOK IN COLLECTION: ", x.get_path)
            


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = Edit_Hook_Controller()
        w.show()
        sys.exit(app.exec())        
