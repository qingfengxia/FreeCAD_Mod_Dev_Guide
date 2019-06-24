## combination the strength of FreeCAD and Salome

FreeCAD is best 2D and 3D CAD software, it is clear.

Salome is powerful platform to glue many open source CAE software, see <http://www.salome-platform.org/>
 Salome has plugin architecture, using Qt, Python, and have similar arch with FreeCAD.
![architecture of Salome](images/salome_arch.png)

[Documentation on integrating component to salome](http://docs.salome-platform.org/latest/gui/YACS/components.html)

Although there is feature listed in the website:
*Supports interoperability between CAD modeling and computation software (CAD-CAE link).*
CAD-CAE link, at least to FreeCAD, is missing in Salome platform.

Some example of opensource CAE Solvers:
- elmer (FEM+multiphysics),
- Code_Aster (FEM+multiphysics),
- OpenFOAM (FEM+CFD),
- Code_Saturne (CFD)
- bluefish for Boltzman method
- more if you search

Preprocessing and post-processing tools: Salome-Mesh/gmsh, ParaView

The processing of FreeCAD modeling-> Salome Meshing -> OpenFome Solver -> Paraview visualisation seems very promissing, and there has been an example.
[Tutorial for FreeCAD + Salome+OpenFoam cavity driving flow case](http://uberlinux.blogspot.co.uk/2015/01/tutorial-1lid-driven-cavity-in-openfoam.html)

[documentation for salome](http://docs.salome-platform.org/latest)

### commercial CAD and CAE solution

SolidWorks supports name attribute on solids in STEP import/export : you can define the name of solids/faces/edges/vertices in the GUI and this name is linked when exporting the part in STEP format.

Ansys workbench "Not only do we import geometric entities such as bodies, faces or edges, but we also support the import of such additional attributes as materials, selections of entities and design parameters", see more at [Leveraging Parametric CAD Models with ANSYS Bidirectional Interfaces ](http://www.ansys.com/Products/Simulation+Technology/Structural+Analysis/Structural+Technology+Leadership/Technology+Tips/Leveraging+Parametric+CAD+Models+with+ANSYS+Bidirectional+Interfaces)

Ansys workbench start the external CAD software, an "Ansys Link" menu appeared in CAD software.  After finish modeling in CAD software and close/jump to Ansys workbench. The geometry and named entities are ready to use. I believe IGES/STEP is used to transfer model.

### possible soluitions of open source software stack
FreeCAD could be embedded into Salome as "Paraview", since they are all based on Qt. While it is out of my knowledge. Embedded python


[example of embedding FreeCAD python module into Blender](https://www.freecadweb.org/wiki/Embedding_FreeCAD)

Even if, a 'contract' still needed to be defined for at least single direction information transfer (CAD model + namedSelection) to meshing tools, the meshing tool will never modify topology, e.g. beam thickness change in CAD model will not invalidate meshing rules and CAE solver setup, just updating internal cell position by meshing tool.

CAD named selection (*Group* in Salome, *namedSelection* in AnsysWorkbench) , contacting interface between bodies, material information exported could be useful to coordinate different CAE solver.

Post-processing is more independent, an Paraview macro (setup in GUI) should reply reach time after geometrical change.


[more CFD open source tools can be found at cfdonline](http://www.cfd-online.com/Links/soft.html)


### Exporting model and extra information

If embed attribute into STEP is hard, a bundle of XML + STEP could be used. see freecad.org/forum discussion of [Managing shapes names with STEP import/export](https://forum.freecadweb.org/viewtopic.php?t=3972)

A simple solution will be, Salome request a geometry be modeled and saved with predecided name and folder, and signal the finished event (Instead of close CAD software which takes time to open up). If no good and portable IPC is available, FileSystemWatcher polling by Salome (caller) would be enough.



Boundarycondition setup,
NamedSelection
Material


### IPC

Interprocess communication with other CAE software, file exchange is the first (COM, DBus, no portable way)

*subprocess.PIPE* is used in FreeCAD to communicate with external process, by catch up the stdin and stdout, as well as the returncode at the process exit.

Salome, using a higher level infrastructure.

https://github.com/mikeboers/PyAV/blob/master/examples/audio.py


Application.h key for embedding, same Qt version,   derived from App::Application

http://docs.enthought.com/mayavi/mayavi/auto/example_qt_embedding.html



