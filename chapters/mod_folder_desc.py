#introduction to each module in src/Mod
ModFolder=[
("Mechanical Engineering, CAD and CAM",),
("Part","make primitive 3D objects like cube, cylinder, boolean operaton",
"""The	Part	module	is based on	the professional CAD kernel ,	 OpenCasCade,	 objects and	 functions."""),
("OpenSCAD","Extra OpenCasCade functions","""use the high level API in Part module instead"""),
("PartDesign","modelling	 complex	 solid	 part from 2D sketch","""The	 Part	 Design	 Workbench	 provides	 tools	 for	 modelling	 complex	 solid	 parts	 and	 is	 based	 on	 a	 Feature	 editing
methodology	to	produce	a	single	contiguous	solid.	It	is	intricately	linked	with	the	Sketcher	Workbench."""),
("Draft","draw and modify 2D objects, traditional 2D engineering drawing,",
"""The	Draft	workbench	allows	to	quickly	draw	simple	2D	objects	in	the	current	document,	and	offers	several	tools	to	modify	them
afterwards.	 Some	 of	 these	 tools	 also	 work	 on	 all	 other	 FreeCAD	 objects,	 not	 only	 those	 created	 with	 the	 Draft	 workbench.	 It
also	provides	a	complete	snapping	system,	and	several	utilities	to	manage	objects	and	settings."""),
("Drawing","put 3D model to paper, can save to DXF and SVG format",""""""),
("Sketcher","buld up 3D part from 2D sketch used in PartDesign",""""""),
("Assembly","Assembly of part","""Constraint of """),
("Cam","Computer aided machining (CAM), CNC machining",""""""),
("Path","Tool path for CAM",""""""),
#
("Civil Engineering",),
("Idf","used by Arch module",""""""),
("Arch","CAD for civil engineering, like desing of a house",
"""The	 Arch	 workbench	 provides	 modern	 BIM 	 workflow	 to	 FreeCAD,	 with	 support	 for	 features	 like	 IFC	 support,	 fully	 parametric
architectural	 entities	 such	 as	 walls,	 structural	 elements	 or	 windows,	 and	 rich	 2D	 document	 production.	 The	 Arch	 workbench
also	feature	all	the	tools	from	the	Draft	Workbench"""),
("Ship","Build 3D model (hull)for ship ",""""""),
#
("Computer aided engineering (CAE)",),
("Points","points cloud from 3D scanning",""""""),
("ReverseEngineering","build 3D part from points cloud",""""""),
("Raytracing","to render lighting 3D model more vivid as in physical world",
"""generate	photorealistic images of your	models	by	rendering	them with	an external renderer. The	 Raytracing	 workbench	 works	 with	 templates,	 the	 same	 way	 as	 the	 Drawing	 workbench,	 by	 allowing	 you	 to	 create	 a Raytracing project	 in which	 you	 add	 views	 of	 your	 objects.	 The	 project	 can	 then	 be	 exported	 to	 a	 ready-to-render	 file,	 or	 be rendered	directly."""),
("MeshPart","",""""""),
("Mesh","convert part into triangle mesh for rendering (tessellation)",""""""),
("Fem","Fenite element analysis for part design",""""""),
("Robot","Robot simulator",""""""),
("Utilities",),
("Plot","2D plot,like XYplot, based on matplotlib","""allows	 to	 edit	 and	 save	 output	 plots	 created	 from	 other	 modules	 and	 tools"""),
("Image","import various image format, draw them in 3D plane",""""""),
("Spreadsheet","Excel like data view widget",""""""),
#
("Testing facility",),
("Inspection","Testing",""""""),
("Test","Workbench for self testing",""""""),
("Sandbox","Testing",""""""),
#
("Meta workbench",),
("Web","web view of FreeCAD",""""""),
("Start","start page of FreeCAD",""""""),
("Complete","show all toolbar from loadable modules",""""""),
#
("Module not visible to workbench users",),
("Import","",""""""),
("JtReader","",""""""), 
("Material","define standard material property, like density, elastic modulus",
"""not visible to workbench users, used by Fem module"""),
("TemplatePyMod"," a collection of python example DocumentObject, ViewProvider","""""")
]
