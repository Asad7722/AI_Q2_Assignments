{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "NgUeapcvmIRh"
   },
   "source": [
    "# **Assignment For Numpy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yhr3JicwnA-4"
   },
   "source": [
    "Difficulty Level **Beginner**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hVPqDJ1SnKSh"
   },
   "source": [
    "1. Import the numpy package under the name np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "SePu31zKmgS-"
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "d0gO81krnL7g"
   },
   "source": [
    "2. Create a null vector of size 10 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "id": "2s6o2JPgnSBr"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[9.90219522e-312, 1.77863633e-322, 0.00000000e+000,\n",
       "        0.00000000e+000, 8.06638080e-308],\n",
       "       [1.27965878e+161, 1.14199269e-071, 7.73902349e-091,\n",
       "        3.34577573e-061, 8.34402861e-308]])"
      ]
     },
     "metadata": {},
     "execution_count": 78
    }
   ],
   "source": [
    "x=np.empty((2,5))\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BJTMK03fnS1w"
   },
   "source": [
    "3. Create a vector with values ranging from 10 to 49"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "qRXxXuWdnj1M"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,\n",
       "       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,\n",
       "       44, 45, 46, 47, 48])"
      ]
     },
     "metadata": {},
     "execution_count": 10
    }
   ],
   "source": [
    "x=np.arange(10,49)\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "n63lzg5Onkcn"
   },
   "source": [
    "4. Find the shape of previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "1FueBdqPn_q7"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "(39,)"
      ]
     },
     "metadata": {},
     "execution_count": 11
    }
   ],
   "source": [
    "x=np.arange(10,49)\n",
    "x.shape\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "AzMlQj1MoAVe"
   },
   "source": [
    "5. Print the type of the previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "AO9PYmdWoE1L"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "x=np.arange(10,49)\n",
    "x.dtype\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0qaKS13Yon-U"
   },
   "source": [
    "6. Print the numpy version and the configuration\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "id": "T3wY24e1oorh"
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "blas_mkl_info:\n  NOT AVAILABLE\nblis_info:\n  NOT AVAILABLE\nopenblas_info:\n    library_dirs = ['D:\\\\a\\\\1\\\\s\\\\numpy\\\\build\\\\openblas_info']\n    libraries = ['openblas_info']\n    language = f77\n    define_macros = [('HAVE_CBLAS', None)]\nblas_opt_info:\n    library_dirs = ['D:\\\\a\\\\1\\\\s\\\\numpy\\\\build\\\\openblas_info']\n    libraries = ['openblas_info']\n    language = f77\n    define_macros = [('HAVE_CBLAS', None)]\nlapack_mkl_info:\n  NOT AVAILABLE\nopenblas_lapack_info:\n    library_dirs = ['D:\\\\a\\\\1\\\\s\\\\numpy\\\\build\\\\openblas_lapack_info']\n    libraries = ['openblas_lapack_info']\n    language = f77\n    define_macros = [('HAVE_CBLAS', None)]\nlapack_opt_info:\n    library_dirs = ['D:\\\\a\\\\1\\\\s\\\\numpy\\\\build\\\\openblas_lapack_info']\n    libraries = ['openblas_lapack_info']\n    language = f77\n    define_macros = [('HAVE_CBLAS', None)]\n"
     ]
    }
   ],
   "source": [
    "np.version.full_version\n",
    "(np.__version__)\n",
    "(np.show_config())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZyUUiQf5oyvE"
   },
   "source": [
    "7. Print the dimension of the array in question 3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "pLXfuIqIo0vq"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "x=np.arange(10,49)\n",
    "x.ndim"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JYVMuFrqpBdV"
   },
   "source": [
    "8. Create a boolean array with all the True values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "id": "3apZsISzpFKR"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ True,  True,  True,  True,  True,  True,  True,  True,  True,\n",
       "        True])"
      ]
     },
     "metadata": {},
     "execution_count": 80
    }
   ],
   "source": [
    "np.full((10), True, dtype=bool)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4zbBooWZpPBU"
   },
   "source": [
    "9. Create a two dimensional array\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "KfPQEiVIpdTo"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[1, 2, 3, 4],\n",
       "       [5, 6, 7, 8]])"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    " import numpy as np\n",
    "data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]\n",
    " arr=np.array((data2))\n",
    " arr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "do9wPAFbpqC7"
   },
   "source": [
    "10. Create a three dimensional array\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "ZCO_q-KZqAeW"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4],\n",
       "       [ 5,  6,  7,  8],\n",
       "       [ 9, 10, 11, 12]])"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "data3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]\n",
    "arr = np.array((data3))\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a4iysJ87qEeb"
   },
   "source": [
    "Difficulty Level **Easy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DehgqszSqjY6"
   },
   "source": [
    "11. Reverse a vector (first element becomes last)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "tfevmc4VqkWu"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "x=np.arange(0,10)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])"
      ]
     },
     "metadata": {},
     "execution_count": 15
    }
   ],
   "source": [
    "x=x[::-1]\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yoATXS-qqk_q"
   },
   "source": [
    "12. Create a null vector of size 10 but the fifth value which is 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0., 0., 0., 0., 1., 0., 0., 0., 0., 0.])"
      ]
     },
     "metadata": {},
     "execution_count": 4
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=np.zeros(10)\n",
    "x[4]=1\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RZRzOBbFsY0w"
   },
   "source": [
    "13. Create a 3x3 identity matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "va2ou0BHsvEj"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[1., 0., 0.],\n",
       "       [0., 1., 0.],\n",
       "       [0., 0., 1.]])"
      ]
     },
     "metadata": {},
     "execution_count": 17
    }
   ],
   "source": [
    "array_2D=np.identity(3)\n",
    "array_2D"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lnN5drkUs6o2"
   },
   "source": [
    "14. arr = np.array([1, 2, 3, 4, 5]) \n",
    "\n",
    "---\n",
    "\n",
    " Convert the data type of the given array from int to float "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "59EIQt6otKUB"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "metadata": {},
     "execution_count": 4
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr = np.array([1, 2, 3, 4, 5,])\n",
    "arr.dtype\n",
    "float_arr = arr.astype(np.float)\n",
    "float_arr.dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fSL2AKJetTes"
   },
   "source": [
    "15. arr1 =          np.array([[1., 2., 3.],\n",
    "\n",
    "                    [4., 5., 6.]])  \n",
    "                      \n",
    "    arr2 = np.array([[0., 4., 1.],\n",
    "     \n",
    "                   [7., 2., 12.]])\n",
    "\n",
    "---\n",
    "\n",
    "\n",
    "Multiply arr1 with arr2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "7VDXgRQDuJNV"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 0.,  8.,  3.],\n",
       "       [28., 10., 72.]])"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    "arr1 = np.array([[1., 2., 3.],\n",
    "\n",
    "            [4., 5., 6.]])  \n",
    "              \n",
    "arr2 = np.array([[0., 4., 1.],\n",
    "\n",
    "           [7., 2., 12.]])\n",
    "arr1*arr2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a8yJ438-uKni"
   },
   "source": [
    "16. arr1 = np.array([[1., 2., 3.],\n",
    "                    [4., 5., 6.]]) \n",
    "                    \n",
    "    arr2 = np.array([[0., 4., 1.], \n",
    "                    [7., 2., 12.]])\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Make an array by comparing both the arrays provided above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "3MPDaAlYueF3"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ True, False,  True, False,  True, False])"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "arr1 = np.array([1., 2., 3., 4., 5., 6.])\n",
    "arr2 = np.array([0., 4., 1., 7., 2., 12.])\n",
    "arr1>arr2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3xiD0eJluewk"
   },
   "source": [
    "17. Extract all odd numbers from arr with values(0-9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "J_qbt_EuvM7l"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([1, 3, 5, 7, 9])"
      ]
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=np.arange(10)\n",
    "x[x % 2 == 1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zpg5cyLsvPoZ"
   },
   "source": [
    "18. Replace all odd numbers to -1 from previous array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "id": "rXUV1-ULvQdd"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "x=np.arange(10)\n",
    "x[x % 2 == 1] = -1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FWpHTWTDvjvi"
   },
   "source": [
    "19. arr = np.arange(10)\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Replace the values of indexes 5,6,7 and 8 to **12**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "id": "ensZ3lqwvlSb"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4, 12, 12, 12, 12,  9])"
      ]
     },
     "metadata": {},
     "execution_count": 33
    }
   ],
   "source": [
    "arr = np.arange(10)\n",
    "arr[5:9]=12\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ib-vBffAv0zy"
   },
   "source": [
    "20. Create a 2d array with 1 on the border and 0 inside"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "id": "RmzcjNYrwDrM"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[1., 1., 1., 1., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 1., 1., 1., 1.]])"
      ]
     },
     "metadata": {},
     "execution_count": 38
    }
   ],
   "source": [
    "x=np.ones((5,5))\n",
    "x[1:-1,1:-1] = 0\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "E1diIFSEwEmh"
   },
   "source": [
    "Difficulty Level **Medium**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eGLZmNb_wKb4"
   },
   "source": [
    "21. arr2d = np.array([[1, 2, 3],\n",
    "\n",
    "                    [4, 5, 6], \n",
    "\n",
    "                    [7, 8, 9]])\n",
    "\n",
    "---\n",
    "\n",
    "Replace the value 5 to 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "id": "VdUnsUOZwJFz"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3],\n",
       "       [ 4, 12,  6],\n",
       "       [ 7,  8,  9]])"
      ]
     },
     "metadata": {},
     "execution_count": 56
    }
   ],
   "source": [
    "arr2d = np.array([[1, 2, 3],\n",
    "\n",
    "            [4, 5, 6], \n",
    "\n",
    "            [7, 8, 9]])\n",
    "arr2d[1:2, 1:2] = 12\n",
    "arr2d            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TEbFhlPZxaKO"
   },
   "source": [
    "22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])\n",
    "\n",
    "---\n",
    "Convert all the values of 1st array to 64\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "id": "eYzephU8xmsg"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[64, 64, 64, 64, 64, 64],\n",
       "       [ 7,  8,  9, 10, 11, 12]])"
      ]
     },
     "metadata": {},
     "execution_count": 57
    }
   ],
   "source": [
    "arr3d = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])\n",
    "arr3d[0] = 64\n",
    "arr3d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vZj0Ndvnx6f0"
   },
   "source": [
    "23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "id": "pM4e9YfdyHSv"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0, 1, 2])"
      ]
     },
     "metadata": {},
     "execution_count": 59
    }
   ],
   "source": [
    "arr2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])\n",
    "arr2d[0]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "C3dkW0lZyVps"
   },
   "source": [
    "24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "id": "IrrzK2xgygqV"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "metadata": {},
     "execution_count": 61
    }
   ],
   "source": [
    "arr2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])\n",
    "arr2d[1][1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "G3dLwOO9yyrE"
   },
   "source": [
    "25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "id": "5Bx4fqsLyqGD"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[2],\n",
       "       [5]])"
      ]
     },
     "metadata": {},
     "execution_count": 73
    }
   ],
   "source": [
    "arr2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])\n",
    "arr2d[:2, 2:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CQ9YST5jy0IL"
   },
   "source": [
    "26. Create a 10x10 array with random values and find the minimum and maximum values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "lhJPugjQzG6W"
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Original Array:\n[[0.35229118 0.77853896 0.63708852 0.31274702 0.62038523 0.45628243\n  0.80780266 0.39158738 0.78394019 0.58693838]\n [0.37712282 0.47489224 0.84008798 0.19248548 0.52266037 0.03290704\n  0.03050477 0.30447183 0.92572594 0.75387754]\n [0.69935336 0.82040182 0.50995248 0.48263901 0.19277048 0.89165436\n  0.00987154 0.78700084 0.07433394 0.96172457]\n [0.28828395 0.86375698 0.86194268 0.01773642 0.93235394 0.21756397\n  0.57489    0.07721936 0.11444255 0.922682  ]\n [0.08218288 0.25213179 0.19663404 0.0973404  0.07557042 0.12996625\n  0.80030601 0.27733376 0.52639004 0.41475388]\n [0.85454854 0.19836126 0.39468634 0.28661281 0.64076138 0.12669029\n  0.50742435 0.67651211 0.85080828 0.03670888]\n [0.66220393 0.4348172  0.97962718 0.97651503 0.52185615 0.31867006\n  0.59450778 0.62787164 0.22916976 0.54970146]\n [0.02293801 0.27825906 0.821964   0.52667653 0.61877625 0.38383225\n  0.92199738 0.81177931 0.00550047 0.76274106]\n [0.25517581 0.63970628 0.58805638 0.62720291 0.6142112  0.89938638\n  0.49229982 0.93017101 0.54892374 0.54712014]\n [0.61616585 0.45854702 0.21740622 0.40294372 0.85456146 0.96145571\n  0.46994589 0.7956849  0.40888063 0.77935268]]\nMinimum and Maximum Values:\n0.005500474032997693 0.9796271760175259\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.random.random((10,10))\n",
    "print(\"Original Array:\")\n",
    "print(x) \n",
    "xmin, xmax = x.min(), x.max()\n",
    "print(\"Minimum and Maximum Values:\")\n",
    "print(xmin, xmax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cAgDt6KazHk6"
   },
   "source": [
    "27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "---\n",
    "Find the common items between a and b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "kBXZanxIzs_F"
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[2 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array((1,2,3,2,3,4,3,4,5,6))\n",
    "b = np.array((7,2,10,2,7,4,9,4,9,8))\n",
    "print(np.intersect1d(a, b)) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lF9IzWOAztpD"
   },
   "source": [
    "28. a = np.array([1,2,3,2,3,4,3,4,5,6])\n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "\n",
    "---\n",
    "Find the positions where elements of a and b match\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "JR-mHQLH0HY_"
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[2 4]\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "(array([1, 3, 5, 7], dtype=int64),)"
      ]
     },
     "metadata": {},
     "execution_count": 17
    }
   ],
   "source": [
    "a = np.array((1,2,3,2,3,4,3,4,5,6))\n",
    "b = np.array((7,2,10,2,7,4,9,4,9,8))\n",
    "print(np.intersect1d(a, b)) \n",
    "np.where(a==b)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "mMDiefpH0H1x"
   },
   "source": [
    "29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "gfc1Lpf81ZSR"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ True,  True, False,  True, False,  True,  True])"
      ]
     },
     "metadata": {},
     "execution_count": 19
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) \n",
    "data = np.random.randn(7, 4)\n",
    "names != 'Will'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "52zEjDMf1aXS"
   },
   "source": [
    "30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "id": "8RYG0kLO1mHw"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ True, False, False,  True, False, False, False])"
      ]
     },
     "metadata": {},
     "execution_count": 24
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "data = np.random.randn(7, 4)\n",
    "(names != 'Will') & (names != 'Joe')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q7hjf2bd2dCY"
   },
   "source": [
    "Difficulty Level **Hard**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b48g7aRA2jVM"
   },
   "source": [
    "31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "id": "EbwfSCrW2f9_"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[7.34016581, 7.53113875, 6.19097033],\n",
       "       [6.26635479, 9.92184558, 6.56263242],\n",
       "       [5.10575368, 9.17175335, 8.94360863],\n",
       "       [5.54066268, 8.08345238, 6.85172606],\n",
       "       [6.87892438, 6.53722311, 8.18899409]])"
      ]
     },
     "metadata": {},
     "execution_count": 32
    }
   ],
   "source": [
    "x=np.random.uniform(5,10, size=(5,3))\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ei_nDHtO3qBk"
   },
   "source": [
    "32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "id": "phOxVpBM4M6D"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[[ 3.05946824,  3.51051937,  8.49770926, 13.10083371],\n",
       "        [ 4.4066042 ,  2.32274155, 15.1956963 ,  9.23762858]],\n",
       "\n",
       "       [[13.29273057, 13.15008163, 12.56188779,  1.99615453],\n",
       "        [ 1.744035  , 10.96566283,  1.94284239,  9.00165564]]])"
      ]
     },
     "metadata": {},
     "execution_count": 34
    }
   ],
   "source": [
    "x=np.random.uniform(1,16, size=(2, 2, 4 ))\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "uyiQaMjA4d_x"
   },
   "source": [
    "33. Swap axes of the array you created in Question 32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "id": "w2m9p8064VtR"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[[ 6.60328056,  4.98981487],\n",
       "        [ 7.23797347,  8.65948817]],\n",
       "\n",
       "       [[14.88918861,  4.87281922],\n",
       "        [13.41228399,  5.05864196]],\n",
       "\n",
       "       [[13.17657039, 13.79332712],\n",
       "        [ 1.25752781, 14.25988841]],\n",
       "\n",
       "       [[ 7.17558702, 15.18504843],\n",
       "        [14.83637061, 14.19399083]]])"
      ]
     },
     "metadata": {},
     "execution_count": 37
    }
   ],
   "source": [
    "x=np.random.uniform(1,16, size=(2, 2, 4 ))\n",
    "y=np.transpose(x)\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2dlU_yUR4mVZ"
   },
   "source": [
    "34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "id": "tmBabEJ-5JgB"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,\n",
       "       2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])"
      ]
     },
     "metadata": {},
     "execution_count": 45
    }
   ],
   "source": [
    "arr = np.arange(10)\n",
    "np.sqrt(arr)\n",
    "np.where(arr<=0.5,0,arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SNAM4dpu5RKA"
   },
   "source": [
    "35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " x = np.random.randn(12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " y = np.random.randn(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([-0.61237171, -1.22692236, -0.78228094, -0.95447881, -0.61028803,\n",
       "       -1.04021464, -0.70206808, -0.64912903, -0.31610992,  1.58727698,\n",
       "        1.90959404,  0.56959919])"
      ]
     },
     "metadata": {},
     "execution_count": 55
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 0.86366145, -0.36356808,  0.88756661,  0.36361423,  1.67459157,\n",
       "        1.75060305, -2.2441182 ,  1.06296737,  0.27501981,  0.41129829,\n",
       "       -1.07193429, -0.93362083])"
      ]
     },
     "metadata": {},
     "execution_count": 56
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 0.86366145, -0.36356808,  0.88756661,  0.36361423,  1.67459157,\n",
       "        1.75060305, -0.70206808,  1.06296737,  0.27501981,  1.58727698,\n",
       "        1.90959404,  0.56959919])"
      ]
     },
     "metadata": {},
     "execution_count": 58
    }
   ],
   "source": [
    "np.maximum(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fz_bpqm28qmD"
   },
   "source": [
    "36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "\n",
    "---\n",
    "Find the unique names and sort them out!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array(['Bob', 'Joe', 'Will'], dtype='<U4')"
      ]
     },
     "metadata": {},
     "execution_count": 60
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "np.unique(names)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dguMNzob870H"
   },
   "source": [
    "37. a = np.array([1,2,3,4,5])\n",
    "b = np.array([5,6,7,8,9])\n",
    "\n",
    "---\n",
    "From array a remove all items present in array b\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "id": "eCNJXPvK9IAr"
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "b = np.array([5, 6, 7, 8, 9])\n",
    "\n",
    "result = np.setdiff1d(a, b)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "gz4Dvd4b_Akh"
   },
   "source": [
    "38.  Following is the input NumPy array delete column two and insert following new column in its place.\n",
    "\n",
    "---\n",
    "sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) \n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "newColumn = numpy.array([[10,10,10]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "id": "lLWAJWJJ_I3d"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[34, 43, 73],\n",
       "       [82, 22, 12],\n",
       "       [53, 94, 66]])"
      ]
     },
     "metadata": {},
     "execution_count": 66
    }
   ],
   "source": [
    "sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])\n",
    "sampleArray"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[34, 73],\n",
       "       [82, 12],\n",
       "       [53, 66]])"
      ]
     },
     "metadata": {},
     "execution_count": 67
    }
   ],
   "source": [
    "sampleArray = np.delete(sampleArray , 1, axis = 1)\n",
    "sampleArray"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[34, 10, 73],\n",
       "       [82, 10, 12],\n",
       "       [53, 10, 66]])"
      ]
     },
     "metadata": {},
     "execution_count": 68
    }
   ],
   "source": [
    "arr = np.array([[10,10,10]])\n",
    "sampleArray = np.insert(sampleArray , 1, arr, axis = 1)\n",
    "sampleArray"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1lIfmbQt_J_W"
   },
   "source": [
    "39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])\n",
    "\n",
    "\n",
    "---\n",
    "Find the dot product of the above two matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([1., 2., 3., 4., 5., 6.])"
      ]
     },
     "metadata": {},
     "execution_count": 69
    }
   ],
   "source": [
    "x = np.array([1., 2., 3., 4., 5., 6.])\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "id": "fV2-vXcR_vmu"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 6., 23., -1.,  7.,  8.,  9.])"
      ]
     },
     "metadata": {},
     "execution_count": 71
    }
   ],
   "source": [
    "y = np.array([6., 23., -1, 7, 8, 9])\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "171.0"
      ]
     },
     "metadata": {},
     "execution_count": 72
    }
   ],
   "source": [
    "np.dot(x,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5U-4odUw_wP0"
   },
   "source": [
    "40. Generate a matrix of 20 random values and find its cumulative sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "id": "_oOHdiYEAF8N"
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 0.18093554,  0.23133003,  0.05183222,  1.18627728,  0.20578749,\n",
       "        0.64410343, -0.60545416,  0.31224335, -0.62266004, -0.15235313,\n",
       "       -0.56706571,  1.24905636, -0.33923353, -0.11619748, -0.56899491,\n",
       "       -0.64589554, -1.00381477, -0.70483625, -0.6303452 , -0.72388063])"
      ]
     },
     "metadata": {},
     "execution_count": 73
    }
   ],
   "source": [
    "x=np.random.randn((20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 1.,  3.,  6., 10., 15., 21.])"
      ]
     },
     "metadata": {},
     "execution_count": 75
    }
   ],
   "source": [
    "x.cumsum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Numpy-Assignment-PIAIC-Batch35-Q2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.3 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "2db524e06e9f5f4ffedc911c917cb75e12dbc923643829bf417064a77eb14d37"
    }
   }
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3-final"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}