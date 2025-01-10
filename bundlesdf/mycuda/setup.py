# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.

from setuptools import setup
import os
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

code_dir = os.path.dirname(os.path.realpath(__file__))

# NVCC 和 GCC 编译标志
nvcc_flags = ['-Xcompiler', '-O3', '-std=c++17', '-U__CUDA_NO_HALF_OPERATORS__', '-U__CUDA_NO_HALF_CONVERSIONS__', '-U__CUDA_NO_HALF2_OPERATORS__']
c_flags = ['-O3', '-std=c++17']

setup(
    name='common',
    ext_modules=[
<<<<<<< Updated upstream
        CUDAExtension('common', [
            'bindings.cpp',
            'common.cu',
        ],extra_compile_args={'gcc': c_flags, 'nvcc': nvcc_flags}),
        CUDAExtension('gridencoder', [
            f"{code_dir}/torch_ngp_grid_encoder/gridencoder.cu",
            f"{code_dir}/torch_ngp_grid_encoder/bindings.cpp",
        ],extra_compile_args={'gcc': c_flags, 'nvcc': nvcc_flags}),
    ],
    include_dirs=[
        "/usr/local/include/eigen3",
        "~/anaconda3/envs/py39/include/eigen3",
=======
        CUDAExtension(
            'common', 
            [
                'bindings.cpp',
                'common.cu',
            ],
            extra_compile_args={'cxx': c_flags, 'nvcc': nvcc_flags},
        ),
        CUDAExtension(
            'gridencoder',
            [
                f"{code_dir}/torch_ngp_grid_encoder/gridencoder.cu",
                f"{code_dir}/torch_ngp_grid_encoder/bindings.cpp",
            ],
            extra_compile_args={'cxx': c_flags, 'nvcc': nvcc_flags},
        ),
>>>>>>> Stashed changes
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
