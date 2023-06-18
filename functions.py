{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee6183eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_gender_column(df1: pd.DataFrame) -> pd.DataFrame:\n",
    "    '''\n",
    "    This function will take a Pandas DataFrame as an input and it will replace the values in\n",
    "    the \"GENDER\" column ins such a way that any gender which is not Male or Female with be \n",
    "    replaced by \"U\" otherwise the genders will be either \"F\" or \"M\"\n",
    "\n",
    "    Inputs:\n",
    "    df: Pandas DataFrame\n",
    "\n",
    "    Outputs:\n",
    "    A pandas DataFrame with the values in the \"gender\" column cleaned.\n",
    "    '''\n",
    "\n",
    "    df2 = df1.copy()\n",
    "    \n",
    "    df2[['GENDER']] = df2[['GENDER']].astype(str)\n",
    "\n",
    "    if \"GENDER\" not in df2.columns:\n",
    "        return df2\n",
    "    else:\n",
    "        #df2['GENDER'] = df2['GENDER'].apply(lambda x: x[0].upper if x[0].upper in ['M', 'F'] else \"U\")\n",
    "        df2['GENDER'] = list(map(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else \"U\", df2['GENDER']))\n",
    "        return df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ba9da40",
   "metadata": {},
   "outputs": [],
   "source": [
    "def drop_null(df1: pd.DataFrame) -> pd.DataFrame:\n",
    "    '''\n",
    "    This function will drop null values from df1\n",
    "    \n",
    "    Inputs:\n",
    "    df: Pandas DataFrame\n",
    "\n",
    "    Outputs:\n",
    "    A pandas DataFrame with the values null values dropped.\n",
    "    '''\n",
    "\n",
    "    df2 = df1.copy()\n",
    "    df3 = df2.dropna()\n",
    "    return df3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db12e75b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def drop_duplicates(df1: pd.DataFrame) -> pd.DataFrame:\n",
    "    '''\n",
    "    This function will drop duplicates  from df1\n",
    "    \n",
    "    Inputs:\n",
    "    df: Pandas DataFrame\n",
    "\n",
    "    Outputs:\n",
    "    A pandas DataFrame with the values null values dropped.\n",
    "    '''\n",
    "\n",
    "    df2 = df1.copy()\n",
    "    df3 = df2.drop_duplicates())\n",
    "    return df3"
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
