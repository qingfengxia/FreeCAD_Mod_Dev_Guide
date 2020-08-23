#all files under "Base/"
BaseFolder=[
("Basic class and Type system",),
("Type.h" ,"register type and create instance from name", "see code snippets in later section"),
("BaseClass.h","using macro function to make type system and link to Python",
""" see detailed analysis in the later section"""),
("Exception.h"," base class for all FreeCAD exceptios, derived from BaseClass",
"""can be constructed from std::exception, see inherit graph for all derived exceptions"""),
#
("Python related headers",),
("Interpreter.h","Very important and frequently included header file",
"""define classes: `PyException, PyGILStateLocker, InterpreterSingleton`
define methods: `addType(), loadModule()`, will be discussed in Python wrapping section"""),
("PyExport.h", "define PyHandle<> temaplate class",
"""  Using pointers on classes derived from PyObjectBase would be potentionaly dangerous
because you would have to take care of the reference counting of python by yourself.
Therefore this class was designed. It takes care of references and  as long as a object of this class exists the handled class get  not destructed.
That means a PyObjectBase derived object you can  only destruct by destructing all FCPyHandle and all python  references on it!"""),
("PyObjectBase.h","Base Class for all classed exposed to python interpreter",""),
("PyTools.h" ,"ppembed-modules.c: load,access module objects", ""),
("swigrun.cpp","there are several with diff swig version",
"cpp files related to diff swig version are not listed here"),
("swigrun.inl","swig for python binding",""),
#
("Input and output and File related",),
("Reader.h" ,"XML file reader for DocumentObject for persistence",""),
("Writer.h" ,"XML file writer for DocumentObject",""),
("Stream.h","define adapter classes for Qt class QByteArray; class QIODevice;class QBuffer;",
""""""),
("gzStream.h" ,"gzip compressed file Stream",""),
("InputSource.h" ,"",
"`class BaseExport StdInputStream : public XERCES_CPP_NAMESPACE_QUALIFIER BinInputStream`"),
("FileInfo.h"  ,"File name unification class",
"""This class handles everything related to file names the file names which are internal generally UTF-8 encoded on all platforms."""),
("FileTemplate.h","used for testing purpose",""),
("Parameter.h"  ,"ParameterGrp: key-value, XML persistence as app config",
"""`class  BaseExport ParameterGrp	: public Base::Handled,public Base::Subject <const char*>`
`class BaseExport ParameterManager	: public ParameterGrp`"""),
("Console.h" ,"output message to terminal which starts FreeCADCmd",
"""ConsoleObserver and ConsoleSingleton with python code [Console.cpp],
This is not Python Console, but dealing with stdio, logging to terminal which starts FreeCADCmd.
`class BaseExport ConsoleObserverStd: public ConsoleObserver` to write Console messages and logs the system con.
"""),
("Debugger.h","Debugger class",
"""Debugging related classes in source files [Debugger.h Debugger.cpp StackWalker.h StackWalker.cpp MemDebug.h]"""),
#
("serialization support, example of class with cpp, py and XML code",),
("Persistence.h" ,"serialization of objects","base class for DocumentObject, Property, etc"),
("Persistence.cpp" ,"C++ implementation of Persistence class",""),
("PersistencePyImp.cpp" ,"automatically generated C++ code for exporting Persistence class to python",""),
("PersistencePy.xml" ,"XML to generate PersistencePyImp.cpp by python script",""),
#
("Geometry related calculation classes with *Py.cpp",),
("Axis.h","Class for Axis of coordination system",""),
("BoundBox.h","bounding boxes of the 3D part, define max{x,y,z} and min{x,y,z}",""),
("Rotation.h","define class and method for rotation an objecti n 3D space",""),
("Placement.h" ,"class to place/relocate an object in 3D space","see official api doc: <https://www.freecadweb.org/api/Placement.html>"),
("DualNumber.h" "Dual Numbers are 2-part numbers like complex numbers, but different algebra",""),
("DualQuaternion.h" "Quaternion of Dual Numbers for placement interpolation, etc",""),
("Vector.h" "Template class represents a point, direction in 3D space",
"""`typedef Vector3<float>  Vector3f;`
`typedef Vector3<double> Vector3d;`"""),
("Matrix.h" "Template class: Matrix4D for coordination translation and rotation",""),
("GeometryPyCXX.h","template class GeometryT<>",
"""This is a template class to provide wrapper classes for geometric classes like   `Base::Matrix4D, Base::Rotation Placement and Base::BoundBox` .
 Since the class inherits from `Py::Object` it can be used in the same fashion as  `Py::String, Py::List`, etc. to simplify the usage with them.
 """),
#
("Geometry related classes without *Py.cpp",),
("CordiniateSystem.h",  "XYZ only?","local cylindral coordination is common"),
("ViewProj.h","View Projection"),
("Builder3D.h","class Builder3D, InventorBuilder",
""" A Builder class for 3D representations without the visual representation of data.
 Nevertheless it's often needed to see some 3D information, e.g. points, directions,  when you program or debug an algorithm. For that purpose Builder3D was made.
 This class allows you to build up easily a 3D representation of some math and  lgorithm internals.  You can save this representation to a file and see it in an  Inventor viewer, or put it to the log.
"""),
("Tools2D.h","class Vector2D, BoundBox2D,Polygon2D, Line2D",""),
#
("Unit and physical quantity",),
("Unit.h","Physical unit like Newton, second for time",
"""
`struct  UnitSignature{9* int32_t}`   International System of Units (SI) has only 7 base unit
boost has its unit system;  OpenFoam also has its templated class for physical quantity.
OpenFOAM  uses a unit tuple of 7 foundamental SI base unit
"""),
("UnitScheme.h"," Base class for diff schemes like imperial, SI MKS(meter, kg, second) ,etc",
"""[Unit.cpp       UnitsApi.cpp     UnitsSchema.h             UnitsSchemaInternal.h Unit.h
UnitsApi.h       UnitsSchemaImperial1.cpp  UnitsSchemaMKS.cpp
UnitPyImp.cpp  UnitsApiPy.cpp   UnitsSchemaImperial1.h    UnitsSchemaMKS.h
UnitPy.xml     UnitsSchema.cpp  UnitsSchemaInternal.cpp
]"""),
("Quantity.h" ," define static quantity with unit like Force",
"""
"""),
#
("Important utility classes",),
("TimeInfo.h", "helper class to deal with time_t, currentDataTimeString()", ""),
("Base64.h","text encoding helper class for URL",""),
("Uuid.h" ,"a wrapper of QUuid class: unique ID 128bit",""),
("Handle.h" ,"class Base::Handled, Base::Reference<T>: Reference counting pattern",
"Implementation of the reference counting pattern.  Only able to instantiate with a class inheriting  Base::Handled."),
("Factory.h","Factory design pattern to create object",
""" to get the singleton instance of concrete class:
`ScriptFactorySingleton & ScriptFactorySingleton::Instance	(	void 		)`
"""),
("Observer.h" ,"Observer design pattern: define class Subject,Observer ",
"""`template <class MessageType> class Subject; ` """),
("Sequencer.h", "report Progress", "ConsoleSequencer, EmptySequencer",
"""
In the FreeCAD Gui layer there is a subclass of SequencerBase called ProgressBar
that grabs the keyboard and filters most of the incoming events.
If the programmer uses the API of SequencerBase directly to start an instance without due diligence with exceptions
then a not-handled exception could block the whole application so the user has to kill the application then.
"""),
("FutureWatcherProgress.h","progress report based on sequencer","it is derived from QObject, so can be used in Qt object event loop"),
("Tools.h","Main dealing with string encoding,  std::string <-> QString",""""""),
("XMLtools.h","include Xerces library header","")
]
