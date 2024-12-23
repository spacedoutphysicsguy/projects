from setuptools import setup, Extension
from Cython.Build import cythonize

__version__= "0.1.0b"
# Define the extensions (Cython modules)
extensions = [
    Extension("dual_autodiff_x.dual", ["src/dual_autodiff_x/dual.pyx"]),
]

# Call setup with cythonized extensions
setup(
    ext_modules=cythonize(extensions,
    compiler_directives={'language_level': "3"}),
    package_dir={"src": "src"},
    packages=["dual_autodiff_x"],

    # # Include only .so/.pyd files (compiled extensions), exclude source files
    package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
    # Ensure that wheels can be built
    zip_safe=False,
)