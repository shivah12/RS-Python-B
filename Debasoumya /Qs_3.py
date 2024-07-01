{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNB0Tpad2NtEN75KzLoOH+p",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def plusOne(self,digits):\n",
        "   n=len(digits)\n",
        "   digits[n-1]+=1\n",
        "   for i in range(n-1,-1,-1):\n",
        "     if digits[i]==10:\n",
        "       digits[i]=0\n",
        "       if i-1>=0:\n",
        "         digits[i-1]+=1\n",
        "       else:\n",
        "        digits.append(0)\n",
        "        digits[i]+=1\n",
        "   return[1]+digits"
      ],
      "metadata": {
        "id": "K2sm0NDJAeKL"
      },
      "execution_count": 15,
      "outputs": []
    }
  ]
}