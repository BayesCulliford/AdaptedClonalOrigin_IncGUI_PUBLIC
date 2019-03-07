I leave this notes if you wish to continue working on this projet.

####################################################################################
#Installing Python and wxPython
####################################################################################
Here are a few basic instructions on how to open a .py file such that you can make edits to it. 
You would need python for compiling too, and 

We also explain how to install relevent modules.
 
For example wxpython is not part of python by default, and you
would have to specify that you want it installed. You can find more information on how to install it at
https://www.wxpython.org/pages/downloads/

Check if basic python has been installed by opening a python file within a command terminal using
"python name.py"

Note that in these instructions I do not discuss how to build something should "pip" fail. I don't 
think pip will fail though. 

Windows:
1.	There already should be a .exe file on the website that should automatically install the 
	software. The default directory, if I am not mistaken, should be C:\Python3.7

2. 	Once you have installed it, to open a .py file via a command terminal you need to set a PATH to the libraries. To do this
	just follow the instructions shown here https://geek-university.com/python/add-python-to-the-windows-path/
	where you need to set the enviromental paths to something like C:\Python37 depending on how you saved the python directory.

 
3.	Finally you need to install wxPython, in which providing that you have set the PATH correctly
	can be done via the command
	"pip install -U wxPython"
	If there are any other packages that I missed, you use the same technique except replace
	wxPython with the name of the package to install. 

Mac:
1.	If I am not mistaken Mac should have python installed be default, although you might want to
	the current version of it. So try typing in
	"python3 --version" 
	or
	"python2 --version"
 	If you have no variants of Python3 then there is risk of certain commands mentioned in the GUI 
	not working so definiately upgrade if it is Python2.7 
	Otherwise You need to use the homebrew bootstrap, more information can be found at https://realpython.com/installing-python/
	
2.	I am not sure if you should be able to use the python command by default. Othewise you would need to set the PYTHONPATH 
	variable and do the following code, assuming mrdir is where the Python37 (or otherwise) folder is located,
	PYTHONPATH="/Me/mydir:$PYTHONPATH"
	export PYTHONPATH

3.	Finally you need to install wxPython, in which providing that you have set the PATH correctly
	can be done via the command
	"pip install -U wxPython"
	If there are any other packages that I missed, you use the same technique except replace
	wxPython with the name of the package to install. 

Linux:
Linux is a little trickier, becaues there are different distributions of linux such as Ubuntu or CentOS. 

1. 	Most importantly though python is in fact installed on linux by default, at least for most distributions. 
	So the first thing to check is what version is installed via 
	"python3 --version"
 	If you have no variants of Python3 then there is risk of certain commands mentioned in the GUI 
	not working so definiately upgrade if it is Python2.7 
	If you want to just install the newest version of Python3 then use the link below for platform dependent instructions
	https://realpython.com/installing-python/

2.	Installing a new version of wxPython is platform dependent, overall you need to know your linux distribution
	For example if you were to install something on Ubuntu linux you usually download it via the URL, such as
	"pip install -U \ -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \ wxPython"
	for more information on where these files see https://extras.wxpython.org/wxPython4/extras/linux/gtk3/

3. 	Otherwise you should able to run python naturally, providing that you everything in the correct bins etc.



####################################################################################
#Installing Pyinstaller
####################################################################################

Pyinstaller works on Windows, Mac and Linux. This is the software used to compile files into an executable

The output may take different forms depending on the operating system. 
I will give the methods for several options on how to compile, and you 
can pick which is the most appropiate given the task. 

While the current version of Pyinstaller is 3.4, I have been personally been successful compiling 
files using it. 

MOST IMPORTANTLY, the reason we need to do this in seperate OS because pyinstaller cannot
cross compile for different OS. For something to work in linux it must be compiled in linux
For something to work in Mac it needs to be compiled in a Mac.

Information can be found here 
https://pyinstaller.readthedocs.io/en/stable/installation.html
https://www.youtube.com/watch?v=lOIJIk_maO4

#######################
#INSTALLATION FOR WINDOWS, 

1.	Prerequite software needs to be installed first, although they may already exist on your system
	Nevertheless using pip will automatically tell if something is installed or not.
	Firstly install PyWin32 (although it should be installed already) by using
	"pip install pywin32"
	Same goes for pypiwin32
	"pip install pypiwin32"
	and finallly the pefile package
	"pip install pefile"

2.	Then just install pyinstaller by
	"pip install pyinstaller"
	or if you need an upgraded version
	"pip install --upgrade pyinstaller"

3.	To verify installation type in 
	"pyinstaller --version"
	Or alternatively go to your files and find it installed in C:\Python34\Scripts

#######################
#INSTALLATION FOR LINUX, 

1.	The prerequistes are a little different. It requires the "ldd" terminal application
	to discover the shared libraries required by each program or shared library. 
	It is found in either the distribution package dlibc of libc-bin, therefore do
	"pip install glibc"
	or otherwise try "libc-bin"
	We also require the "objdump" terminal application to extract information from object
	files and the "objcopy" terminal application to append data to the bootloader. These are 
	found in "binutils" so do
	"pip install binutils"
	Depending on the linux distribution there might be more stuff that you need to implement 
	so chek out other details in https://pyinstaller.readthedocs.io/en/stable/requirements.html#linux

2.	I could be wrong on this, but I think it works for same for Windows so type
	"pip install pyinstaller"
	or if you need an upgraded version
	"pip install --upgrade pyinstaller"

3.	To verify installation type in 
	"pyinstaller --version"	
	Or alternatively go to your files and find it installed in
	"/usr/bin/"

#######################
#INSTALLATION FOR APPLE 

1.	I could not find a good amount of instructions, and whether it requires any prerequistes
	I really am unsure. for now I would recommend just try on the command terminal
	"pip install pyinstaller"

########################
#SHOULD THE ABOVE FAIL

1.	Download the tar.gz file at https://github.com/pyinstaller/pyinstaller/releases
2.	Open up the archive and you should see a file called setup.py, from here you use the command
	"python setup pyinstaller"
3.	Check if pyinstaller is installed correctly within the correct folders. They should be stored
	in /Python37/Scripts be it in Windows, Mac or Linux


Overall you should be able to use the commands "pyinstaller" and ""pyi-makespec" which
are the only files you need to pay attention to.

####################################################################################
#Compiling the code: Basic
####################################################################################

This section goes over basic options to compile.

More information can be found here
https://pyinstaller.readthedocs.io/en/stable/usage.html
https://pyinstaller.readthedocs.io/en/v3.3.1/spec-files.html
##############
#General options

Here are the main options which I feel like are the most useful to use. 
Although I discuss compiling multiple files in a seperate section.

1.	If we want a very simple installation we can use
	"pyinstaller name.py"
	or to be more specific
	"pyinstaller --onedir name.py"
	this creates a folder called dist which has an executable that can be 
	distributed to everyone.
	By default it has all the relvent python packages, including ones, compiled
	within a folder. See further below for how to compile everything to one executable. 

2.	If we want to apply an icon to the executable file, then we need to use
	"pyinstaller --icon=sampleicon.ico name.py"
	this can only be done in Windows and Mac, not Linux

3.	If we want to remove the automatically generated command terminal in Windows and Mac
	compilations then we can state
	"pyinstaller --windowed name.py"
	without this option, a command terminal automatically loads up. 
	Alternatively you can specify an open console window via
	"pyinstaller --console name.py"
	but this command is not usually needed at least in Windows, a terminal is already loaded.
	Again this can only be done in Windows and Mac, not Linux.

4.	We may also want to compile the executable into one single file. 
	DO NOT GIVE ADMIN PRIVELAGES TO A ONE-FILE EXECUTABLE. This is due to security reasons.

####################################################################################
#Compiling the code: Editing .spec files to include additional files/folders
####################################################################################
Here we discuss adding additional files to be compiled with the main python script
As far as I can tell, --add-data does not work or at least how it works to work 
varies with the OS. So it might be easier to add files but you 

See for more information
https://pyinstaller.readthedocs.io/en/v3.3.1/spec-files.html
https://pythonhosted.org/PyInstaller/man/pyi-makespec.html
	
Basically you need, 
1.	To create the basic blueprint for a .spec file, with most standard options etc, you use the following
	"pyi-makespec nameofpythonscript.py"
2. 	Then you make edits to your .spec file, these will be explained below. 
3.	Once you have the .spec file then you install it by using
	"pyinstaller name.spec"

When you open a spec file you will notice a list called "Analysis" and the bits you should pay attention to are,

1. 	The first argument which gives both the name of the spec file and usually the name of the python file,
	I think there is an argument as well that specificies the names of the spec file and python file seperately
	but you won't really need to use it.

2. 	Then there is pathex which shows the directory of where to compile.

3.	MOST IMPORTANTLY, create a blueprint of a .spec file does not always inherit all the additional 
	libraries such as wx or subprocess. It could depending on the operating system, but they were
	not added into the .spec file when I tested it
	Therefore  you would need to state these manually within the hiddenimports attribute, for example
	"hiddenimports=[('wx'), ('os')]". 

4.	The one thing you would be considering the most is the "datas" attribute. For example to add a single
	readme you would have 
	"datas=[('Readme.txt', '.')]"
	Note that the '.' indicates that we don't want something to be put into a seperate folder
	To specify entire folders containing a certain text you would use '*' such that you have 
	"datas=[('Readme.txt', '.'), (/myfolder/*.txt,'.')]"
	Or alternatively a complete folder, and for example we may want to put all items
	into the 'datafolderforbuild' folder,
	"datas=[('/myfolder', 'datafolderforbuild')]"

5.	Otherwise if you want to include custom modules, then you use the binaries keyword. For example
	"binaries[('MyCustomClass.dylib', '.')]"

####################################################################################
#Compiling the code: Compiling all files into a single executable
####################################################################################

You can define compiling all relevent python libraries and other files into a single executable
through pyinstaller or via the .spec files.

1.	Given a single python file you can use --onefile 
	"pyinstaller --onefile name.py"
2.	Using a spec file just add in the --onefile during its creation,
	"pyu-makespec --onefile name.py"
	followed by the standard instructions of compiling a .spec file. You could make a 
	few alterations to an existing .spec file to make sure it compiles into one executable, 
	but this requires quite a few things to make and there is a risk you could have a .spec
	file that doesn't work 
