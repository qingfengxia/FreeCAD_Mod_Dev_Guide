
ModuleName="Fem"
#test existent is needed, by libcurl
ModuleFolder=[
("Init.py","Module initialization code, will be run during FreeCAD startup", 
"""   e.g. add importable and exportable file types, it is optional"""),
("InitGui.py","to declare Module's Workbench class",
"""to insert items into FreeCAD Gui"""),
(ModuleName+".dox","Independent Doxygen documentation for this module",""""""),
("Readme.md","Description of this module ,shown directly on github",""""""),
("CMakeList.txt","cmake config file, to define installaton of this module",""""""),
("App","C++ code to generate {} binary dyanamically linkable lib".format(ModuleName),
"""All nonGui code should go here, like classes derived from App::DocumentObject"""),
("Gui","C++ code to generate {}Gui binary dyanamically linkable lib".format(ModuleName),
"""Gui code should go here, like classes derived from TaskView, ViewProvider"""),
#("License.txt","License of this module if different from the main program FreeCAD",""""""),
#module meta info for ModuleManager
#
("C++ code in App subfolder",),
("App/PreCompiled.h","include some headers shared by most source code files",""""""),
("App/PreCompiled.cpp","include some headers shared by most source code files",""""""),
("App/CMakeLists.txt","cmake config file to generate dll or so shared dynamically linkable lib",""""""),
("Gui/App{}.cpp".format(ModuleName),"init_type,init DocumentObject",""""""),
("Gui/App{}Py.cpp".format(ModuleName),"register types, methods exported to Python",
"""```#methods can be accessed in python:
import {}
dir({})```""".format(ModuleName,ModuleName)),
#
("C++ code in Gui subfolder",),
("Gui/Workbench.h","to declare module workbench derived from `Gui::Workbench`",""""""),
("Gui/Workbench.cpp","",""""""),
("Gui/App{}Gui.cpp".format(ModuleName),"",
""" within function of init{}Gui():
- {}_Import_methods[]
- load command.cpp,
- workbench and ViewProvider init(),
- `Base::Interpreter().loadModule('python modules')`
- register preferences pages 
- load resource, mainly translation""".format(ModuleName,ModuleName)),
("Gui/App{}GuiPy.cpp".format(ModuleName),"wrapping code to export functions to python",
"""
`/* registration table */ struct PyMethodDef FemGui_Import_methods[]`
"""),
("Gui/PreCompiled.h","include some headers shared by most source code files",""""""),
("Gui/PreCompiled.cpp","contains single line `#include \"PreCompiled.h\"` ",""""""),
("Gui/CMakeLists.txt","cmake config file to generate dll or so shared dynamically linkable lib",""""""),
("Gui/Command.cpp","to add Toolbar and MenuItem to module workbench",""""""),
("Gui/Resources/{}.qrc".format(ModuleName),"file contains translattion for Qt widgets",""""""),
("","","""""")
]
