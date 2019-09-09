PartFolder=[
("MakeBottle.py", "good example of making complex geometry from  points to wires to face to solid", 
"""**class _PartJoinFeature** is a community contributed pure python, 
extending **Part::FeaturePython**,  *self.Type = \"PartJoinFeature\"* 
"""),
("JoinPartFeature.py","good example of pure python implemented Feature ",""""""),
("App/FT2FC.h","FreeType font to FreeCAD python related tool",""""""),
#
("App/FeatureReference.h", "Base class of all shape feature classes in FreeCAD",
 """class PartExport FeatureReference : public App::GeoFeature"""),
 ("App/PartFeature.h", "feature like Loft, Sweep, etc",),
("App/PartFeatures.h", "feature like Loft, Sweep, etc",),
("App/Primitive.h"," define primitive Vertex, Line,Plane, Cube,Sphere, Cone, Torus, Helix",
"""`class PartExport Primitive : public Part::Feature `"""),
("App/ImportIges.h","ImportIgesParts(App::Document *pcDoc, const char* Name)",
"""IGESControl_Reader aReader is used to load as PartFEatuer's shape
```
 Part::Feature *pcFeature = static_cast<Part::Feature*>(pcDoc->addObject
                ("Part::Feature", name.c_str()));
            pcFeature->Shape.setValue(comp);
```"""),
("App/TopoShape.h","wrapper of Topo_Shape of OpenCascade, represent CAD shape",
"""```
class PartExport ShapeSegment : public Data::Segment
class PartExport TopoShape : public Data::ComplexGeoData
//Boolean operation, feature loft, document save, import/export, getFaces/Segments
```"""),
("App/CrossSection.h","",""""""),
("App/FeatureBoolean.h","boolean operation Part::Feature cut, fusion, intersect",
"""```class Boolean : public Part::Feature
virtual BRepAlgoAPI_BooleanOperation* makeOperation(const TopoDS_Shape&, const TopoDS_Shape&) const = 0;
```"""),
("App/Geometry.h","define 2D geometry data, derived from Base::Persistence",""" save/restore,  Topo_Shape toShape()"""),
("App/Part2DObject.h","derived from Part::Feature, special 3D shape with Z=0",
""" Sketcher::SketchObject is derived from this class"""),
("Gui/ViewProviderPart.h","",
"""```class PartGuiExport ViewProviderPart : public ViewProviderPartExt
class ViewProviderShapeBuilder : public Gui::ViewProviderBuilder```"""),
("Gui/","",""""""),
("Gui/","",""""""),
]



"""
class PartExport PropertyPartShape : public App::PropertyComplexGeoData

struct PartExport ShapeHistory { typedef std::map<int, std::vector<int> > MapList; typedef std::vector<int> List; TopAbs_ShapeEnum type; MapList shapeMap; };
"""
