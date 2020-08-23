**Module developer's guide to FreeCAD source code**

by [Qingfeng Xia](https://www.researchgate.net/profile/Qingfeng_Xia) 2016~

by [Luzpaz 2019~](https://github.com/luzpaz)

download the latest version from `pdf` folder of this repo

## [Changelog](./changelog.md)
- 2015-09-18 version 0.1 *for FreeCAD version 0.16-dev*

- 2016-09-18 version 0.2 *for FreeCAD version 0.17-dev*

- 2019-06-18 start again to work towards version 0.3 *for FreeCAD version 0.19-dev*

## Plan and progress

This book should be updated for the recent release, esp. after migration to Python3 + Pyside2. I plan another release for FreeCAD 0.19 dev near Xmas time.

## [License of this book](http://creativecommons.org/licenses/sa/4.0/)

Similar as FreeCAD document license CC-BY 3.0

This ebook is licensed as [Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)

see the full  text in this repo and also online  <https://creativecommons.org/licenses/by-sa/4.0/>
In short, this license let you 
> Share — copy and redistribute the material in any medium or format
> Adapt — remix, transform, and build upon the material for any purpose, even commercially. 

Just request: share your derived work(share-alike) and credit the author (attribution)

## Acknowledge to developers of FreeCAD

Original/lead developers:

- [Jürgen Riegel](http://juergen-riegel.net/)
- [Werner Mayer]()
- [yorik van havre](https://www.facebook.com/yorikvanhavre)

Add all contributors see <https://www.freecadweb.org/wiki/Contributors>

## Target audiences: new module developers

Make sure you are familiar with FreeCAD workbench GUI and API as a user:

- [Foundamental document on official wiki for FreeCAD](https://www.freecadweb.org/wiki/)
- [FreeCAD python API document](https://www.freecadweb.org/api/)
- [single file PDF user manual for quick start](http://sourceforge.net/projects/free-cad/files/FreeCAD%20Documentation/)

## Doxygen documents links

[Doxygen generated online documentation of source  for 0.16dev, will be delete soon](https://www.iesensor.com/FreeCADDoc/0.16-dev/)

[Doxygen generated online documentation of source  for 0.19dev on 2019-06-24](https://www.iesensor.com/FreeCADDoc/0.19/modules.html)

## Why I want to write this book

- Learn the software architecture of FreeCAD: a large open source project
- Learn to use git to contribute to open source projects like FreeCAD
- Save time for new developers to explore the source code of FreeCAD
- Record personal note and lesson during writing/contributing code to FreeCAD
- Some chapters of this ebook is seeking to be merged into official wiki after reviewed as usable

My research: ["Automated and Intelligent Engineering Design"](https://www.researchgate.net/project/Automated-and-Intelligent-Enigneering-Design)

## How to contribute to this ebook

- write on unfinished topics/chapters listed in [todo.md](./todo.md)
  fork and pull request `git clone https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide.git`

- file bug for outdated code analysis
  As this book is about code analysis while FreeCAD is under heavy development, source codes quoted may outdated quickly.
  Please point out my report bugs in [ this github issues board](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/issues)
  
- This ebook is pre-processed by a python script, see more details in the [scripts](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/scripts) folder's Readme.

  There are some anchor texts like:

  -  [src/*.h/cpp] are processed into link to the latest official FreeCAD source.
  - some another anchors "## folders ... ", which will be marked out soon more explicitly

## Acknowledgement to my family

This work is not funded to my employers (Oxford Unviersity, UKAEA) by the time 2019. It is a community voluntary work, thank every one review, contribute to this book.

Qingfeng Xia thanks for my wife Ms J. Wang, and other family members' for the housework exempt to complete this work.

****************************************************
