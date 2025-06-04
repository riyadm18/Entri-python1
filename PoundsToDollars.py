{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7084a61b-7717-4aea-8d33-2b5649df25c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pounds = float(input(\"Please enter amount in pounds: \"))\n",
    "\n",
    "# Conversion rate (example: 1 pound = 1.25 dollars, you can update this as needed)\n",
    "conversion_rate = 1.25\n",
    "\n",
    "# Calculate amount in dollars\n",
    "dollars = pounds * conversion_rate\n",
    "\n",
    "# Display result\n",
    "print(f\"£ {pounds} are $ {dollars:.2f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
