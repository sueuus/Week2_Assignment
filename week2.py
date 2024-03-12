{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b532d7a8-2e0f-4cf1-a829-416a36c2e907",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /opt/anaconda3/lib/python3.11/site-packages (2.1.4)\n",
      "Requirement already satisfied: numpy<2,>=1.23.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in /opt/anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "7c8339b0-dc12-4f88-9a20-532473032a0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "425fa058-33ae-4f1e-a43c-18437f71873c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Manufacturer    Model     Type\n",
      "0         Acura  Integra    Small\n",
      "20     Chrysler  LeBaron  Compact\n",
      "40        Honda  Prelude   Sporty\n",
      "60      Mercury   Cougar  Midsize\n",
      "80       Subaru   Loyale    Small\n"
     ]
    }
   ],
   "source": [
    "#Task 1 From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).\n",
    "df1 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')\n",
    "f_df1 = df1.iloc[::20, :][['Manufacturer', 'Model', 'Type']]\n",
    "print(f_df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1ea363c4-fcda-4fc7-a70d-992e7cb40d74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Manufacturer    Model     Type  Min.Price  Price  Max.Price  MPG.city  \\\n",
      "0         Acura  Integra    Small  12.900000   15.9  18.800000      25.0   \n",
      "1           NaN   Legend  Midsize  29.200000   33.9  38.700000      18.0   \n",
      "2          Audi       90  Compact  25.900000   29.1  32.300000      20.0   \n",
      "3          Audi      100  Midsize  17.118605   37.7  44.600000      19.0   \n",
      "4           BMW     535i  Midsize  17.118605   30.0  21.459091      22.0   \n",
      "..          ...      ...      ...        ...    ...        ...       ...   \n",
      "88   Volkswagen  Eurovan      Van  16.600000   19.7  22.700000      17.0   \n",
      "89   Volkswagen   Passat  Compact  17.600000   20.0  22.400000      21.0   \n",
      "90   Volkswagen  Corrado   Sporty  22.900000   23.3  23.700000      18.0   \n",
      "91        Volvo      240  Compact  21.800000   22.7  23.500000      21.0   \n",
      "92          NaN      850  Midsize  24.800000   26.7  28.500000      20.0   \n",
      "\n",
      "    MPG.highway             AirBags DriveTrain  ... Passengers  Length  \\\n",
      "0          31.0                 NaN      Front  ...        5.0   177.0   \n",
      "1          25.0  Driver & Passenger      Front  ...        5.0   195.0   \n",
      "2          26.0         Driver only      Front  ...        5.0   180.0   \n",
      "3          26.0  Driver & Passenger        NaN  ...        6.0   193.0   \n",
      "4          30.0                 NaN       Rear  ...        4.0   186.0   \n",
      "..          ...                 ...        ...  ...        ...     ...   \n",
      "88         21.0                 NaN      Front  ...        7.0   187.0   \n",
      "89         30.0                 NaN      Front  ...        5.0   180.0   \n",
      "90         25.0                 NaN      Front  ...        4.0   159.0   \n",
      "91         28.0         Driver only       Rear  ...        5.0   190.0   \n",
      "92         28.0  Driver & Passenger      Front  ...        5.0   184.0   \n",
      "\n",
      "    Wheelbase  Width  Turn.circle Rear.seat.room  Luggage.room  Weight  \\\n",
      "0       102.0   68.0         37.0           26.5           NaN  2705.0   \n",
      "1       115.0   71.0         38.0           30.0          15.0  3560.0   \n",
      "2       102.0   67.0         37.0           28.0          14.0  3375.0   \n",
      "3       106.0    NaN         37.0           31.0          17.0  3405.0   \n",
      "4       109.0   69.0         39.0           27.0          13.0  3640.0   \n",
      "..        ...    ...          ...            ...           ...     ...   \n",
      "88      115.0   72.0         38.0           34.0           NaN  3960.0   \n",
      "89      103.0   67.0         35.0           31.5          14.0  2985.0   \n",
      "90       97.0   66.0         36.0           26.0          15.0  2810.0   \n",
      "91      104.0   67.0         37.0           29.5          14.0  2985.0   \n",
      "92      105.0   69.0         38.0           30.0          15.0  3245.0   \n",
      "\n",
      "     Origin                Make  \n",
      "0   non-USA       Acura Integra  \n",
      "1   non-USA        Acura Legend  \n",
      "2   non-USA             Audi 90  \n",
      "3   non-USA            Audi 100  \n",
      "4   non-USA            BMW 535i  \n",
      "..      ...                 ...  \n",
      "88      NaN  Volkswagen Eurovan  \n",
      "89  non-USA   Volkswagen Passat  \n",
      "90  non-USA  Volkswagen Corrado  \n",
      "91  non-USA           Volvo 240  \n",
      "92  non-USA           Volvo 850  \n",
      "\n",
      "[93 rows x 27 columns]\n"
     ]
    }
   ],
   "source": [
    "#Task 2 Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).\n",
    "df2 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')\n",
    "df2['Min.Price'].fillna(df2['Min.Price'].mean(), inplace=True)\n",
    "df2['Max.Price'].fillna(df2['Max.Price'].mean(), inplace=True)\n",
    "print(df2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f53da0ef-ab05-4124-afff-9be446689b2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     0   1   2   3\n",
      "2   35  15  22  31\n",
      "3   37  33  36  38\n",
      "7   21  29  39  25\n",
      "11  19  30  27  37\n",
      "13  18  31  30  35\n",
      "14  34  13  38  29\n"
     ]
    }
   ],
   "source": [
    "#Task 3 How to get the rows of a dataframe with row sum > 100?\n",
    "df3 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))\n",
    "f_df3 = df3[df3.sum(axis=1) > 100]\n",
    "print(f_df3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "57c7ed6e-1fe0-45a1-b955-6ad8eef8c638",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[35 84  6 74]\n",
      " [25 14 60 21]\n",
      " [ 1 36 17  6]\n",
      " [43 96 47 88]]\n",
      "[199 120  60 274]\n",
      "[104 230 130 189]\n"
     ]
    }
   ],
   "source": [
    "#Task 4 \n",
    "array = np.random.randint(1, 100, size=(4, 4))\n",
    "row_sums = np.apply_along_axis(lambda x: np.sum(x), axis=1, arr=array)\n",
    "column_sums = np.apply_along_axis(lambda x: np.sum(x), axis=0, arr=array)\n",
    "print(array)\n",
    "print(row_sums)\n",
    "print(column_sums)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
