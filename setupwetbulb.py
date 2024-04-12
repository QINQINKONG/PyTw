from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
	"wetbulb",
        ["wetbulb.pyx"],
        libraries=["m"],
        extra_compile_args=['-qopenmp','-Ofast'],
        extra_link_args=['-qopenmp'],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    )
]

setup(
    name='wetbulb',
    ext_modules=cythonize(ext_modules,annotate=True,language_level = "3"),
    zip_safe=False,
    include_dirs=[numpy.get_include()]
)
