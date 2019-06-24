
GuiFolder=[
########################################
 ("Application.h","Gui related init code, run after `App::Application::initApplication()`",
 """ `Gui::Application` is different from `App::Application`, it mainly deals with Gui stuff, Documents, Views and Workbenches
 - type system: `initTypes(), initApplication() and runApplication(); `
 - document file open: `importFrom();` 
 - singleton: `*Application::Instance*` 
 - `Gui::Document* activeDocument(void) const;`
 - `void attachView(Gui::BaseView* pcView);`
 - `bool activateWorkbench(const char* name);`
 - `Gui::MacroManager *macroManager(void);`
 - `Gui::CommandManager &commandManager(void);`
 """),
("ApplicationPy.cpp","Export Gui::Application methods as FreeCADGui python module",
"""other ClassNamePy.cpp are also init and incorporated into FreeCADGui.py, Control, Selection module"""),
("FreeCADGuiInit.py"," function like Init.py and InitGui.py in other module",
"""define Workbench and StdWorkbech python class, InitApplications(), and add types"""),
("Gui components",),
("Workbench.h","class in FreeCAD, each module has one class derived from this",
"""  
StdWorkbech <- Workbench <- BaseClass
The PythonBaseWorkbench class allows the manipulation of the workbench from Python.
   `virtual void setupContextMenu(const char* recipient, MenuItem*) const; `
The workbench defines which GUI elements (such as toolbars, menus, dockable windows, ...) 
are added to the mainwindow and which gets removed or hidden. 
 To create workbenches you should use the API of WorkbenchManager.
    [Workbench.cpp         Workbench.h           WorkbenchPyImp.cpp
WorkbenchFactory.cpp  WorkbenchManager.cpp  WorkbenchPy.xml
WorkbenchFactory.h    WorkbenchManager.h
PythonWorkbenchPyImp.cpp PythonWorkbenchPy.xml]
"""),
("Window.h","Adapter class to the parameter of FreeCAD for all windows",
"""Retrieve the parameter group of the specific window by the windowname.
`class GuiExport WindowParameter : public ParameterGrp::ObserverType`"""),
("MainWindow.h","QMainWindow, also defined MDITabbar class",""""""),
("GuiConsole.h","what is the reationship with PythonConsole?",""""""),
("PythonEditor.h","python macro file view and edit",""""""),
("PythonConsole.h","Where python command can be typed in, GUI commands show up",""""""),
("PrefWidgets.h","The preference widget classes like PrefRadioButton used in *Preference Page*",
""" PrefRadioButton is derived from QRadioButton and PrefWidget 
If you want to extend a QWidget class to save/restore its data  you just have to derive from this class and implement the methods 
 restorePreferences() and savePreferences()."""),
 ("StatusWidget.h","",""""""),
 #
("Singleton Gui services",),
("MenuManager.h","module can add new Mune and MenutItem",""""""),
("ToolBarManager.h","module can add new ToolBar and ToolBox",""""""),
("ToolBoxManager.h","add ToolBox to MainWindow",""""""),
("WorkbenchManager.h","activate workbench",""""""),
("DockWindowManager.h","",""""""),
####################################################
("Model-Document-View design pattern",),
("Document.h","Document class's corresponding object in the Gui namespace",
"""`Gui::Document class` includes a member of `App::Document  class`
Its main responsibility is keeping track off open windows for a document and warning on unsaved closes.
All handled views on the document must inherit from MDIView"""),
("DocumentModel.h","derived from QAbstractItemModel, represents DocumentObject in diff view", 
"""Qt Model-View design to split data and GUI rendering widgets"""),
("View.h","define BaseView for various derived *View* class",
""" DockWindow and MDIView are derived from BaseView, see doxygen inheritance graph
module developers need not know such low level API as in
[CombiView.cpp         GraphvizView.cpp  ProjectView.h      TreeView.cpp
CombiView.h           GraphvizView.h    PropertyView.cpp   TreeView.h
CommandView.cpp       HelpView.cpp      PropertyView.h     View.cpp
DlgReportView.ui      HelpView.h        ReportView.cpp     View.h
DlgSettings3DView.ui  MDIView.cpp       ReportView.h
EditorView.cpp        MDIView.h         SelectionView.cpp
EditorView.h          ProjectView.cpp   SelectionView.h]"""),
("MDIView.h","View binding with `Gui::Document`",
"""3D view scene is derived from this class, MDIView can be organised by Tab """),
("DockWindow.h","organise diff dockable widgets in workbench",
"""derived from `BaseView` and `QWidget`"""),
("CombiView.h","TreeView+TaskView of the group of `DocumentObject`",
"""Derived from DockWindows, showDialog(), getTaskPanel()"""),
("PropertyView.h","show in CombiView, can modify DocumentObject by setting property",
"""`class PropertyView : public QWidget, public Gui::SelectionObserver`"""),
######################################
("Transation, Command, Macro record framework",),
("Macro.h","Collection of python code can be play back",""""""),
("Command.h","Base class for command used in transactonal operation to document",
""" There are a lot `stdCmd*` classed,  CommandManager [Command.cpp      Command.h         
CommandTest.cpp    DlgCommandsImp.cpp
CommandDoc.cpp   CommandMacro.cpp  CommandView.cpp    DlgCommandsImp.h
CommandFeat.cpp  CommandStd.cpp    CommandWindow.cpp  DlgCommands.ui ]"""),
("Action.h","The Action class is the link between Qt's QAction class and FreeCAD's command classes",
"""The ActionGroup class is the link between Qt's QActionGroup class and  FreeCAD's command classes
WorkbenchGroup, WorkbenchComboBox, why defined in this header?
UndoAction, RedoAction, ToolboxAction, `class GuiExport WindowAction : public ActionGroup`
 The RecentFilesAction class holds a menu listed with the recent files.
"""),
("ActionFunction.h","",""""""),
######################################
("Selection in View and identify it DocumentObject tree",),
("Selection.h","represent selected DocumentObject",
""" see details in *Selection Framework* section 
[lex.SelectionFilter.c  SelectionFilter.y     SoFCSelectionAction.cpp
MouseSelection.cpp     Selection.h               SoFCSelectionAction.h
MouseSelection.h       SelectionObject.cpp       SoFCSelection.cpp
Selection.cpp          SelectionObject.h         SoFCSelection.h
SelectionFilter.cpp    SelectionObjectPyImp.cpp  SoFCUnifiedSelection.cpp
SelectionFilter.h      SelectionObjectPy.xml     SoFCUnifiedSelection.h
SelectionFilter.l      SelectionView.cpp SelectionFilter.tab.c  SelectionView.h] """),
######################################
("TaskView Framework",),
("Control.h" ,"ControlSingleton is TaskView controller, update all views for document change",""),
("TaskView","TaskView is feature setup dialog embedded in left pane",""""""),
####################################
("Python related classes",),
("PythonConsole.h","Interactive Python console in dockable windows",""""""),
("PythonEditor.h","QTextEdit with Python grammar highligher",""""""),
("PythonDebugger.h","???",""""""),
#####################################
("Widgets with quantity/expression support",),
("SpinBox.h","ExpressionBinding+QSpinBox",
"""[InputField.h InputVector.h]"""),
("QuantitySpinBox.h","QSpinBox with unit support",""""""),
("PropertyPage.h","PreferencePage and PropertyPage",""""""),
("TextEdit.h","Text input widget",""""""),
####################################
("Utility classes",),
("Thumbnail.h","show thumbnail in file explorer",""""""),
("Splashscreen.h","customize FreeCAD startup Splashscreen",""""""),
("CallTips.h","",""""""),
("WhatsThis.h","gives tip for ToolBar for mouse-over event",""""""),
("Assistant.h","`startAssistant(); in QProcess`",""""""),
("WaitCursor.h","hint user to wait and disable user input",""""""),
("ProgressDialog.h","show progress in dialog",""""""),
("ProgressBar.h","show progress in statusbar",""""""),
("Placement.h","derived from Gui::LocationDialog to edit ViewProvider's Placement",""""""),
("Transform.h","derived from Gui::LocationDialog to edit Transormation",""""""),
("Utilities.h","Utility functions",""""""),
("Flag.h","???",""""""),
#other widgets, why not PySide widgets?
########################################
("ViewProvider framework, 2D/3D visualization related classes",),
("ViewProvider.h","base class for DocumentObject in rendering",
"""derived classes: [ViewProviderAnnotation.cpp           ViewProviderInventorObject.cpp
ViewProviderAnnotation.h             ViewProviderInventorObject.h
ViewProviderBuilder.cpp              ViewProviderMaterialObject.cpp
ViewProviderBuilder.h                ViewProviderMaterialObject.h
ViewProvider.cpp                     ViewProviderMeasureDistance.cpp
ViewProviderDocumentObject.cpp       ViewProviderMeasureDistance.h
ViewProviderDocumentObjectGroup.cpp  ViewProviderPlacement.cpp
ViewProviderDocumentObjectGroup.h    ViewProviderPlacement.h
ViewProviderDocumentObject.h         ViewProviderPlane.cpp
ViewProviderDocumentObjectPyImp.cpp  ViewProviderPlane.h
ViewProviderDocumentObjectPy.xml     ViewProviderPyImp.cpp
ViewProviderExtern.cpp               ViewProviderPythonFeature.cpp
ViewProviderExtern.h                 ViewProviderPythonFeature.h
ViewProviderFeature.cpp              ViewProviderPythonFeaturePyImp.cpp
ViewProviderFeature.h                ViewProviderPythonFeaturePy.xml
ViewProviderGeometryObject.cpp       ViewProviderPy.xml
ViewProviderGeometryObject.h         ViewProviderVRMLObject.cpp
ViewProvider.h                       ViewProviderVRMLObject.h]"""),
("ViewProviderDocumentObject.h","base class for view providers of attached document object",
""" `void 	attach (App::DocumentObject *pcObject)`, 
redraw after changing obj's property`updateData (const App::Property *)`
"""),
("ViewProviderGeometryObject.h","base class for all view providers that display geometric data, like mesh, point cloudes and shapes",""""""),
("ViewProviderExtern.h","render OpenInventor *.iv file or iv string",""""""),
("ViewProviderAnnotation.h","Text render in 3D scene",""""""),
("ViewProviderFeature.h","has full Python support on this class",""""""),
("ViewProviderPythonFeature.h","???",""""""),
######################################
("OpenInventor/Coin3D rendering related classes",),
("SoFCDB.h","The FreeCAD database class to initialioze all onw Inventor nodes",),
("SoFCSelection.h","extend SoNode of Coin3D/OpenInventor",
"""header file name begins with *SoFC* is derived from OpenInventor objects used by FreeCAD"""),
("View3DInventor.h","contains View3DInventorViewer obj and control parameter and event",
"""`View3DInventor : public MDIView, public ParameterGrp::ObserverType`"""),
("View3DInventorViewer.h","3D rendering in QGraphicsView",
"""bridge the gap between OpenInvetorObject and ViewProvider
derived from Quarter::SoQTQuarterAdaptor and Gui::SelectionSingleton::ObserverType"""),
("View3DPy.h","PyObject controls *View3DInventor*, like view angle, viewLeft()...",
"""[View3DInventor.cpp          View3DInventorRiftViewer.cpp  View3DPy.cpp
View3DInventorExamples.cpp  View3DInventorRiftViewer.h    View3DPy.h
View3DInventorExamples.h    View3DInventorViewer.cpp      View3DViewerPy.cpp
View3DInventor.h            View3DInventorViewer.h        View3DViewerPy.h ]"""),
########################################
("Network related related classes",),
("DownloadItem.h","",""""""),
("DownloadManager.h","",""""""),
("NetworkRetriever.h","",""""""),
#
########################################
("subfolders in Gui",),
("3Dconnexion","3D mouse 3Dconnexion's supporting lib",""""""),
("Inventor","Inventor 3D rendering lib",""""""),
("TaskView","TaskView Framework for FreeCAD Gui",""),
("QSint","Collection of extra Qt widgets from community",""""""),
("iisTaskPanel","Task panel UI widgets, now part of QSint",""""""),
("propertyeditor","Widget for property edit for DocumentObject",""""""),
("Language","translation for FreeCADGui",""""""),
("Icons","icon for commands","""""")
]