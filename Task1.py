{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NAME: HARLEEN KAUR BHATIA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task # 2 - To Explore Supervised Machine Learning"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### PROBLEM STATEMENT:  In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just two variables.What will be predicted score if a student study for 9.25 hrs in a day?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### DATASET : http://bit.ly/w-data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import all libraries required\n",
    "import pandas as pd\n",
    "import numpy as np  \n",
    "import matplotlib.pyplot as plt  \n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30\n",
       "5    1.5      20\n",
       "6    9.2      88\n",
       "7    5.5      60\n",
       "8    8.3      81\n",
       "9    2.7      25"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#loading dataset\n",
    "df = pd.read_csv('http://bit.ly/w-data')\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(25, 2)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking size of dataset\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Hours', 'Scores'], dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking all column names of dataset\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5.012000</td>\n",
       "      <td>51.480000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.525094</td>\n",
       "      <td>25.286887</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.100000</td>\n",
       "      <td>17.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.700000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.800000</td>\n",
       "      <td>47.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.400000</td>\n",
       "      <td>75.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.200000</td>\n",
       "      <td>95.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Hours     Scores\n",
       "count  25.000000  25.000000\n",
       "mean    5.012000  51.480000\n",
       "std     2.525094  25.286887\n",
       "min     1.100000  17.000000\n",
       "25%     2.700000  30.000000\n",
       "50%     4.800000  47.000000\n",
       "75%     7.400000  75.000000\n",
       "max     9.200000  95.000000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEWCAYAAABhffzLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nO3deZxcdZ3u8c9DEkiTBhsIxCQsYQQDSICQwLAIN2FJVBQyjIrjgInDGEe9GEQYwQ316oCD4zIzKKJ4EzfCDgoMBLOwDIuQBA0aIIhczCLbJECHYBL43j/OKVLpVHef6vSpOlX1vF+veqXqrE9Xd7516nfO+f0UEZiZWevYpt4BzMystlz4zcxajAu/mVmLceE3M2sxLvxmZi3Ghd/MrMW48JuZtRgX/iYh6SlJJ3SZNk3SPRWmLZH0iqQ/S/qepI6y+TMlfbXLOqMkhaSBZftaJ6kz3cZMSe1ly+8u6TpJz0t6Md3ftAqZR0raKOktFebdIOkb6fNTJD0s6aV0m3MljermfZgpaX2a7X8k3SFpv3TelyRtSOeVHmvK1g1Ja9PpKyR9U9KALtufLOkuSS9Lek7SnZJOLntvX+uy/U5JI8ret2ckDSnb3j9KWiBpzy7rlGfplHRM2TpfSucfXuHnHy7pB5JWpus9mb4npfeg9LvsmvG0bt7Pt0maI2m1pDWSFkp6V9n8HSV9W9LT6XaeSF8PLVumt7+58t/LGkn3SjqybP4ESa9XyHwk1icu/C1E0qeBrwPnAW8CjgD2Au6QtG2Vm3tPRLQDhwBjgQvK5v0E+FO67V2ADwHPdN1ARKwA5gJndMm5M/AuYJakfYAfA59OM+8NfBd4vYds/5pm2x14FphZNu+qiGgve3R0WffgdN3/BZwG/ENZrvcC16R5dgeGAV8E3lO2/n1dtt8eESvL5g8EZlR4L54uX6c8S/q4O82g9P36H2Bql/dtF+BeYHvgGGAH4FDgTuDELrvs6JLxqq6ZUr8E7kh/1t2ATwIvpfvbluT39zbgHcCOwFHAC8Dh6TJZ/+auSn/uocB8kve53MoK7+t93WS23kSEH03wAJ4CTugybRpwT/p8R6ATeH+XZdpJiuM/pK9nAl/tsswoIICBlfYF/CtwS9nrTuCQjLk/CPyhy7SPA4vS5+8FHq7ifdgsP3AS0Jk+/xLw0x7WDWCfstdXA5emzwU8DZzXw/pvvN89/I7OJynaHem0fwQW9JalbPqxwDrgdJICu23ZvK8CvwG26SHDZr/LXt7LoemyHd3M/0eSD/T2buZn/Zvb7PcCHJDud9f09QRgeZ7/f1rt4SP+1nEUMBi4vnxiRHQC/8WWR4SZSNodeCfwRNnk+4FLJX1A0p69bOIGYKikt5dNO4PkqBpgEbCfpG9JmqiyJqUM2dqBvwcWZ12nbN39SI6aSz/XaGAP4Npqt9XFQ8AC4Nw+rj+V5Ci8dIT+7rJ5JwA3RERP34aq8QLJz/9TSVMkDesy/wTgtvRvqJKq/+bSbwEfSve9euviW3dc+JvLjWkb6Zq07fq7ZfOGAs9HxMYK661K51e7r5dJmnSeBS4sm/c+4G7gC8AflbTPH1ZpIxGxjuRr/YcAJO0LjAN+ns5/kuSIbyTJEfjz6nJOoYJz05//CZKjy2ll895f/h5Jmt9l3UWS1gJLSQp06T3cJf13VQ/7BTiiy/b/UGGZLwJnSdq1l21tRtL2JO/tzyNiA8mHUHlzz1Dgz2XLn5xmeFnSnC6be75Lzv277i+Sw+2JJN9U/g1YpeT8xr7pIrvQ8/tRzd/c+9Pf2TrgI8B7u6w3okveNeXnSqw6LvzNZUpEdJQeJE0mJc+THFkPrLDe8HQ+wEZgUJf5g0ja1MuPJKdExA4kRXk/yv4TR8TqiDg/It5G0jb8MMkHhbrJPYvkP/5gkqP92yLi2bLt3R8R74+IXUmOwo8FPtftuwDfSN+DN0fEyRFRXnyvLn+PImJil3UPJfmwOA34a6BUXF5I/x3ew34B7u+y/S1OXEfEI8DNJM0+1fgbkt/PrenrnwHvLPsAeaE8X0T8Iv07+BTQ9RzO0C45l1baYUQsj4j/nf4cewFr2fRtbLP9VZD1bw7S3wvJ38sjJB/+5VZ2ydsREWt72Lf1wIW/ddwH/AU4tXxietT0TpKTdJC0Y4/qsu7ewJ8qNSFExJ0k7erfqLTTiHg+nTcC2LmbZe4mKSKnkLRd/7jScumyD5I0HRzY3TJbKxJXk7xnX0wnP0by7eZv+2k3F5Ic2Y6sYp2pJB9KT0v6M8k3pUHA36Xz5wJTJOXy/zoi/gRcyqb3/lfA5B6OvLP+zZXv43ngo8CXJPX2IWt95MLfIiLiReDLwH9IeoekQUouibwGWE5yJQ7AdcBJkiZJGqDkUsTPA7N72Py3gRMlHQIg6euSDpQ0UNIOwMeAJyLihR628WOSqz86SNqwSbf1dkkfkbRb+no/4GSS8wh5uxiYLunNabPHOcAXJH04vYxxmzTf5dVuOCKeIGmn/2SW5SWNBI4nadM/JH0cTPKelZp7vgnsBPxE0luU2CFdtmqSdpL0ZUn7pD/rUJKrnErvfenqresk7Zcus4ukz0p6VxV/c5uJiEeB24F/7ktu650LfwuJiH8FPktyBP4S8ADJf9zjI+Iv6TK/IzmCvIjk6pP70uW+3MN2nyMp3F9IJ21PctJ2DfAkSRPByb3E+zGwJ8llfX8pm74mXXeJpE7gtnTb/5rph97SaRWuB9+tm59rCcmlkOelr69l0yWeK0muaPkqcFPZakdW2H7F8xvAV9jUlNSbM0iubpoTEX8uPYB/Bw6SdGB6tHwE8CpwD/AySTNb6cO33JouGc+psM/1JN/+fkXy9/IIyRH8tPT9+AvJCd5HSS75fAn4NUmz3wPpMr3+zXXjEpIP3dLvZkSF97W/vn21HCUHMmZm1ip8xG9m1mJc+M3MWowLv5lZi3HhNzNrMZVurCicoUOHxqhRozItu3btWoYMKd4NfUXMVcRM4FzVKGImKGauImaCfHMtXLjw+fTGx83Vu7OgLI9x48ZFVvPnz8+8bC0VMVcRM0U4VzWKmCmimLmKmCki31zAQ+FO2szMzIXfzKzFuPCbmbWYhji5W8mGDRtYvnw5r7766mbT3/SmN7F0acWOBusq71yDBw9m9913Z9Cgrh1rmpltrmEL//Lly9lhhx0YNWoU5b39vvzyy+ywww51TFZZnrkighdeeIHly5ez995757IPM2seDVv4X3311S2KfquSxC677MJzzz1X7yhm1o0bF6/gktsfY+WadYzoaOO8yaOZMraaXrn7T8MWfsBFv4zfC7PiunHxCi64fgnrNrwGwIo167jg+iVA0g95rfnkrplZzi65/bE3in7Jug2vccntj9Uljwv/Vvja177G2972Ng466CAOOeQQHnjggXpHMrMCWrlmXVXT89bQTT3V6O/2tfvuu4+bb76ZRYsWsd122/H888+zfv36Pm9v48aNDBzYMr8Os5YyoqONFRWK/IiOtjqkaZEj/lL72oo16wg2ta/duHhFn7e5atUqhg4dynbbbQfA0KFDGTFiBA8++CBHHXUUBx98MIcffjgvv/wyr776Kh/72McYM2YMY8eOZf78+QDMnDmT973vfbznPe9h0qRJAFxyySUcdthhHHTQQVx44YVA0pfHSSedxMEHH8yBBx7IVVddtXVviJnV1HmTR9M2aMBm09oGDeC8yaPrkqclDjF7al/r61H/pEmT+MpXvsJb3/pWTjjhBE477TSOPPJITjvtNK666ioOO+wwXnrpJdra2vjOd74DwJIlS3j00UeZNGkSjz/+OJB8c/jtb3/LzjvvzJw5c1i2bBm//vWviQhOPvlk7rrrLp577jlGjBjBLbfcAsCLL764Fe+GmdVaqc5UanVYsGBZzfO0ROHPo32tvb2dhQsXcvfddzN//nxOO+00Pve5zzF8+HAOOywZYnXHHXcE4J577uHMM88EYL/99mOvvfZ6o/CfeOKJ7LzzzgDMmTOHOXPmMHbsWAA6OztZtmwZxxxzDOeeey6f+cxnePe7380xxxzT59xmVh9Txo6s2+WbXbVE4c+rfW3AgAFMmDCBCRMmMGbMGC699NKKl1VGD+Mal3fHGhFccMEFfPSjH91iuYULF3LrrbdywQUXMGnSJL74xS9uVXYza10t0cafR/vaY489xrJlm76iPfzww+y///6sXLmSBx98EEju1t24cSPHHnssV199NQCPP/44Tz/9NKNHb7nvyZMn86Mf/YjOzk4AVqxYwbPPPsvKlSvZfvvtOf300zn33HNZtGhRn3ObmbXEEX9P7Wt91dnZyVlnncWaNWsYOHAg++yzD5dffjkf/vCHOeuss1i3bh1tbW386le/4uMf/zhnnnkmY8aMYeDAgcycOfONk8LlJk2axNKlSznyyCOBpDnppz/9KU888QTnnXce22yzDYMGDeJ73/ten3ObmbVE4Yf+b18bN24c99577xbThw4dyv3337/F9Msuu2yLvnqmTZvGtGnTNps2Y8YMZsyYsdm0t7zlLUyePHnrQ5uZ0SJNPWZmtkmuhV/SDEmPSPqdpLPTaTtLukPSsvTfnfLMYGZmm8ut8Es6EPgIcDhwMPBuSfsC5wNzI2JfYG76uk96ulqm1fi9MLOs8jzi3x+4PyJeiYiNwJ3A3wCnALPSZWYBU/qy8cGDB/PCCy+44LGpP/7BgwfXO4qZNQDlVTgl7Q/cBBwJrCM5un8IOCMiOsqWWx0RWzT3SJoOTAcYNmzYuNmzZ3edz5AhQxgwYPPLNCOikF0U553rtddeY+3atVV9EHZ2dtLe3p5bpr5yruyKmAmKmauImSDfXBMnTlwYEeO3mBERuT2AM4FFwF3AZcC3gDVdllnd23bGjRsXWc2fPz/zsrVUxFxFzBThXNUoYqaIYuYqYqaIfHMBD0WFmprr5ZwRcQVwBYCkfwGWA89IGh4RqyQNB57NM4OZWaPJe7SuvK/q2S39d0/gVOBK4BfA1HSRqSTNQWZmRj69CXeV93X810n6PfBL4BMRsRq4GDhR0jLgxPS1mZlRm9G68m7q2aIbyYh4ATg+z/2amTWqWozW5Tt3zcwKpLteg/tztC4XfjNreDcuXsHRF89j7/Nv4eiL5/Vre3it1WK0rpbppM3MmlPpZGipXbx0MhQozMAn1cijN+GuXPjNrKHlMbRqveU9WpcLv5k1nPLr3Lu7V70/T4Y2Gxd+M2soXZt2utOfJ0ObjU/umllDqdS001V/nwxtNj7iN7OG0lMTjiCXk6HNxoXfzBrKiI42VlQo/iM72vjv84+rQ6LG46YeM2sotbjOvdn5iN/MGkotrnNvdi78ZtZw8r7Ovdm5qcfMrMW48JuZtRg39ZiZlcl79KsicOE3M0s1W4dv3cl76MVPSfqdpEckXSlpsKS9JT0gaZmkqyRtm2cGM7OsajH6VRHkVvgljQQ+CYyPiAOBAcAHgK8D34qIfYHVwJl5ZTAzq0YtRr8qgrxP7g4E2iQNBLYHVgHHAdem82cBU3LOYGaWSS1GvyoCRXTXqWk/bFyaAXwNWAfMAWYA90fEPun8PYD/Sr8RdF13OjAdYNiwYeNmz56daZ+dnZ20t7f3zw/Qj4qYq4iZwLmqUcRMUMxcWTLdu3IDMx9Zz/rXN03bdhuYduC2HDViUN1y9dXEiRMXRsT4LWZERC4PYCdgHrArMAi4ETgDeKJsmT2AJb1ta9y4cZHV/PnzMy9bS0XMVcRMEc5VjSJmiihmrqyZbli0PI66aG6M+szNcdRFc+OGRcsLkasvgIeiQk3N86qeE4A/RsRzAJKuB44COiQNjIiNwO7AyhwzmJlVpRXuCs6zjf9p4AhJ20sScDzwe2A+8N50manATTlmMDOzLnIr/BHxAMlJ3EXAknRflwOfAc6R9ASwC3BFXhnMzGxLud7AFREXAhd2mfwkcHie+zUzs+65rx4zsxbjLhvMrM9aoV+bZuTCb2Z90lO/Nh31DGa9clOPmfVJq/Rr04x8xG9mfdJzvzZDahumRpqlactH/GbWJ63Sr01JqWlrxZp1BJuatm5cvKLe0armwm9mfXLe5NG0DRqw2bS2QQM4b/LoOiXKVzM1bbnwm1mfTBk7kotOHcPIjjYEjOxo46JTxzRk00cWzdRls9v4zazPWqFfm5IRHW2sqFDkG7Fpy0f8ZmYZNFPTlo/4zcwyKH2zaYarelz4zcwyapamLTf1mJm1mEyFX9Jekk5In7dJ2iHfWGZmlpdeC7+kj5D0q//9dNLuJMMomplZA8pyxP8J4GjgJYCIWAbslmcoMzPLT5bC/5eIWF96IWkgEL2tJGm0pIfLHi9JOlvSzpLukLQs/XenrfkBzMysOlkK/52SPgu0SToRuAb4ZW8rRcRjEXFIRBwCjANeAW4AzgfmRsS+wNz0tZmZ1UiWwn8+8BzJuLkfBW4FPl/lfo4H/hAR/w84BZiVTp8FTKlyW2ZmthV6vI5f0gBgVkScDvxgK/bzAeDK9PmwiFgFEBGrJPl8gZk1TZfHjUARPTfXS7odeE95O39VO5C2BVYCb4uIZyStiYiOsvmrI2KLdn5J04HpAMOGDRs3e/bsTPvr7Oykvb29L1FzVcRcRcwEzlWNImaC6nPdu3IDMx9Zz/rXN03bdhuYduC2HDViUF0y1UqeuSZOnLgwIsZ3nZ7lzt2ngP+W9AtgbWliRHwz477fCSyKiGfS189IGp4e7Q8Hnq20UkRcDlwOMH78+JgwYUKmnS1YsICsy9ZSEXMVMRM4VzWKmAmqz/W5i+dtVvQB1r8Otzw9gM9+MPt2+jNTrdQjV5Y2/pXAzemyO5Q9svo7NjXzAPwCmJo+nwrcVMW2zKwJNVOXx42g1yP+iPgyQHq3bkREZ9aNS9oeOJHkpHDJxcDVks4EngbeV1ViM2s6zdTlcSPotfBLOhD4CbBz+vp54EMR8bve1o2IV4Bdukx7geQqHzPrJ41+YvS8yaO54Polm41w1ahdHjeCLG38lwPnRMR8AEkTSK7wOSrHXGaWUWks2FLRLI0FCzRM8W+mLo8bQZbCP6RU9AEiYoGkITlmMrMq9DQWbCMVzmbp8rgRZCn8T0r6AklzD8DpwB/zi2Rm1fCJUatWlqt6/gHYFbg+fQwFPpxnKDPLrrsToD4xat3ptfBHxOqI+GREHJo+zo6I1bUIZ2a9a6axYK02svTHf4ek8jttd0rv5jWzApgydiQXnTqGkR1tCBjZ0cZFp45xe7l1K0sb/9CIWFN6ERGr3b+OWbH4xKhVI0sb/+uS9iy9kLQXGfrjNzOzYspyxP854B5Jd6avjyXtPM3MzBpPli4bbpN0KHBEOulTEfF8vrHMzCwv3Tb1SNpL0psA0kK/lqTfnQ+lXS2bmVkD6qmN/2pgCICkQ0iGXHwaOBj4bv7RzMwsDz019bRFxMr0+enAjyLi3yRtAzycfzQzK2n0TtisWHoq/Cp7fhxwAUBEvC6p8hpm1u966oSto6cVzbrRU1PPPElXS/oOsBMwDyAdNatPwzCaWfV66oTNrC96Kvxnk/TN8xTw9ojYkE5/M8klnmZWA+6Ezfpbt009kYzCvsUI5xGxONdEZrYZj05l/S3Lnbt9JqlD0rWSHpW0VNKRknZO+/9Zlv67U54ZzIrixsUrOPrieex9/i0cffE8bly8ItN67oTN+luuhR/4DnBbROxHchnoUuB8YG5E7AvMTV+bNbXSCdoVa9YRbDpBm6X4uxM2629ZumxAUhuwZ0RkPpskaUeS7h2mAUTEemC9pFOACelis4AFwGcyJzZrQFs7SpY7YbP+pKQpv4cFpPcA3wC2jYi905u5vhIRJ/ey3iEk4/X+nuRofyEwA1gREeXdPK+OiC2aeyRNJ+0TaNiwYeNmz97idENFnZ2dtLe3Z1q2loqYq4iZoDlzTbttbbfzZr6j7yOZNuN7lZciZoJ8c02cOHFhRIzvOj3LEf+XgMNJjsyJiIcljcqw3kDgUOCsiHggvSw0c7NORFxO8sHB+PHjY8KECZnWW7BgAVmXraUi5ipiJmjOXCPvn1fxBO3Ijrat+lmb8b3KSxEzQX1yZWnj3xgRL/Zh28uB5RHxQPr6WpIPgmfSewFK9wQ824dtmzUUn6C1IslS+B+R9EFggKR9Jf0HcG9vK0XEn4E/SSr9ZR9P0uzzC2BqOm0qcFP1sc0ai0/QWpFkaeo5i+SGrb8AVwK3A/8n4/bPAn6W9ub5JMkg7dsAV0s6k6TTt/dVG9qsEfkErRVFlv74XyEp/FXfrRsRDwNbnFggOfo3M7M66LXwS/olWw61+CLwEPD9iHg1j2BmZpaPLG38TwKdwA/Sx0vAM8Bb09dmZtZAsrTxj42IY8te/1LSXRFxrKTf5RXMzMzykeWIf1dJe5ZepM+Hpi/dPbOZWYPJcsT/aeAeSX8gGZxlb+DjkoaQdLlgZmYNJMtVPbdK2hfYj6TwP1p2QvfbeYYzM7P+l6mTNmBfYDQwGDhIEhHx4/ximdWOx7O1VpPlcs4LSXrTPAC4FXgncA/gwm8Nr6fxbF38rVllObn7XpIbrv4cER8m6Wlzu1xTmdWIx7O1VpSl8K+LiNeBjWkf+88Cf5VvLLPa8Hi21oqyFP6HJHWQ3Ky1EFgE/DrXVGY10t24tR7P1ppZr4U/Ij4eEWsi4jLgRGBq2uRj1vDcXbK1ol4Lv6S5pecR8VRE/LZ8mlkjc3fJ1oq6vapH0mBge2CopJ1IruEH2BEYUYNsZjXh7pKt1fR0OedHgbNJivxCNhX+l4BLc85lZmY56bbwR8R3gO9IOisi/qOGmczMLEdZumz4D0lHAaPKl89y566kp4CXgddIxu4dL2ln4Kp0e08B74+I1X3IbmZmfZDl5O5PgG8AbwcOSx+VRtXqzsSIOCQiSuucD8yNiH2BuelrMzOrkSx99YwHDoiIrqNw9dUpJF1AQNK75wLgM/20bTMz64V6q+eSrgE+GRGrqt649EdgNcnQjd+PiMslrYmIjrJlVkfEThXWnQ5MBxg2bNi42bNnZ9pnZ2cn7e3t1UbNXRFzFTETOFc1ipgJipmriJkg31wTJ05cWNbasklE9PgA5pMU79uBX5Qeva2Xrjsi/Xc34DfAscCaLsus7m0748aNi6zmz5+fedlaKmKuImaKcK5qFDFTRDFzFTFTRL65gIeiQk3N0tTzpb5+2kTEyvTfZyXdABwOPCNpeESskjScpO8fMzOrkSxdNtxJcvXNoPT5gyT99fRI0hBJO5SeA5OAR0i+MUxNF5sK3NSn5GZm1idZ+uP/CElb+87AW4CRwGUkXTX3ZBhwg6TSfn4eEbdJehC4WtKZwNPA+/oe38zMqpWlqecTJE00DwBExDJJu/W2UkQ8SdJ3f9fpL9D7h4ZZIXm0LmsGWQr/XyJifXrkjqSBJFfpmLWUe1du4CdzPVqXNb4s/fHfKemzQJukE4FrgF/mG8useK57fINH67KmkKXwnw88Bywh6bjtVuDzeYYyK6IXXq38RdejdVmjydLU0wb8KCJ+ACBpQDrtlTyDmRXNLoNVsfh7tC5rNFmO+OeSFPqSNuBX+cQxK66/fesgj9ZlTSFL4R8cEZ2lF+nz7fOLZFZMR40Y5NG6rClkaepZK+nQiFgEIGkc4EZNa0kercuaQZbCPwO4RtLK9PVw4LT8IpmZWZ56LPyStgG2BfYDRpMMv/hoRGyoQTYzM8tBj4U/Il6X9G8RcSRJPztmZtbgspzcnSPpb1W6ddfMzBpaljb+c4AhwGuS1pE090RE7JhrMjMzy0WWwdZ3qEUQKy53TGbWXLIMti5Jp0v6Qvp6D0mH5x/NiuDGxSu44PolrFizjmBTx2Q3Ll5R72hm1kdZ2vi/CxwJfDB93QlcmlsiK5RLbn+sITsmu3HxCo6+eB57n38LR188zx9UZmWytPH/dUQcKmkxQESslrRtzrmsILrrgKzIHZOVvqW4+2SzyrIc8W9IO2YLAEm7Aq9n3YGkAZIWS7o5fb23pAckLZN0lT9Eiq27DsiK3DFZo35LMauVLIX/34EbgN0kfQ24B/iXKvYxA1ha9vrrwLciYl9gNXBmFduyGjtv8uiG65isEb+lmNVSlsHWfwb8M3ARsAqYEhHXZNm4pN2Bk4Afpq8FHAdcmy4yC5hSfWyrlSljRzZcx2SN+C3FrJa6beOXNBj4J2AfkkFYvh8RG6vc/rdJPjRKl4TuAqwp285yksHbrcAarWOy8yaP3qyNH4r/LcWslhRReVQhSVcBG4C7gXcCT0XE2Zk3LL0beFdEfFzSBOBc4MPAfRGxT7rMHsCtETGmwvrTgekAw4YNGzd79uxM++3s7KS9vT1rzJopYq4iZoL+yXXvyg1c9/gGXng12GWw+Nu3DuKoEYPqnqu/FTETFDNXETNBvrkmTpy4MCLGbzEjIio+gCVlzwcCi7pbtpv1LyI5on8K+DPJiF0/A54HBqbLHAnc3tu2xo0bF1nNnz8/87K1VMRcRcwU4VzVKGKmiGLmKmKmiHxzAQ9FhZraUxv/Gz1wRvVNPETEBRGxe0SMAj4AzIuIvwfmA+9NF5sK3FTtts3MrO96KvwHS3opfbwMHFR6LumlrdjnZ4BzJD1B0uZ/xVZsy8zMqtTtyd2IGNDdvGpFxAJgQfr8ScBdPpiZ1UmW6/jNzKyJuPCbmbUYF34zsxbjwm9m1mKy9M5p1i88oItZMbjwW024q2Sz4nBTj9WEu0o2Kw4XfqsJd5VsVhwu/FYT7irZrDhc+K0mGnFAF7Nm5ZO7VhOlE7i+qses/lz4rWYabUAXs2blph4zsxbjwm9m1mJc+M3MWowLv5lZi3HhNzNrMbld1SNpMHAXsF26n2sj4kJJewOzgZ2BRcAZEbE+rxzNpKdOzurVAZo7XjNrPHlezvkX4LiI6JQ0CLhH0n8B5wDfiojZki4DzgS+l2OOptBTJ2dAXTpAc8drZo0pt6aeSHSmLweljwCOA65Np88CpuSVoZn01MlZvTpAc8drZo1JEZHfxqUBwEJgH+BS4BLg/ojYJ52/B/BfEXFghXWnA9MBhg0bNm727NmZ9tnZ2Ul7e3v//AD9aGtzTT5XV3EAAAsdSURBVLttbZ/Wm/mOId3OyzNTT/vtTbP+DvNQxExQzFxFzAT55po4ceLCiBjfdXqud+5GxGvAIZI6gBuA/Sst1s26lwOXA4wfPz4mTJiQaZ8LFiwg67K1tLW5Rt4/jxUVerIcmXZy1t28nvaZZ6at2W6z/g7zUMRMUMxcRcwE9clVk6t6ImINsAA4AuiQVPrA2R1YWYsMja6nTs7q1QGaO14za0x5XtWzK7AhItZIagNOAL4OzAfeS3Jlz1TgprwyNJMsnZzV+uoad7xm1pjybOoZDsxK2/m3Aa6OiJsl/R6YLemrwGLgihwzNJWeOjmrVwdo7njNrPHkVvgj4rfA2ArTnwQOz2u/tvV8bb5Zc3O3zLYZX5tv1vzcZYNtxtfmmzU/F37bjAdFN2t+Lvy2GQ+Kbtb8XPibxI2LV3D0xfPY+/xbOPriedy4eEWftuNr882an0/uNoH+PCHra/PNmp8Lfz+rx6WQPZ2Q7cu+fW2+WXNz4e9HPR15d+S4X5+QNbNquI2/H9XrUkifkDWzarjw96N6HXn7hKyZVcOFvx/V68h7ytiRXHTqGEZ2tCGSbpEvOnWM2+nNrCK38fej8yaP3qyNH8qOvF9cluu+fULWzLLyEX8/8pG3mTUCH/H3Mx95m1nRufA3EHeXbGb9wYW/Qbi7ZDPrL7m18UvaQ9J8SUsl/U7SjHT6zpLukLQs/XenvDL0VX/1e9Of3F2ymfWXPE/ubgQ+HRH7kwyy/glJBwDnA3MjYl9gbvq6MEpH1ivWrCPYdGRd7+Lvu3PNrL/kVvgjYlVELEqfvwwsBUYCpwCz0sVmAVPyytAXRT2y9t25ZtZfFBH570QaBdwFHAg8HREdZfNWR8QWzT2SpgPTAYYNGzZu9uzZmfbV2dlJe3t7n7NOu21tt/NmvmNIn7e7tbnuXbmBmY+sZ/3rm6Ztuw1MO3BbjhoxqC6Z8uJc2RUxExQzVxEzQb65Jk6cuDAixnednvvJXUntwHXA2RHxkqRM60XE5cDlAOPHj48JEyZkWm/BggVkXbaSkffPY0WF5pORHW1btd2tzTUBOKCfr+rZ2kx5ca7sipgJipmriJmgPrlyLfySBpEU/Z9FxPXp5GckDY+IVZKGA8/mmaFaPd59W2e+R8DM+kOeV/UIuAJYGhHfLJv1C2Bq+nwqcFNeGfrCd9+aWbPL84j/aOAMYImkh9NpnwUuBq6WdCbwNPC+HDP0iY+szayZ5Vb4I+IeoLsG/ePz2m+J73I1M6usKe/c9V2uZmbda8reOYt6Lb6ZWRE0ZeH3Xa5mZt1rysLvu1zNzLrXlIXfY9CamXWvKU/ulk7g+qoeM7MtNWXhB1+Lb2bWnaZs6jEzs+658JuZtRgXfjOzFuPCb2bWYlz4zcxaTE1G4Npakp4D/l/GxYcCz+cYp6+KmKuImcC5qlHETFDMXEXMBPnm2isidu06sSEKfzUkPVRpqLF6K2KuImYC56pGETNBMXMVMRPUJ5ebeszMWowLv5lZi2nGwn95vQN0o4i5ipgJnKsaRcwExcxVxExQh1xN18ZvZmY9a8YjfjMz64ELv5lZi2mawi/pR5KelfRIvbOUSNpD0nxJSyX9TtKMemcCkDRY0q8l/SbN9eV6ZyqRNEDSYkk31ztLiaSnJC2R9LCkh+qdp0RSh6RrJT2a/o0dWec8o9P3qPR4SdLZ9cxUIulT6d/6I5KulDS4AJlmpHl+V+v3qWna+CUdC3QCP46IA+udB0DScGB4RCyStAOwEJgSEb+vcy4BQyKiU9Ig4B5gRkTcX89cAJLOAcYDO0bEu+udB5LCD4yPiELd/CNpFnB3RPxQ0rbA9hGxpt65IPkAB1YAfx0RWW++zCvLSJK/8QMiYp2kq4FbI2JmHTMdCMwGDgfWA7cBH4uIZbXYf9Mc8UfEXcD/1DtHuYhYFRGL0ucvA0uBug8SEInO9OWg9FH3IwBJuwMnAT+sd5aik7QjcCxwBUBErC9K0U8dD/yh3kW/zECgTdJAYHtgZZ3z7A/cHxGvRMRG4E7gb2q186Yp/EUnaRQwFnigvkkSaZPKw8CzwB0RUYRc3wb+GXi93kG6CGCOpIWSptc7TOqvgOeA/5s2jf1Q0pB6hyrzAeDKeocAiIgVwDeAp4FVwIsRMae+qXgEOFbSLpK2B94F7FGrnbvw14CkduA64OyIeKneeQAi4rWIOATYHTg8/epZN5LeDTwbEQvrmaMbR0fEocA7gU+kzYr1NhA4FPheRIwF1gLn1zdSIm12Ohm4pt5ZACTtBJwC7A2MAIZIOr2emSJiKfB14A6SZp7fABtrtX8X/pylbejXAT+LiOvrnaertHlgAfCOOkc5Gjg5bU+fDRwn6af1jZSIiJXpv88CN5C0y9bbcmB52Te1a0k+CIrgncCiiHim3kFSJwB/jIjnImIDcD1wVJ0zERFXRMShEXEsSTN1Tdr3wYU/V+lJ1CuApRHxzXrnKZG0q6SO9HkbyX+MR+uZKSIuiIjdI2IUSTPBvIio61EZgKQh6Yl50qaUSSRf0+sqIv4M/EnS6HTS8UBdLxoo83cUpJkn9TRwhKTt0/+Tx5Ocb6srSbul/+4JnEoN37OmGWxd0pXABGCopOXAhRFxRX1TcTRwBrAkbU8H+GxE3FrHTADDgVnplRfbAFdHRGEunyyYYcANSb1gIPDziLitvpHecBbws7Rp5Ungw3XOQ9pefSLw0XpnKYmIByRdCywiaU5ZTDG6b7hO0i7ABuATEbG6Vjtumss5zcwsGzf1mJm1GBd+M7MW48JvZtZiXPjNzFqMC7+ZWYtx4beGJKmzy+tpkv6zhvs/QtIDaS+USyV9KZ0+QVLVNwdJminpvenzH0o6oIp1JxSpN1Mrvqa5jt+sP0gaEBGvZVh0FvD+iPhNej9E6UaqCSS9xN7b1wwR8Y99XdcsCx/xW9ORtJekuZJ+m/67Zzr9jaPq9HVn+u+EdNyEn5PcbDdE0i3peAWPSDqtwm52I+nwq9Tv0e/Tjvj+CfhU+k3gmB72KUn/Ken3km5Jt1daZoGk8enzSZLuk7RI0jVpv09IeoeSfvjvIbnr0ywzF35rVG0qG/QD+ErZvP8kGZfhIOBnwL9n2N7hwOci4gCSfotWRsTB6dgOle7U/RbwmKQbJH1U0uCIeAq4DPhWRBwSEXf3sL+/IfmWMAb4CBX6jpE0FPg8cELaSdxDwDlKBhH5AfAe4BjgzRl+PrM3uPBbo1qXFtdD0l5Gv1g270jg5+nznwBvz7C9X0fEH9PnS4ATJH1d0jER8WLXhSPiKyQDxswBPkjlD4eeHAtcmX5bWAnMq7DMEcABwH+nH25Tgb2A/Ug6HVsWya33hejMzhqHC7+1glK/JBtJ/+bTzrq2LVtm7RsLRzwOjCP5ALhIUvmHCmXL/SEivkfS6dfBab8rXfW0z976SxHJWAmlD7gDIuLMjOuadcuF35rRvSQ9fAL8PcmwewBPkRR0SPpnH1RpZUkjgFci4qckA3hs0d2xpJPSQg6wL/AasAZ4GdihbNHu9nkX8IF0QJzhwMQKUe4Hjpa0T7rP7SW9laQn1b0lvSVd7u8q/Rxm3fFVPdaMPgn8SNJ5JKNUlXqt/AFwk6RfA3MpO8rvYgxwiaTXSXpO/FiFZc4AviXpFZKj+r+PiNck/RK4VtIpJL1ndrfPG4DjSL5VPE4y9N5mIuI5SdOAKyVtl07+fEQ8rmQksFskPU/ywVaIcaatMbh3TjOzFuOmHjOzFuPCb2bWYlz4zcxajAu/mVmLceE3M2sxLvxmZi3Ghd/MrMX8fxkzObhInDQxAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the distribution of scores\n",
    "df.plot(x='Hours', y='Scores', style = 'o')  \n",
    "plt.title('HOURS VS PERCENTAGE SCORE')  \n",
    "plt.xlabel('Hours Studied')  \n",
    "plt.ylabel('Percentage Score')  \n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# From the graph above, we can clearly see that there is a positive linear relation between the number of hours studied \n",
    "and percentage of score."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Preparing the data\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### divide the data into \"attributes\" (inputs) and \"labels\" (outputs)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df.iloc[:, :-1].values  \n",
    "y = df.iloc[:, 1].values  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### next step is to split this data into training and test sets by using Scikit-Learn's built-in train_test_split() method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split  \n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=0) \n",
    "\n",
    "#Training the Algorithm\n",
    "from sklearn.linear_model import LinearRegression  \n",
    "model = LinearRegression()  \n",
    "model.fit(x_train, y_train) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the regression line\n",
    "line = model.coef_*x + model.intercept_\n",
    "\n",
    "# Plotting for the test data\n",
    "plt.scatter(x, y)\n",
    "plt.plot(x, line)\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Making Predictions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.5]\n",
      " [3.2]\n",
      " [7.4]\n",
      " [2.5]\n",
      " [5.9]]\n",
      "[16.88414476 33.73226078 75.357018   26.79480124 60.49103328]\n"
     ]
    }
   ],
   "source": [
    "print(x_test) # Testing data - In Hours\n",
    "y_pred = model.predict(x_test) # Predicting the scores\n",
    "print(y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Actual  Predicted\n",
      "0      20  16.884145\n",
      "1      27  33.732261\n",
      "2      69  75.357018\n",
      "3      30  26.794801\n",
      "4      62  60.491033\n"
     ]
    }
   ],
   "source": [
    "# Comparing Actual vs Predicted\n",
    "pred_data = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  \n",
    "print(pred_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x15e236190c8>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot bar graph for predictive data\n",
    "data_plot = pred_data.head()\n",
    "data_plot.plot(kind = \"bar\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Evaluating the model\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The final step is to evaluate the performance of algorithm. This step is particularly important to compare how well different algorithms perform on a particular dataset. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THE TRAIN SCORE; 0.9515510725211553\n",
      "THE TEST SCORE; 0.9515510725211553\n",
      "MEAN ABSOLUTE ERROR : 4.183859899002975\n",
      "MEAN SQUARED ERROR : 21.5987693072174\n"
     ]
    }
   ],
   "source": [
    "print(f'THE TRAIN SCORE; {model.score(x_train,y_train)}')\n",
    "print(f'THE TEST SCORE; {model.score(x_train,y_train)}')\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import mean_squared_error\n",
    "print(f'MEAN ABSOLUTE ERROR :' ,mean_absolute_error(y_test,y_pred))\n",
    "print(f'MEAN SQUARED ERROR :' ,mean_squared_error(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Evaluating What will be predicted score if a student study for 9.25 hrs in a day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No of Hours : [[9.25]]\n",
      "Predicted Score : [93.69173249]\n"
     ]
    }
   ],
   "source": [
    "# Test with your own data\n",
    "hours = [[9.25]]\n",
    "pred = model.predict(hours)\n",
    "print(\"No of Hours : {}\".format(hours))\n",
    "print(\"Predicted Score : {}\".format(pred))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
