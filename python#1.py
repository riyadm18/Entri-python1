{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e6701f27-9833-485a-8c90-e60906f6b8f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Riya Derose Michael\n",
      "ST1234\n",
      "riyamichael@gmail.com\n"
     ]
    }
   ],
   "source": [
    "print(\"Riya Derose Michael\")\n",
    "print(\"ST1234\")\n",
    "print(\"riyamichael@gmail.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "98579ae9-ff08-4ea3-9b48-264a3ce8bce9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Riya Derose Michael\n",
      "ST1234\n",
      "riyamichael@gmail.com\n"
     ]
    }
   ],
   "source": [
    "print(\"Riya Derose Michael\\nST1234\\nriyamichael@gmail.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fe2cd15a-6ebd-4134-bd8b-c0c5485d7fc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14 + 7 = 21\n",
      "14 * 7 = 98\n",
      "14 - 7 = 7\n",
      "14 / 7 = 2.0\n"
     ]
    }
   ],
   "source": [
    "a = 14\n",
    "b = 7\n",
    "\n",
    "print(a, \"+\", b, \"=\", a + b)\n",
    "print(a, \"*\", b, \"=\", a * b)\n",
    "print(a, \"-\", b, \"=\", a - b)\n",
    "print(a, \"/\", b, \"=\", a / b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "000dd248-0a1e-4d22-99cd-6aa26688f474",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 6):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8fdbbafa-4507-4f3c-be34-0c25d63d5f72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"SDK\" stands for \"Software Development Kit\", whereas\n",
      "\"IDE\" stands for \"Integrated Development Environment\".\n"
     ]
    }
   ],
   "source": [
    "print(\"\\\"SDK\\\" stands for \\\"Software Development Kit\\\", whereas\\n\\\"IDE\\\" stands for \\\"Integrated Development Environment\\\".\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8080413c-16f6-4b21-9848-2591b24b9c3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is an \"awesome\" language.\n",
      "python\n",
      "\t2023\n",
      "I'm from Entri\n",
      "5\n",
      "e\n",
      "Entri\n",
      "2023\n",
      "Entr2023\n",
      "Entri*20"
     ]
    }
   ],
   "source": [
    "print(\"python is an \\\"awesome\\\" language.\")\n",
    "print(\"python\\n\\t2023\")\n",
    "print('I\\'m from Entri.\\b')         \n",
    "print(\"\\65\")                        \n",
    "print(\"\\x65\")                       \n",
    "print(\"Entri\", \"2023\", sep=\"\\n\")   \n",
    "print(\"Entri\", \"2023\", sep=\"\\b\")   \n",
    "print(\"Entri\", \"2023\", sep=\"*\", end=\"\\b\\b\\b\\b\")  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "be39f28d-831a-4bef-b00c-1fdb675dc5d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'str'>\n",
      "<class 'float'>\n",
      "Sum: 178.3\n",
      "Type of sum: <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "num = 23\n",
    "textnum = \"57\"\n",
    "decimal = 98.3\n",
    "\n",
    "print(type(num))       \n",
    "print(type(textnum))   \n",
    "print(type(decimal))   \n",
    "\n",
    "sum_total = num + int(textnum) + decimal\n",
    "print(\"Sum:\", sum_total)\n",
    "print(\"Type of sum:\", type(sum_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b08b377d-49ef-4fea-8ede-e59bc67b8a33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This program calculates the number of minutes in a year.\n",
      "Minutes in a year: 525600\n"
     ]
    }
   ],
   "source": [
    "days_in_year = 365\n",
    "hours_in_day = 24\n",
    "minutes_in_hour = 60\n",
    "minutes_in_year = days_in_year * hours_in_day * minutes_in_hour\n",
    "\n",
    "print(\"This program calculates the number of minutes in a year.\")\n",
    "print(\"Minutes in a year:\", minutes_in_year)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8b2c5185-6ef1-4c5a-ba9c-969055fed734",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter your name:  Riya\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi Riya, welcome to Python programming :)\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Please enter your name: \")\n",
    "print(f\"Hi {name}, welcome to Python programming :)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c95bdc8-f8a1-4e02-989c-17bedc1a7d87",
   "metadata": {},
   "outputs": [],
   "source": []
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
