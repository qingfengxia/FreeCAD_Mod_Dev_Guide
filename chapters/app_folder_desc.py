#
AppFolder=[
("Application",),
 ("Application.h","method called in QApplication to init and run FreeCAD",
 """Mange `App::Document`, import/export files ,Path, ParameterManager/config, init()/addTypes()
The FreeCAD startup process will call `App::Application::initApplication()`, 
setup/init FreeCAD python module """),
 ("ApplicationPy.cpp","export method to python as FreeCAD module",
 """```import FreeCAD
dir(FreeCAD)```"""),
 ("Branding.h.cpp","Customise splashscreen and banner in CMD mode",""""""),
 ("FreeCADInit.py","def InitApplications() which adds Mod path to sys.path",
 """prepend all module paths to Python search path
Searching for modules... by file: `Init.py` in each module folder
`FreeCAD.__path__ = ModDict.values()`
init every application by `import Init.py`, call `InitApplications()`
"""),
#
("Property framework",),
 ("Property.h","Base class for all Properties, derived from Base::Persistence",
 """ 
 Can access attributes of a class by name without knowing the class type, enable access in Python, parameterise 3D part,  
 Useful methods: get/setValue(), save/restore(), get/setPyObject(), copy/paste(), getGroup/getPath/getType/getDocumentation()
 
 [PropertyContainer.cpp         PropertyFile.cpp   PropertyPythonObject.cpp
PropertyContainer.h           PropertyFile.h     PropertyPythonObject.h
PropertyContainerPyImp.cpp    PropertyGeo.cpp    PropertyStandard.cpp
PropertyContainerPy.xml       PropertyGeo.h      PropertyStandard.h
Property.cpp                  Property.h         PropertyUnits.cpp
PropertyExpressionEngine.cpp  PropertyLinks.cpp  PropertyUnits.h
PropertyExpressionEngine.h    PropertyLinks.h]"""),
 ("PropertyStandard.h","define Property for common types like string int",
""" why not template in c++?"""),
("PropertyContainer.h","define class PropertyContainer and PROPERTY related macro functions",
"""
DocumentObject is derived from this class, macro function will be explained in Property framework section
"""),
("DynamicProperty.h","Runtime added into PropertyContainer","""not derived from App::Property"""),
("ObjectIdentifier.h","define Component class and ObjectIdentifier class",
 """A component is a part of a Path object, and is used to either name a property or a field within a property. A component can be either a single entry, and array, or a map to other sub-fields."""),
("PropertyLinks.h","property is to Link DocumentObjects and Feautures in a document.",""""""),
("PropertyUnits.h","Quantiy as Property, PropertyAngle, PropertyAcceleration, etc",
"""its path is based on ObjectIdentifier"""),
("PropertyPythonObject.h"," to manage Py::Object instances as properties",""""""),
("PropertyGeo.h"," PropertyVector, PropertyMatrix, Property",
"""PropertyPlacementLink, 
`class AppExport PropertyGeometry : public App::Property // transformGeometry()  getBoundBox3d() `
`class AppExport PropertyComplexGeoData : public App::PropertyGeometry`"""),
("Enumeration.h",  "A bidirectional stringinteger mapping for enum", ""),
 #
 ("App::Document and App::DocumentObject",),
 ("Document.h","Corresponding to FreeCAD main saving file format for 3D part or other info: *.FCstd",
 """[Document.cpp                    DocumentObject.h
Document.h                      DocumentObjectPyImp.cpp
DocumentObject.cpp              DocumentObjectPy.xml
DocumentObjectFileIncluded.cpp  DocumentObserver.cpp
DocumentObjectFileIncluded.h    DocumentObserver.h
DocumentObjectGroup.cpp         DocumentObserverPython.cpp
DocumentObjectGroup.h           DocumentObserverPython.h
DocumentObjectGroupPyImp.cpp    DocumentPyImp.cpp
DocumentObjectGroupPy.xml       DocumentPy.xml
]"""),
 ("DocumentObject.h","Most important class in FreeCAD",
 """The inheritance chain is: Base::BaseClass->Base::Persistence->Base::PropertyContainer->DocumentObject"""), 
 ("DocumentGroup.h","DocumentObjectGroup class: Container of DocumentObject",""""""),  
 ("DocumentObserver.h","Minitoring the create, drop, change of DocumetnObject and emit signal",""""""),
 ("MergeDocuments.h","helper classes for document merge",""""""),
 ("Transactions.h","A collection of operation on DocumentObject like SQL database that can be rolled back",
 """DocumentObject could be restored to a previous state"""),
("FeaturePython.h","Generic Python feature class which allows to behave every DocumentObject derived class as Python feature  simply by subclassing",
"""
`// Special Feature-Python classes,  Feature is another name for DocumentObject` 
`typedef FeaturePythonT<DocumentObject> FeaturePython;`
`typedef FeaturePythonT<GeoFeature> GeometryPython;`"""),
#
("Expression framework",),
("Expression.h","Base class for FunctionExpression, OperatorExpression etc.",
"""expression and Parser for parameterization
[Expression.cpp      ExpressionParser.tab.c  lex.ExpressionParser.c
Expression.h        ExpressionParser.tab.h  PropertyExpressionEngine.cpp
ExpressionParser.l  ExpressionParser.y      PropertyExpressionEngine.h] """),
#
("Extension framework",),
('Extension.h', "extend function of object other than inheritance",
""" [DocumentObjectExtension.cpp       GeoFeatureGroupExtension.cpp  DocumentObjectExtension.h         GeoFeatureGroupExtension.h
DocumentObjectExtensionPyImp.cpp  GeoFeatureGroupExtensionPyImp.cpp  DocumentObjectExtensionPy.xml     GeoFeatureGroupExtensionPy.xml
ExtensionContainer.cpp            GroupExtension.cpp ExtensionContainer.h              GroupExtension.h
ExtensionContainerPyImp.cpp       GroupExtensionPyImp.cpp  ExtensionContainerPy.xml          GroupExtensionPy.xml
Extension.cpp        OriginGroupExtension.cpp  Extension.h                       OriginGroupExtension.h
ExtensionPyImp.cpp      OriginGroupExtensionPyImp.cpp ExtensionPy.xml       OriginGroupExtensionPy.xml]"""),
#
("Utilities",),
("MeasureDistance.h","Measure distance between two entity",""""""),
("ColorModel.h","Color bar like grayscale, inverse gray scale, Tria,",
"""Color class is defined here, constructed from uint32_t or 4 float number for RGBA."""),
("Material.h","appearance: color and transparency for rendering of 3D object",
""" define a few standard material
MaterialObject is derived from DocumentObject and contains data from Material class. 
[Material.cpp  MaterialObject.cpp  MaterialPyImp.cpp Material.h   MaterialObject.h    MaterialPy.xml]"""),
("MaterialObject.h","DocumentObject store key-valve pair for material information",
"""physical property of  *.ini style FCMat files, under `src/Mod/Material/StandardMaterial/<MaterialName>.FCMat`
`Fem::MechanicalMaterial` is python class derived from this class"""),
#
("App::GeoFeature and derived classes",),
("GeoFeature.h","Base class of all geometric document objects",
""" Derived from `DocumentObject`, contains only *PropertyPlacement*, see [GeoFeature.cpp]
"""),
("Plane.h","Object Used to define planar support for all kind of operations in the document space",
"""sketch is done on planes, derived from `App::GeoFeature` which is derived from `DocumentObject`"""),
("Placement.h" , "define six degree of freedom (orientation and position ) for placing a part in space",
"""derived from `App::GeoFeature`, 
A placement defines an orientation (rotation) and a position (base) in 3D space. It is used when no scaling or other distortion is needed.
"""),
#
 ("InventorObject.h","derived from App::GeoFeature wiht only 2 properties: PropertyString Buffer, FileName; ",""""""),
("VRMLObject.h","derived from App::GeoFeature",""""""),
("App::Data namespace and ComplexGeoData class",),
("ComplexGeoData.h","store data to represent complex geometry in line, facet(triangle) and segment",
"""
declare `Segment`, and `ComplexGeoData`, which has ref counting, in `App::Data` namespace.
`class AppExport ComplexGeoData: public Base::Persistence, public Base::Handled`
""")
]