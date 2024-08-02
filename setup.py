import platform
from setuptools import setup, Extension

include_dirs = ["/usr/local/opt/jpeg-turbo/include", "/opt/intel/oneapi/ipp/2021.12/include/ipp"]
library_dirs=["/usr/local/opt/jpeg-turbo/lib", "/opt/intel/oneapi/ipp/2021.12/lib"]
sources=["accimagemodule.c", "jpegloader.c", "imageops.c"]
if platform.system() == "Windows":
    include_dirs = ["C:/libjpeg-turbo64/include", "C:/Program Files (x86)/Intel/oneAPI/ipp/2021.10/include/ipp"]
    library_dirs=["C:/libjpeg-turbo64/lib", "C:/Program Files (x86)/Intel/oneAPI/ipp/2021.10/lib"]
    sources=["accimagemodule.c", "libfmemopen.c", "jpegloader.c", "imageops.c"]

accimage = Extension(
    "accimage",
    include_dirs=include_dirs,
    libraries=["jpeg", "ippi", "ipps"],
    library_dirs=library_dirs,
    sources=sources,
)

setup(
    name="accimage",
    version="0.2.0",
    description="Accelerated image loader and preprocessor for Torch",
    author="Marat Dukhan",
    author_email="maratek@gmail.com",
    ext_modules=[accimage],
)
