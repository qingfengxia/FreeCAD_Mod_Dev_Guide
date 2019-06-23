#  Learning OpenInventor/Coin3D

Coin3D is an open source implementation for OpenInventor spec/API, released in a less constrainted license, LGPL.

Usful links to learn OpenInventor programming:
<http://webee.technion.ac.il/~cgcourse/InventorMentor/The%20Inventor%20Mentor.pdf>
[Coin3D Online Document](http://doc.coin3d.org/Coin/annotated.html)


### Important classes in OpenInventor/Coin3D

`SoPath, SoNode, SoEngine` are three main categories of Object in Coin3D.
Classes are organised into modules, see <http://developer90.openinventor.com/APIS/RefManCpp/main.html>

Description from this online documentation is extracted for key classes.
See the brief description for classes: <http://coin3d.bitbucket.org/Coin/annotated.html>;

** Basic objects **

- SbXXX: Basic types like SbVec3f, SbMatrix, SbColor, SbString, SbTime; Containers like SbDict, SbList;  geometrical representation of basic shape like SbSphere; SbTypeInfo

- SoBase: ancester for most Coin3D ojbects, similar with *QObject*, FreeCAD's `Base::BaseClass`

> Top-level superclass for a number of class-hierarchies. SoBase provides the basic interfaces and methods for doing reference counting, type identification and import/export. All classes in Coin3D which uses these mechanisms are descendent from this class

```cpp
ref() unref() getName()
virtual SoType 	getTypeId (void) const =0
notify (SoNotList *nl) //observer pattern, notify Auditor
addAuditor (void *const auditor, const SoNotRec::Type type)
```

Qobject is the base object for all derived Qt objects, offering event, containner, property, type support.

![Inheritance chain of Coin3D](../images/classSoBase.png)

Example of inheritance chains:

Coin3D: `SoBase->SoFieldContainer->SoNode->SoGroup->SoShape`
FreeCAD: `BaseClass->App::PropertyContainer->App::DocumentObject->Part::Feature`

- SoType: Inventor provides runtime type-checking through the `SoType` class. `node->getTypeId().getName(); ` like `Base::TypeClass` in FreeCAD

> Basis for the run-time type system in Coin3D. Many of the classes in the Coin3D library must have their type information registered before any instances are created (including, but not limited to: engines, nodes, fields, actions, nodekits and manipulators). The use of `SoType` to store this information provides lots of various functionality for working with class hierarchies, comparing class types, instantiating objects from classnames, etc etc

- SoField: Top-level abstract base class for fields serializable, similar with `App::Property` in FreeCAD

> Fields is the mechanism used throughout Coin for encapsulating basic data types to detect changes made to them, and to provide conversion, import and export facilities. *SoSFXXX*:  Single Field with Base type wrapped (App::Property); *SoMFXXX*: Multiple Field (array of field). E.g. SoSFBool class is a container for an SbBool value.

- SoFieldContainer: serializaton(`App::PropertyContainer` in FreeCAD) function is built into `SoNode`

- SoBaseList	Container for pointers to SoBase derived objects.

> The additional capability of the SoBaseList class over its parent class, SbPList, is to automatically handle referencing and dereferencing of items as they are added or removed from the lists

** Scene organisation **

- SoDB: This class collects various methods for initializing, setting and accessing common global data from the Coin library

> Similar with `App::Document` in FreeCAD import and export into file. Directed Acyclic Graph is used for better performance, SoNodes are organised into database, serialization into text file *.iv .

> "The foundation concept in Open Inventor is the "scene database" which defines the objects to be used in an application. When using Open Inventor, a programmer creates, edits, and composes these objects into hierarchical 3D scene graphs (i.e., database). " Quoted from Open Inventor reference.

- SoNode: similar with `App::DocumentObject` in FreeCAD, has flags like ignore, override

> Base class for nodes used in scene graphs. Coin is a retained mode 3D visualization library (built on top of the immediate mode OpenGL library). "Retained mode" means that instead of passing commands to draw graphics primitives directly to the renderer, you build up data structures which are rendered by the library on demand

- SoGroup:  similar with `App::DocumentObjectGroup` in FreeCAD

> An `SoSwitch` node is exactly like an SoGroup except that it visits only one of its children. `SoShape` is derived from `SoGroup` Shared Instancing: share the SoShape, but seperate SoTransform, ref counting

- SoSeperator: State-preserving group node (derived from `SoGroup`), conprising SoColor, SoMaterial, SoTexture, SoShape, etc.

> Subgraphs parented by SoSeparator nodes will not affect the previous state, as they push and pop the traversal state before and after traversal of its children. Order (topdown, left to right) in SoDB (scene graph) is important to determine rendering, see exmaple in <http://developer.openinventor.com/content/34-creating-groups>. Scale node is only added to first Hydrogen SoGroup, but this scale applied to the second Hydrogen SoGroup. To isolate the effects of nodes in a group, use an SoSeparator node, which is a subclass of SoGroup . Before traversing its children, an SoSeparator saves the current traversal state. When it has finished traversing its children, the SoSeparator restores the previous traversal state. Nodes within an SoSeparator thus do not affect anything above or to the right in the graph.

- SoPath: Container class for traversal path for nodes in scene database, see also `SoFullPath, SoNodeKitPath`. It is derived from `SoBase`, not `SoFieldContainer`, it is different from `App::PropertyLink` in FreeCAD.

> "SoPath objects contain a list of SoNode pointers and a list of child indices. Indices are necessary to disambiguate situations where a node uses the same node as a child multiple times. Similarly, UUID and getUniqueName() in FreeCAD make the unique reference to Document Objects."

- SoBaseKit: base class for all NodeKit (not a SoGroup) which create groups of scene graph nodee. Parts are added as hidden children, accessable only by the methods of SoBaseKit and its derived classes.

- SoSeparatorKit: A nodekit that is used for creating nodekit hierarchies. SoSeparatorKit contains a transform part, a childList part, and a few others like pickStyle , appearance in its catalog.

** Scene rendering **

- SoAnnotation: (Derived from SoSeparator) node draws all its child geometry on top of other geometry.

> This group-type node uses delayed rendering in combination with Z-buffer disabling to let its children transparently render their geometry on top of the other geometry in the scene.

- SoShape: SoCube/SoCone/SoCynlinder/SoSphere/SoText/SoImageSoNurbsCurve/SoNurbsSurface/SoImage: (`App::GeoFeature` in FreeCAD??)

> For rendering basic shpapes.Insert a shape into the scenegraph and render with the current material, texture and drawstyle settings (if any, otherwise the default settings are used)

- SoDetail: Superclass for all classes (SoCubeDetail...) storing detailed information about particular shapes.

> Detail information about shapes is used in relation to picking actions in Coin. They typically contain the relevant information about what particular part of the shape a pick ray intersected with

** misc objects **

- SoEngine: SoEngine (derived from SoFieldContainer, as a sibling of SoNode) is the base class for Coin/Inventor engines.

> Engines enables the application programmers to make complex connections between fields, for example, animation.

- SoVRMLXXX: VRML file import and export
- SoAudioDevice: 3D sound
- SoSensor: for scene manipulation
- SoCamera: belongs only to scene
- SoLight: belongs only to scene

- SoEnvironment: gloable settings

- ScXml: Namespace for static ScXML-related functions

- SoElement:  base class for classes used internally for storing information in Open Inventor's traversal state list.

- SoSelection: Manages a list of selected nodes, Derived from SoSeparator.

> Inserting an SoSelection node in your scene graph enables you to let the user "pick" with the left mousebutton to select/deselect objects below the SoSelection node

- SoSFEnum/SoMFEnum: single or multiple Enumeration fields

** Action, event and callback **

- SoAction: SoCallback(object oriented)

> Applying actions is the basic mechanism in Coin for executing various operations on scene graphs or paths within scene graphs, including search operations, rendering, interaction through picking, etc

- SoEvent: 	Base class for keyboard/mouse/motion3d event
- SoEventCallback:  nodes in the scenegraph for catching user interaction events with the scenegraph's render canvas
- SoCallback:	Node type which provides a means of setting callback hooks in the scene graph.

> By inserting SoCallback nodes in a scene graph, the application programmer can set up functions to be executed at certain points in the traversal
- SoCallbackAction:	Invokes callbacks at specific nodes.This action has mechanisms for tracking traversal position and traversal state.

> In combination with the ability to pass geometry primitives to callback actions set by the user, this does for instance make it rather straightforward to extract the geometry of a scene graph

- SoCallbackList	The SoCallbackList is a container for callback function pointers, providing a method for triggering the callback functions

see <http://developer.openinventor.com/content/chapter-10-handling-events-and-selection>


### Window System integration

Previous (deprecated) windwos system integration lib:

- SoWin: for win32 windows platform
- SoXt: for XWindows for *nix system
- SoQt: integrating with Qt window system

**Quater: the most updated bind with Qt**
Quarter is superior over SoQt providing OpenGL widget viewer.  Release 1.0.0 is the first major release. Quarter 1.0 is only usable with Coin-3.x and Qt-4.x.

*Quarter* is a light-weight glue library that provides seamless integration between Systems in Motions's Coin high-level 3D visualization library and Trolltech's Qt 2D user interface library, to replace SoQt. The functionality in Quarter revolves around QuarterWidget, a subclass of `QGLWidget`. This widget provides functionality for rendering of Coin scenegraphs and translation of `QEvents` into SoEvents. Using this widget is as easy as using any other `QWidget`.

[Quarter / include / Quarter / QuarterWidget.h](https://bitbucket.org/Coin3D/quarter/src/a941589f50f9c88555f558190d489717a7b658f6/include/Quarter/QuarterWidget.h?at=default&fileviewer=file-view-default)

For developers targeting multi-platform - 'Quarter' provides a seamless integration with the Qt framework. <https://en.wikipedia.org/wiki/Coin3D>

<http://doc.coin3d.org/Quarter/>