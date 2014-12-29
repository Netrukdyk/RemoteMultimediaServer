from distutils.core import setup
import py2exe
import glob

setup(
	windows=[{
			"script" : "remote.pyw",
			"icon_resources": [(0, "icon.ico")]
	}],
	options={
			"py2exe":{
					"includes": ["PySide.QtXml"],
					"unbuffered": True,
					"optimize": 2,
					"bundle_files": 3,
					"compressed": True
			}
	},
	data_files=[("",["remote.ui","icon.ico"]),
				("images",glob.glob('images/*')),
				("imageformats",["C:\Python34\Lib\site-packages\PySide\plugins\imageformats\qico4.dll"])
	],
	zipfile = None
)